from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Business, BusinessCategory, County, SubCounty, Area, Ward
from .serializers import CustomerSerializer, CountySerializer, SubCountySerializer, BusinessSerializer, \
    BusinessCategorySerializer, LocationSerializer, WardSerializer
from utils.token import get_auth_token, get_user
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


# Create your views here.

@receiver(post_save, sender=Customer)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class StatusView(APIView):
    def get(self, request):
        json = {
            "statusCode": 200,
            "body": "OK"
        }
        return Response(json)


class CustomerView(APIView):
    def get(self, request, customer_ulid=None):
        data = {}
        user, err = get_user(request)
        if err is not None:
            data["statusCode"] = 400
            data["body"] = str(err)
            return Response(data, status=400)

        if customer_ulid is not None:
            customer = get_object_or_404(Customer, ulid=customer_ulid)

            if user.is_staff or user == customer:
                serializer = CustomerSerializer(customer)
                data["statusCode"] = 200
                data["body"] = serializer.data
                return Response(data)
            else:
                data["statusCode"] = 403
                data["body"] = "Forbidden | You do not have permission to access this resource"
                return Response(data, status=403)
        else:
            data["statusCode"] = 200
            data["body"] = user
            return Response(data)

    def delete(self, request, ulid):
        data = {}
        user, err = get_user(request)
        if err is not None:
            data["statusCode"] = 400
            data["body"] = str(err)
            return Response(data, status=400)

        customer = get_object_or_404(Customer, ulid=ulid)

        if user.is_staff or user == customer:
            customer.delete()
            data["statusCode"] = 200
            data["body"] = "Customer deleted successfully"
            return Response(data)
        else:
            data["statusCode"] = 403
            data["body"] = "Not Allowed | You still have to explicitly pass the ulid even if there exists an auth token"
            return Response(data, status=403)

    def post(self, request):
        new_customer = CustomerSerializer(data=request.data)
        data = {}
        if new_customer.is_valid():
            new_customer.save()
            data["statusCode"] = 201
            data["body"] = new_customer.data
            return Response(data, status=201)
        else:
            data["statusCode"] = 400
            data["body"] = new_customer.errors
            return Response(data, status=400)


class BusinessView(APIView):
    def get(self, request, business_ulid=None):
        data = {}
        if business_ulid is not None:
            business = get_object_or_404(Business, ulid=business_ulid)
            serializer = BusinessSerializer(business)
            data["statusCode"] = 200
            data["body"] = serializer.data
            return Response(data)
        else:
            businesses = Business.objects.all()
            serializer = BusinessSerializer(businesses, many=True)
            data["statusCode"] = 200
            data["body"] = serializer.data
            return Response(data)

    def post(self, request):
        new_business = BusinessSerializer(data=request.data)
        data = {}
        if new_business.is_valid():
            new_business.save()
            data["statusCode"] = 201
            data["body"] = new_business.data
            return Response(data, status=201)
        else:
            data["statusCode"] = 400
            data["body"] = new_business.errors
            return Response(data, status=400)

    def delete(self, request, ulid):
        data = {}
        user, err = get_user(request)
        if err is not None:
            data["statusCode"] = 400
            data["body"] = str(err)
            return Response(data, status=400)

        if user.is_staff:
            business = get_object_or_404(Business, ulid=ulid)
            business.delete()
            data["statusCode"] = 200
            data["body"] = "Business deleted successfully"
            return Response(data)
        else:
            data["statusCode"] = 403
            data["body"] = "Forbidden | You do not have permission to access this resource"
            return Response(data, status=403)


class BusinessCategoryView(APIView):
    def get(self):
        categories = BusinessCategory.objects.all()
        serializer = BusinessCategorySerializer(categories, many=True)
        data = {
            "statusCode": 200,
            "body": serializer.data
        }
        return Response(data)

    def post(self, request):
        new_category = BusinessCategorySerializer(data=request.data)
        data = {}
        if new_category.is_valid():
            new_category.save()
            data["statusCode"] = 201
            data["body"] = new_category.data
            return Response(data, status=201)
        else:
            data["statusCode"] = 400
            data["body"] = new_category.errors
            return Response(data, status=400)


