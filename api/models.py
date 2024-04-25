from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


# Create your models here.

class Customer(AbstractUser):
    dob = models.DateField(_("Date of Birth"), null=True)
    nationality = CountryField(_("Nationality"), null=True)

    def __str__(self):
        return self.username


class Contact(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    phone_number = models.CharField(_("Phone Number"), max_length=15, unique=True)
    email = models.EmailField(_("Email"), unique=True)

    def __str__(self):
        return self.customer.username


class BusinessCategory(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Business Categories")


class Business(models.Model):
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
