from rest_framework import serializers
from .models import Customer, Business, BusinessCategory, Area, County, SubCounty, Ward
from django_countries.serializer_fields import CountryField


class CustomerSerializer(serializers.ModelSerializer):
    """
    This serializer class is used to serialize the customer data.
    The nationality field is a CountryField that is used to store and parse the country data
    using the the django-countries package.
    """

    nationality = CountryField(name_only=True)

    class Meta:
        model = Customer
        fields = (
            "ulid",
            "first_name",
            "last_name",
            "middle_name",
            "nationality",
            "dob",
            "email",
            "phone_number",
        )


class BusinessSerializer(serializers.ModelSerializer):
    """
    This serializer class is used to serialize the business data.
    """

    business_category = serializers.CharField(source="category.name")

    class Meta:
        model = Business
        fields = (
            "business_name",
            "created_at",
            "business_category",
            "business_age",
            "business_email",
            "business_website",
            "business_address",
            "business_phone",
        )

    def create(self, validated_data):
        category = BusinessCategory.objects.get(
            name__iexact=validated_data.pop("category")["name"]
        )
        business = Business.objects.create(category=category, **validated_data)
        return business


class BusinessCategorySerializer(serializers.ModelSerializer):
    """
    This serializer class is used to serialize the business category data.
    """

    class Meta:
        model = BusinessCategory
        fields = ("name",)


class CountySerializer(serializers.ModelSerializer):
    """
    This serializer class is used to serialize the county data.
    """

    class Meta:
        model = County
        fields = "__all__"


class SubCountySerializer(serializers.ModelSerializer):
    """
    This serializer class is used to serialize the sub-county data.
    """

    county_name = serializers.CharField(source="county.name")

    class Meta:
        model = SubCounty
        fields = ("name", "county_name")

    def create(self, validated_data):
        county_name = validated_data.pop("county")["name"]
        county = County.objects.get(name__iexact=county_name)
        sub_county = SubCounty.objects.create(county=county, **validated_data)
        return sub_county


class WardSerializer(serializers.ModelSerializer):
    """
    This serializer class is used to serialize the ward data.
    """

    sub_county_name = serializers.CharField(source="sub_county.name")

    class Meta:
        model = Ward
        fields = ("name", "sub_county_name")

    def create(self, validated_data):
        sub_county_name = validated_data.pop("sub_county")["name"]
        sub_county = SubCounty.objects.get(name__iexact=sub_county_name)
        ward = Ward.objects.create(sub_county=sub_county, **validated_data)
        return ward


class AreaSerializer(serializers.ModelSerializer):
    """
    This serializer class is used to serialize the area data.
    """

    ward_name = serializers.CharField(source="ward.name")

    class Meta:
        model = Area
        fields = ("name", "ward_name")

    def create(self, validated_data):
        ward_name = validated_data.pop("ward")["name"]
        ward = Ward.objects.get(name__iexact=ward_name)
        area = Area.objects.create(ward=ward, **validated_data)
        return area
