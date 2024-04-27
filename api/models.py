from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from ulid import ULID


# Create your models here.
class Customer(AbstractUser):
    ulid = models.CharField(_("ULID"), max_length=26, default=ULID(), unique=True)
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    middle_name = models.CharField(_("Middle Name"), max_length=255, blank=True)
    dob = models.DateField(_("Date of Birth"))
    nationality = CountryField(_("Nationality"))
    phone_number = models.CharField(_("Phone Number"), max_length=15, unique=True, blank=True, null=True)
    email = models.EmailField(_("Email"), unique=True, blank=True, null=True)

    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        if len(self.phone_number) < 10:
            raise ValueError("Phone number should be at least 10 digits")
        if self.phone_number[0] == "+":
            self.phone_number = self.phone_number[1:]
        if len(self.phone_number) == 10:
            self.phone_number = f"254{self.phone_number[1:]}"
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class BusinessCategory(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Business Categories")


class Business(models.Model):
    ulid = models.CharField(_("ULID"), max_length=26, default=ULID(), unique=True)
    business_name = models.CharField(_("Business Name"), max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(_("Registration Date"), auto_now_add=True)

    @property
    def business_category(self) -> str:
        """
        This property gives the business category name.

        Returns:
            str: The name of the business category.
        """
        return self.category.name

    @property
    def business_age(self) -> int:
        """
          This property gives the age of the business in years, months or days.

          Returns:
              int: The age of the business in days.
        """
        age = timezone.now() - self.registration_date
        return age.days

    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name_plural = _("Businesses")


class County(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Counties")


class SubCounty(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Sub Counties")


class Ward(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Wards")


class Location(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Locations")
