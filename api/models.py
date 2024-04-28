import binascii
import os
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from ulid import ULID


class BusinessCategory(models.Model):
    """
    This model represents the categories of businesses that are available in the system.
    """

    name = models.CharField(_("Name"), max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Business Categories")


class Business(models.Model):
    """
    This model represents the businesses that are registered in the system.
    """

    ulid = models.CharField(_("ULID"), max_length=26, unique=True)
    business_name = models.CharField(_("Business Name"), max_length=255)
    category = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE)
    business_phone = models.CharField(
        _("Phone Number"), max_length=20, blank=True, null=True
    )
    business_email = models.EmailField(_("Email"), blank=True, null=True)
    business_address = models.TextField(_("Address"), blank=True, null=True)
    business_website = models.CharField(
        _("Website"), max_length=255, blank=True, null=True
    )
    created_at = models.DateTimeField(_("Registration Date"), auto_now_add=True)

    @property
    def business_age(self) -> int:
        """
        This property gives the age of the business in years, months or days.

        Returns:
            int: The age of the business in days.
        """
        age = timezone.now() - self.created_at
        return age.days

    @property
    def business_category(self):
        """
        This property returns the category of the business.
        """
        return self.category.name

    def save(self, *args, **kwargs):
        if not self.ulid or self.ulid.strip() == "":
            self.ulid = str(ULID())
        super(Business, self).save(*args, **kwargs)

    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name_plural = _("Businesses")


# Create your models here.
class Customer(models.Model):
    """
    This model represents the customers that are registered in the system.
    """

    ulid = models.CharField(_("ULID"), max_length=26, unique=True, blank=True)
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    middle_name = models.CharField(_("Middle Name"), max_length=255, blank=True)
    dob = models.DateField(_("Date of Birth"))
    nationality = CountryField(_("Nationality"))
    phone_number = models.CharField(_("Phone Number"), max_length=20, unique=True)
    email = models.EmailField(_("Email"), unique=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    businesses = models.ManyToManyField(Business, related_name="customers")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if len(self.phone_number) < 10:
            raise ValueError("Phone number should be at least 10 digits")
        if self.phone_number[0] == "+":
            self.phone_number = self.phone_number[1:]
        if len(self.phone_number) == 10:
            self.phone_number = f"254{self.phone_number[1:]}"
        if not self.ulid or self.ulid.strip() == "":
            self.ulid = str(ULID())
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class County(models.Model):
    """
    This model represents the counties that are available in the system.
    """

    name = models.CharField(_("Name"), max_length=255, unique=True)

    @property
    def sub_counties(self):
        """
        This property returns the sub counties that are available in the county.
        """
        return self.subcounty_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Counties")


class SubCounty(models.Model):
    """
    This model represents the sub counties that are available in the system.
    """

    name = models.CharField(_("Name"), max_length=255, unique=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def wards(self):
        """
        This property returns the wards that are available in the sub county.
        """
        return self.ward_set.all()

    class Meta:
        verbose_name_plural = _("Sub Counties")


class Ward(models.Model):
    """
    This model represents the wards that are available in the system.
    """

    name = models.CharField(_("Name"), max_length=255, unique=True)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def areas(self):
        """
        This property returns the areas that are available in the ward.
        """
        return self.area_set.all()

    class Meta:
        verbose_name_plural = _("Wards")


class Area(models.Model):
    """
    This model represents the areas that are available in the system.
    """

    name = models.CharField(_("Name"), max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Areas")


class Token(models.Model):
    """
    This model represents the tokens that are generated for the customers and users.
    """

    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, unique=True, blank=True, null=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
        unique=True,
        blank=True,
        null=True,
    )
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.customer and not self.user:
            raise ValueError("Either customer or user must be set")
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        """
        This method generates a random key for the token.
        """
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
