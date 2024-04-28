from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from ulid import ULID
from faker import Faker
from .models import (
    Customer,
    Token,
    Business,
    BusinessCategory,
    County,
    Ward,
    Area,
    SubCounty,
)
import json
from django.urls import reverse


fake = Faker()


def print_response(response, url=None):
    if url:
        print(f"\n## URL: {url}")
    print(f">Status Code: {response.status_code}")
    print(f">Content Type: {response['content-type']}")
    data = json.dumps(response.data, indent=4)
    print(f"```json\n{data}\n```")


def create_fake_customer():
    return {
        "ulid": str(ULID()),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "middle_name": fake.first_name(),
        "dob": str(fake.date_of_birth()),
        "nationality": fake.country_code(representation="alpha-2"),
        "phone_number": "+254" + fake.phone_number()[:9],
        "email": fake.email(),
    }


class CustomerViewTests(TestCase):
    superuser = None
    admin_token = None

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username="admin", email="admin@test.com", password="asd9032km2sd"
        )
        cls.admin_token = Token.objects.get_or_create(user=cls.superuser)[0]

    def setUp(self):
        self.client = APIClient()

    def test_create_customer(self):
        route = reverse("api:customers")
        data = create_fake_customer()
        response = self.client.post(
            route,
            data=json.dumps(data),
            content_type="application/json",
        )
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, data["first_name"])

    def test_get_customers(self):
        for _ in range(15):
            data = create_fake_customer()
            Customer.objects.create(**data)
        route = reverse("api:customers")
        response = self.client.get(route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_response(response, route)

    def test_get_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        self.client.credentials(Authorization=f"Bearer {self.admin_token}")
        route = reverse("api:customer", args=[customer.ulid])
        response = self.client.get(route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_response(response, route)

    def test_update_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        new_data = create_fake_customer()
        self.client.credentials(Authorization=f"Bearer {self.admin_token}")
        route = reverse("api:customer", args=[customer.ulid])
        response = self.client.put(
            route,
            data=json.dumps(new_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_response(response, route)

    def test_delete_customer_admin(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        self.client.credentials(Authorization=f"Bearer {self.admin_token}")
        route = reverse("api:customer", args=[customer.ulid])
        response = self.client.delete(route)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
        print_response(response, route)

    def test_delete_customer_with_customer_authenticated(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        customer_token = Token.objects.create(customer=customer).key
        self.client.credentials(Authorization=f"Bearer {customer_token}")
        route = reverse("api:customer", args=[customer.ulid])
        response = self.client.delete(route)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
        print_response(response, route)

    def test_send_link_for_delete_customer_when_requested_from_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        customer_token = Token.objects.create(customer=customer).key
        self.client.credentials(Authorization=f"Bearer {customer_token}")
        route = reverse("api:request_delete_customer", args=[customer.ulid])
        response = self.client.put(
            route,
            data={"origin": "https://localhost:8000"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_response(response, route)

    def test_send_link_for_delete_customer_when_requested_from_customer_with_invalid_token(
        self,
    ):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        customer_token = Token.objects.create(customer=customer).key
        self.client.credentials(Authorization=f"Bearer {customer_token}invalid")
        route = reverse("api:request_delete_customer", args=[customer.ulid])
        response = self.client.put(
            route,
            data={"origin": "https://localhost:8000"},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print_response(response, route)

    def test_delete_customer_when_requested_from_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        customer_token = Token.objects.create(customer=customer).key
        link = reverse("api:confirm_delete_customer", args=[customer_token])
        response = self.client.get(link)
        print_response(response, link)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_customer_when_requested_from_customer_with_invalid_token(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        customer_token = Token.objects.create(customer=customer).key
        link = reverse("api:confirm_delete_customer", args=[customer_token + "invalid"])
        response = self.client.get(link)
        print_response(response, link)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BusinessViewTests(TestCase):
    superuser = None
    admin_token = None

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username="admin", email="admin@gmail.com", password="admin"
        )
        cls.customer = Customer.objects.create(
            ulid=str(ULID()),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            middle_name=fake.first_name(),
            dob=fake.date_of_birth(),
            phone_number="+254" + fake.phone_number()[:9],
        )
        cls.admin_token = Token.objects.get_or_create(user=cls.superuser)[0]
        cls.business_category = BusinessCategory.objects.create(name="Test Category")

    def setUp(self):
        self.client = APIClient()

    def test_create_business(self):
        data = {
            "business_category": self.business_category.name,
            "business_name": fake.company(),
            "business_email": fake.email(),
            "business_phone": "+254" + fake.phone_number()[:9],
            "business_address": fake.address(),
            "business_website": fake.url(),
        }
        route = reverse("api:businesses")
        response = self.client.post(
            route,
            data=json.dumps(data),
            content_type="application/json",
        )
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Business.objects.count(), 1)
        self.assertEqual(Business.objects.all()[0].business_name, data["business_name"])

    def test_get_businesses(self):
        for _ in range(15):
            data = {
                "category_id": self.business_category.id,
                "business_name": fake.company(),
                "business_email": fake.email(),
                "business_phone": "+254" + fake.phone_number()[:9],
                "business_address": fake.address(),
                "business_website": fake.url(),
            }
            Business.objects.create(**data)
        route = reverse("api:businesses")
        response = self.client.get(route)
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_business(self):
        data = {
            "category_id": self.business_category.id,
            "business_name": fake.company(),
            "business_email": fake.email(),
            "business_phone": "+254" + fake.phone_number()[:9],
            "business_address": fake.address(),
            "business_website": fake.url(),
        }
        business = Business.objects.create(**data)
        self.client.credentials(Authorization=f"Bearer {self.admin_token}")
        route = reverse("api:business", args=[business.ulid])
        response = self.client.delete(route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Business.objects.count(), 0)
        print_response(response, route)

    def test_get_business_customers(self):
        data = {
            "category_id": self.business_category.id,
            "business_name": fake.company(),
            "business_email": fake.email(),
            "business_phone": "+254" + fake.phone_number()[:9],
            "business_address": fake.address(),
            "business_website": fake.url(),
        }
        business = Business.objects.create(**data)
        for _ in range(15):
            customer = Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                middle_name=fake.first_name(),
                dob=fake.date_of_birth(),
                phone_number="+254" + fake.phone_number()[:9],
                email=fake.email(),
            )
            business.customers.add(customer)

        route = reverse("api:business_customers", args=[business.ulid])
        response = self.client.get(route)
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["body"]), 15)

    def test_get_business_customers_with_invalid_business(self):
        route = reverse("api:business_customers", args=["invalid"])
        response = self.client.get(route)
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BusinessCategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_business_category(self):
        data = {"name": fake.word()}
        route = reverse("api:business_categories")
        response = self.client.post(
            route,
            data=json.dumps(data),
            content_type="application/json",
        )
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BusinessCategory.objects.count(), 1)
        self.assertEqual(BusinessCategory.objects.all()[0].name, data["name"])

    def test_get_business_categories(self):
        for _ in range(15):
            data = {"name": fake.word()}
            BusinessCategory.objects.create(**data)
        route = reverse("api:business_categories")
        response = self.client.get(route)
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["body"]), 15)


class CountyTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_county(self):
        data = {"name": fake.word()}
        route = reverse("api:counties")
        response = self.client.post(
            route,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(County.objects.count(), 1)
        self.assertEqual(County.objects.all()[0].name, data["name"])

    def test_get_counties(self):
        for _ in range(15):
            data = {"name": fake.word()}
            County.objects.create(**data)
        route = reverse("api:counties")
        response = self.client.get(route)
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["body"]), 15)


class SubCountyTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.county = County.objects.create(name=fake.word())

    def test_create_sub_county(self):
        data = {"name": fake.word()}
        route = reverse("api:subcounties", args=[self.county.name])
        response = self.client.post(
            route,
            data=json.dumps(data),
            content_type="application/json",
        )
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCounty.objects.count(), 1)
        self.assertEqual(SubCounty.objects.all()[0].name, data["name"])

    def test_get_sub_counties(self):
        for _ in range(15):
            data = {"name": fake.word(), "county_id": self.county.id}
            SubCounty.objects.create(**data)
        route = reverse("api:subcounties", args=[self.county.name])
        response = self.client.get(route)
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["body"]), 15)


class WardTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.county = County.objects.create(name=fake.word())
        self.sub_county = SubCounty.objects.create(name=fake.word(), county=self.county)

    def test_create_ward(self):
        data = {"name": fake.word(), "sub_county_id": self.sub_county.id}
        route = reverse("api:wards", args=[self.county.name, self.sub_county.name])
        response = self.client.post(
            route,
            data=json.dumps(data),
            content_type="application/json",
        )
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ward.objects.count(), 1)
        self.assertEqual(Ward.objects.all()[0].name, data["name"])

    def test_get_wards(self):
        for _ in range(15):
            data = {"name": fake.word(), "sub_county_id": self.sub_county.id}
            Ward.objects.create(**data)
        route = reverse("api:wards", args=[self.county.name, self.sub_county.name])
        response = self.client.get(route)
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["body"]), 15)


class AreaTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.county = County.objects.create(name=fake.word())
        self.sub_county = SubCounty.objects.create(name=fake.word(), county=self.county)
        self.ward = Ward.objects.create(name=fake.word(), sub_county=self.sub_county)

    def test_create_area(self):
        data = {
            "name": fake.word(),
        }

        route = reverse(
            "api:areas",
            args=[self.county.name, self.sub_county.name, self.ward.name],
        )
        response = self.client.post(
            route,
            data=json.dumps(data),
            content_type="application/json",
        )
        print_response(response, route)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Area.objects.count(), 1)
        self.assertEqual(Area.objects.all()[0].name, data["name"])

    def test_get_areas(self):
        for _ in range(15):
            data = {"name": fake.word(), "ward_id": self.ward.id}
            Area.objects.create(**data)

        route = reverse(
            "api:areas",
            args=[self.county.name, self.sub_county.name, self.ward.name],
        )
        response = self.client.get(route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["body"]), 15)
