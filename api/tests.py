from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from ulid import ULID
from faker import Faker
from .models import Customer, Token
import json
from django.urls import reverse

# Create your tests here.
fake = Faker()


def print_response(response):
    print("-----------------------------------------------------------------------------------------------------------")
    print("=========================================================================================================\n")
    print(f"Status Code: {response.status_code}")
    print(f"Content Type: {response['content-type']}")
    print(json.dumps(response.data, indent=4))
    print("\n=========================================================================================================")
    print("-----------------------------------------------------------------------------------------------------------")


def create_fake_customer():
    return {
        "ulid": str(ULID()),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "middle_name": fake.first_name(),
        "dob": str(fake.date_of_birth()),
        "nationality": fake.country_code(representation="alpha-2"),
        "phone_number": "+254" + fake.phone_number()[:9],
        "email": fake.email()
    }


class CustomerViewTests(TestCase):
    superuser = None
    admin_token = None

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(username="admin", email="admin@test.com", password="asd9032km2sd")
        cls.admin_token = Token.objects.get_or_create(user=cls.superuser)[0]

    def setUp(self):
        self.client = APIClient()

    def test_create_customer(self):
        data = create_fake_customer()
        response = self.client.post(reverse('api:customers'), data=json.dumps(data), content_type='application/json')
        # print_response(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, data["first_name"])

    def test_get_customers(self):
        for _ in range(15):
            data = create_fake_customer()
            Customer.objects.create(**data)
        response = self.client.get(reverse('api:customers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print_response(response)

    def test_get_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        self.client.credentials(Authorization=f"Bearer {self.admin_token}")
        response = self.client.get(reverse('api:customer', args=[customer.ulid]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print_response(response)

    def test_update_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        new_data = create_fake_customer()
        self.client.credentials(Authorization=f"Bearer {self.admin_token}")
        response = self.client.put(reverse('api:customer', args=[customer.ulid]), data=json.dumps(new_data),
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print_response(response)

    def test_delete_customer_admin(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        self.client.credentials(Authorization=f"Bearer {self.admin_token}")
        response = self.client.delete(reverse('api:customer', args=[customer.ulid]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
        # print_response(response)

    def test_send_link_for_delete_customer_when_requested_from_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        customer_token = Token.objects.create(customer=customer).key
        self.client.credentials(Authorization=f"Bearer {customer_token}")
        response = self.client.put(reverse('api:request_delete_customer', args=[customer.ulid]), data={
            "origin": "https://localhost:8000"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print_response(response)

    def test_delete_customer_when_requested_from_customer(self):
        data = create_fake_customer()
        customer = Customer.objects.create(**data)
        customer_token = Token.objects.create(customer=customer).key
        link = reverse('api:confirm_delete_customer', args=[customer_token])
        response = self.client.get(link)
        # print_response(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)