class CountyView(APIView):
    def get(self, county_name=None):
        if county_name is not None:
            county = get_object_or_404(County, name=county_name)
            serializer = CountySerializer(county)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)
        else:
            counties = County.objects.all()
            serializer = CountySerializer(counties, many=True)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_county = CountySerializer(data=request.data)
        data = {}
        if new_county.is_valid():
            new_county.save()
            data["statusCode"] = 201
            data["body"] = new_county.data
            return Response(data, status=201)
        else:
            data["statusCode"] = 400
            data["body"] = new_county.errors
            return Response(data, status=400)


class SubCountyView(APIView):
    def get(self, county_name, subcounty_name=None):
        if subcounty_name is not None:
            sub_county = get_object_or_404(SubCounty, name=subcounty_name, county__name=county_name)
            serializer = SubCountySerializer(sub_county)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)
        else:
            sub_counties = SubCounty.objects.filter(county__name=county_name)
            serializer = SubCountySerializer(sub_counties, many=True)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_sub_county = SubCountySerializer(data=request.data)
        data = {}
        if new_sub_county.is_valid():
            new_sub_county.save()
            data["statusCode"] = 201
            data["body"] = new_sub_county.data
            return Response(data, status=201)
        else:
            data["statusCode"] = 400
            data["body"] = new_sub_county.errors
            return Response(data, status=400)


class WardView(APIView):
    def get(self, county_name, subcounty_name, ward_name=None):
        if ward_name is not None:
            ward = get_object_or_404(Ward, name=ward_name, sub_county__county__name=county_name,
                                     sub_county__name=subcounty_name)
            serializer = WardSerializer(ward)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)
        else:
            wards = Ward.objects.filter(sub_county__county__name=county_name, sub_county__name=subcounty_name)
            serializer = WardSerializer(wards, many=True)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_ward = WardSerializer(data=request.data)
        data = {}
        if new_ward.is_valid():
            new_ward.save()
            data["statusCode"] = 201
            data["body"] = new_ward.data
            return Response(data, status=201)
        else:
            data["statusCode"] = 400
            data["body"] = new_ward.errors
            return Response(data, status=400)


class AreaView(APIView):
    def get(self, county_name, subcounty_name, ward_name, area_name=None):
        if area_name is not None:
            area = get_object_or_404(Area, name=area_name, ward__sub_county__county__name=county_name,
                                     ward__sub_county__name=subcounty_name, ward__name=ward_name)
            serializer = LocationSerializer(area)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)
        else:
            areas = Area.objects.filter(ward__sub_county__county__name=county_name,
                                        ward__sub_county__name=subcounty_name,
                                        ward__name=ward_name)
            serializer = LocationSerializer(areas, many=True)
            data = {
                "statusCode": 200,
                "body": serializer.data
            }
            return Response(data)

    def post(self, request):
        new_location = LocationSerializer(data=request.data)
        data = {}
        if new_location.is_valid():
            new_location.save()
            data["statusCode"] = 201
            data["body"] = new_location.data
            return Response(data, status=201)
        else:
            data["statusCode"] = 400
            data["body"] = new_location.errors
            return Response(data, status=400)


@api_view(["GET"])
def get_business_customers(request, business_ulid):
    customers = Customer.objects.filter(business__ulid=business_ulid)
    serializer = CustomerSerializer(customers, many=True)
    data = {
        "statusCode": 200,
        "body": serializer.data
    }

    return Response(data)


@api_view(["GET"])
def get_customer_businesses(request):
    data = {}
    user, err = get_user(request)
    if err is not None:
        data["statusCode"] = 400
        data["body"] = str(err)
        return Response(data, status=400)

    businesses = Business.objects.filter(customer=user)
    serializer = BusinessSerializer(businesses, many=True)
    data["statusCode"] = 200
    data["body"] = serializer.data
    return Response(data)
