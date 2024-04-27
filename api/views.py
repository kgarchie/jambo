from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_countries.serializer_fields import CountryField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Business, BusinessCategory, County, SubCounty, Area, Ward, Token
from .paginators import UsersPagination
from .serializers import CustomerSerializer, CountySerializer, SubCountySerializer, BusinessSerializer, \
    BusinessCategorySerializer, LocationSerializer, WardSerializer
from utils.token import get_user_from_request, get_customer_from_request
from utils.cache import time_in_hours
from utils.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class StatusView(APIView):
    def get(self, request):
        json = {
            "statusCode": status.HTTP_200_OK,
            "body": "OK"
        }
        return Response(json)


class CustomerView(generics.GenericAPIView):
    pagination_class = UsersPagination
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all().order_by("created_at")

    def get(self, request, customer_ulid=None):
        data = {}
        user, err = get_user_from_request(request)

        if customer_ulid is not None:
            customer = get_object_or_404(Customer, ulid=customer_ulid)

            if (user is not None and user.is_staff) or user == customer:
                serializer = CustomerSerializer(customer)
                data["statusCode"] = status.HTTP_200_OK
                data["body"] = serializer.data
                return Response(data)
            else:
                data["statusCode"] = status.HTTP_403_FORBIDDEN
                data["body"] = "Forbidden | You do not have permission to access this resource"
                return Response(data, status=status.HTTP_403_FORBIDDEN)
        elif user:
            data["statusCode"] = status.HTTP_200_OK
            data["body"] = user
            return Response(data)
        else:
            page = self.paginate_queryset(self.queryset)
            data = {}
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                data["statusCode"] = status.HTTP_200_OK
                data["body"] = serializer.data
                return self.get_paginated_response(data)
            else:
                data["statusCode"] = status.HTTP_404_NOT_FOUND
                data["body"] = "No more data"
                return Response(data, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, customer_ulid):
        data = {}
        user, err = get_user_from_request(request)
        if err is not None:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = str(err)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        customer = get_object_or_404(Customer, ulid=customer_ulid)

        if (user is not None and user.is_staff) or user == customer:
            customer.delete()
            data["statusCode"] = status.HTTP_204_NO_CONTENT
            return Response(data, status.HTTP_204_NO_CONTENT)
        else:
            data["statusCode"] = status.HTTP_403_FORBIDDEN
            data["body"] = "Not Allowed | You still have to explicitly pass the ulid even if there exists an auth token"
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        new_customer = CustomerSerializer(data=request.data)
        data = {}
        if new_customer.is_valid():
            new_customer.save()
            data["statusCode"] = status.HTTP_201_CREATED
            data["body"] = new_customer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = new_customer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, customer_ulid):
        data = {}
        user, err = get_user_from_request(request)
        customer = get_object_or_404(Customer, ulid=customer_ulid)
        if (user is not None and user.is_staff) or user == customer:
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                data["statusCode"] = status.HTTP_200_OK
                data["body"] = serializer.data
                return Response(data)
            else:
                data["statusCode"] = status.HTTP_400_BAD_REQUEST
                data["body"] = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data["statusCode"] = status.HTTP_403_FORBIDDEN
            data["body"] = "Forbidden | You do not have permission to access this resource"
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class BusinessView(APIView):
    def get(self, request, business_ulid=None):
        data = {}
        if business_ulid is not None:
            business = get_object_or_404(Business, ulid=business_ulid)
            serializer = BusinessSerializer(business)
            data["statusCode"] = status.HTTP_200_OK
            data["body"] = serializer.data
            return Response(data)
        else:
            businesses = Business.objects.all()
            serializer = BusinessSerializer(businesses, many=True)
            data["statusCode"] = status.HTTP_200_OK
            data["body"] = serializer.data
            return Response(data)

    def post(self, request):
        new_business = BusinessSerializer(data=request.data)
        data = {}
        if new_business.is_valid():
            new_business.save()
            data["statusCode"] = status.HTTP_201_CREATED
            data["body"] = new_business.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = new_business.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, business_ulid):
        data = {}
        user, err = get_user_from_request(request)
        if err is not None:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = str(err)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if user.is_staff:
            business = get_object_or_404(Business, ulid=business_ulid)
            business.delete()
            data["statusCode"] = status.HTTP_200_OK
            data["body"] = "Business deleted successfully"
            return Response(data)
        else:
            data["statusCode"] = status.HTTP_403_FORBIDDEN
            data["body"] = "Forbidden | You do not have permission to access this resource"
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class BusinessCategoryView(APIView):
    @method_decorator(cache_page(time_in_hours(1)))
    def get(self):
        categories = BusinessCategory.objects.all()
        serializer = BusinessCategorySerializer(categories, many=True)
        data = {
            "statusCode": status.HTTP_200_OK,
            "body": serializer.data
        }
        return Response(data)

    def post(self, request):
        new_category = BusinessCategorySerializer(data=request.data)
        data = {}
        if new_category.is_valid():
            new_category.save()
            data["statusCode"] = status.HTTP_201_CREATED
            data["body"] = new_category.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = new_category.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class CountyView(APIView):
    @method_decorator(cache_page(time_in_hours(2)))
    def get(self, county_name=None):
        if county_name is not None:
            county = get_object_or_404(County, name=county_name)
            serializer = CountySerializer(county)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)
        else:
            counties = County.objects.all()
            serializer = CountySerializer(counties, many=True)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_county = CountySerializer(data=request.data)
        data = {}
        if new_county.is_valid():
            new_county.save()
            data["statusCode"] = status.HTTP_201_CREATED
            data["body"] = new_county.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = new_county.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class SubCountyView(APIView):
    @method_decorator(cache_page(time_in_hours(2)))
    def get(self, county_name, subcounty_name=None):
        if subcounty_name is not None:
            sub_county = get_object_or_404(SubCounty, name=subcounty_name, county__name=county_name)
            serializer = SubCountySerializer(sub_county)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)
        else:
            sub_counties = SubCounty.objects.filter(county__name=county_name)
            serializer = SubCountySerializer(sub_counties, many=True)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_sub_county = SubCountySerializer(data=request.data)
        data = {}
        if new_sub_county.is_valid():
            new_sub_county.save()
            data["statusCode"] = status.HTTP_201_CREATED
            data["body"] = new_sub_county.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = new_sub_county.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class WardView(APIView):
    @method_decorator(cache_page(time_in_hours(2)))
    def get(self, county_name, subcounty_name, ward_name=None):
        if ward_name is not None:
            ward = get_object_or_404(Ward, name=ward_name, sub_county__county__name=county_name,
                                     sub_county__name=subcounty_name)
            serializer = WardSerializer(ward)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)
        else:
            wards = Ward.objects.filter(sub_county__county__name=county_name, sub_county__name=subcounty_name)
            serializer = WardSerializer(wards, many=True)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_ward = WardSerializer(data=request.data)
        data = {}
        if new_ward.is_valid():
            new_ward.save()
            data["statusCode"] = status.HTTP_201_CREATED
            data["body"] = new_ward.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = new_ward.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class AreaView(APIView):
    @method_decorator(cache_page(time_in_hours(2)))
    def get(self, county_name, subcounty_name, ward_name, area_name=None):
        if area_name is not None:
            area = get_object_or_404(Area, name=area_name, ward__sub_county__county__name=county_name,
                                     ward__sub_county__name=subcounty_name, ward__name=ward_name)
            serializer = LocationSerializer(area)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)
        else:
            areas = Area.objects.filter(ward__sub_county__county__name=county_name,
                                        ward__sub_county__name=subcounty_name,
                                        ward__name=ward_name)
            serializer = LocationSerializer(areas, many=True)
            data = {
                "statusCode": status.HTTP_200_OK,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_location = LocationSerializer(data=request.data)
        data = {}
        if new_location.is_valid():
            new_location.save()
            data["statusCode"] = status.HTTP_201_CREATED
            data["body"] = new_location.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["statusCode"] = status.HTTP_400_BAD_REQUEST
            data["body"] = new_location.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_business_customers(request, business_ulid):
    customers = Customer.objects.filter(business__ulid=business_ulid)
    serializer = CustomerSerializer(customers, many=True)
    data = {
        "statusCode": status.HTTP_200_OK,
        "body": serializer.data
    }

    return Response(data)


@api_view(["GET"])
def get_customer_businesses(request):
    data = {}
    user, err = get_user_from_request(request)
    if err is not None:
        data["statusCode"] = status.HTTP_400_BAD_REQUEST
        data["body"] = str(err)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    businesses = Business.objects.filter(customer=user)
    serializer = BusinessSerializer(businesses, many=True)
    data["statusCode"] = status.HTTP_200_OK
    data["body"] = serializer.data
    return Response(data)


@api_view(["GET"])
def get_nationalities(request):
    nationalities = CountryField(name_only=True)
    data = {
        "statusCode": status.HTTP_200_OK,
        "body": nationalities
    }
    return Response(data)


@api_view(["POST", "PUT"])
def send_data_deletion_link(request, customer_ulid):
    data = {}
    customer = get_object_or_404(Customer, ulid=customer_ulid)
    user, err = get_customer_from_request(request)
    if err is not None:
        data["statusCode"] = status.HTTP_400_BAD_REQUEST
        data["body"] = str(err)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    origin = request.data.get("origin")
    if origin is None:
        data["statusCode"] = status.HTTP_400_BAD_REQUEST
        data["body"] = "Origin is required"
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if origin[-1] != "/":
        origin += "/"

    if user == customer:
        token = customer.token
        link = f"{origin}{reverse('api:confirm_delete_customer', args=[token])}"
        send_mail(subject="Request for data deletion",
                  body=f"Click the link below to delete your data\n{link}",
                  destination=customer.email)
        data["statusCode"] = status.HTTP_200_OK
        data["body"] = "Data deletion link sent successfully"
        return Response(data)
    else:
        data["statusCode"] = status.HTTP_403_FORBIDDEN
        data["body"] = "Forbidden | You do not have permission to access this resource"
        return Response(data, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET"])
def delete_customer(request, token):
    data = {}
    customer = get_object_or_404(Token, key=token).customer

    if customer is not None:
        customer.delete()
        data["statusCode"] = status.HTTP_200_OK
        data["body"] = "Customer deleted successfully"
        return Response(data)
    else:
        data["statusCode"] = status.HTTP_404_NOT_FOUND
        data["body"] = "Customer not found"
        return Response(data, status=status.HTTP_404_NOT_FOUND)
