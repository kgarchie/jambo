from rest_framework import serializers
from .models import Customer, Business, BusinessCategory, Area, County, SubCounty, Ward
from django_countries.serializer_fields import CountryField


# from django_countries.serializers import CountryFieldMixin


class CustomerSerializer(serializers.ModelSerializer):
    nationality = CountryField(name_only=True)

    class Meta:
        model = Customer
        fields = ("ulid", "first_name", "last_name", "middle_name", "nationality", "dob", "email", "phone_number")


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ("business_name", "registration_date", "business_category", "business_age")


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = "__all__"


class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCounty
        fields = "__all__"


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"
