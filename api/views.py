from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Business, BusinessCategory, County, SubCounty, Location, Ward
from .serializers import CustomerSerializer, CountySerializer, SubCountySerializer, BusinessSerializer, \
    BusinessCategorySerializer, LocationSerializer, WardSerializer
from utils.token import get_auth_token
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    def get(self, request, ulid=None):
        token = get_auth_token(request)
        data = {}
        if not token:
            data["statusCode"] = 401
            data["body"] = "Unauthorized | User token not provided on header"
            return Response(data, status=401)

        user = Token.objects.get(key=token).user
        if ulid is not None:
            customer = Customer.objects.get(ulid=ulid)

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
        token = get_auth_token(request)
        data = {}
        if not token:
            data["statusCode"] = 401
            data["body"] = "Unauthorized | User token not provided on header"
            return Response(data, status=401)

        user = Token.objects.get(key=token).user
        customer = Customer.objects.get(ulid=ulid)

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
    def get(self, request, ulid=None):
        data = {}
        if ulid is not None:
            business = Business.objects.get(customer__ulid=ulid)
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
        token = get_auth_token(request)
        data = {}
        if not token:
            data["statusCode"] = 401
            data["body"] = "Unauthorized | User token not provided on header"
            return Response(data, status=401)

        user = Token.objects.get(key=token).user

        if user.is_staff:
            business = Business.objects.get(ulid=ulid)
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
    def get(self):
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
    def get(self):
        sub_counties = SubCounty.objects.all()
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
    def get(self):
        wards = Ward.objects.all()
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


class LocationView(APIView):
    def get(self):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
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
