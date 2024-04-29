---
title: Jambo
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: [ ]
includes: [ ]
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# Project

Base URLs:
> http:localhost:8000

# Customers

## Authentication

- HTTP Authentication, scheme:

> Authorization: "Bearer TOKEN"

## POST Add Customer

POST /api/customers

A POST endpoint to add customers

> Body Parameters

```yaml
first_name: "{{customer_first_name}}"
last_name: "{{customer_last_name}}"
email: "{{cusromer_email}}"
nationality: "{{customer_nationality}}"
dob: "{{customer_dob}}"
phone_number: "{{customer_phone}}"

```

### Params

| Name           | Location | Type   | Required | Description |
|----------------|----------|--------|----------|-------------|
| body           | body     | object | no       | none        |
| » first_name   | body     | string | yes      | none        |
| » last_name    | body     | string | yes      | none        |
| » email        | body     | string | yes      | none        |
| » nationality  | body     | string | yes      | none        |
| » dob          | body     | string | yes      | none        |
| » phone_number | body     | string | yes      | none        |

> Response Examples

> 200 Response

```json
{
  "statusCode": 201,
  "body": {
    "ulid": "01HWJ8WH9X8WBK65EMGY9YKPBS",
    "first_name": "Cynthia",
    "last_name": "Norris",
    "middle_name": "Alexander",
    "nationality": "Lesotho",
    "dob": "1912-09-06",
    "email": "aaron97@example.org",
    "phone_number": "254246515866"
  }
}
```

### Responses

| HTTP Status Code | Meaning                                        | Description | Data schema |
|------------------|------------------------------------------------|-------------|-------------|
| 201              | [Created](https://tools.ietf.org/html/rfc7231) | Success     | Inline      |

### Responses Data Schema

## GET Get All Customers

GET /api/customers

An endpoint to retrieve all customers

> Body Parameters

```yaml
origin: postman

```

### Params

| Name     | Location | Type   | Required | Description |
|----------|----------|--------|----------|-------------|
| body     | body     | object | no       | none        |
| » origin | body     | string | no       | none        |

> Response Examples

> 200 Response

```json
{
  "count": 15,
  "next": null,
  "previous": null,
  "results": {
    "statusCode": 200,
    "body": [
      {
        "ulid": "01HWJ8WHAN25NEA2SVCMRX6P6B",
        "first_name": "Tricia",
        "last_name": "Ryan",
        "middle_name": "Karen",
        "nationality": "Kyrgyzstan",
        "dob": "1913-02-03",
        "email": "emilygutierrez@example.net",
        "phone_number": "254001-327-9"
      },
      {
        "ulid": "01HWJ8WHAQZB914NFZ4JT7HFY0",
        "first_name": "Danielle",
        "last_name": "Compton",
        "middle_name": "Bill",
        "nationality": "Liberia",
        "dob": "1999-08-26",
        "email": "stewartmercedes@example.com",
        "phone_number": "254+1-406-90"
      }
    ]
  }
}
```

### Responses

| HTTP Status Code | Meaning                                                 | Description | Data schema |
|------------------|---------------------------------------------------------|-------------|-------------|
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success     | Inline      |

### Responses Data Schema

## PUT Edit Customer (User)

PUT /api/customers

Used to edit the user, uses bearer token to identify and validate who the user is.

> Body Parameters

```yaml
first_name: "{{customer_first_name}}"
last_name: Akama
email: "{{cusromer_email}}"
nationality: "{{customer_nationality}}"
dob: "{{customer_dob}}"
phone_number: "{{customer_phone}}"

```

### Params

| Name           | Location | Type   | Required | Description |
|----------------|----------|--------|----------|-------------|
| body           | body     | object | no       | none        |
| » first_name   | body     | string | yes      | none        |
| » last_name    | body     | string | yes      | none        |
| » email        | body     | string | yes      | none        |
| » nationality  | body     | string | yes      | none        |
| » dob          | body     | string | yes      | none        |
| » phone_number | body     | string | yes      | none        |

> Response Examples

> 200 Response

```json
{
  "statusCode": 200,
  "body": {
    "ulid": "01HWJ8WHCTKBSTNM65KCVT0KGQ",
    "first_name": "Joseph",
    "last_name": "Bauer",
    "middle_name": "Lori",
    "nationality": "Montenegro",
    "dob": "1989-05-10",
    "email": "edixon@example.org",
    "phone_number": "254(483)255-"
  }
}
```

### Responses

| HTTP Status Code | Meaning                                                 | Description | Data schema |
|------------------|---------------------------------------------------------|-------------|-------------|
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success     | Inline      |

### Responses Data Schema

## GET Get Customer

GET /api/customer/customer_ulid

An endpoint to the customer details.

**Note:**  
An auth token is needed. The auth token will be used to retrieve the customer, thus, a customer can only retrieve their
details.

> Response Examples

> 200 Response

```json
{
  "statusCode": 200,
  "body": {
    "ulid": "01HWJ8WH9X8WBK65EMGY9YKPBS",
    "first_name": "Cynthia",
    "last_name": "Norris",
    "middle_name": "Alexander",
    "nationality": "Lesotho",
    "dob": "1912-09-06",
    "email": "aaron97@example.org",
    "phone_number": "254246515866"
  }
}
```

### Responses

| HTTP Status Code | Meaning                                                      | Description | Data schema |
|------------------|--------------------------------------------------------------|-------------|-------------|
| 200              | [Created](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success     | Inline      |

### Responses Data Schema

## PUT Edit Customer (Staff)

PUT /api/customer/customer_ulid

An endpoint to edit the customer, this endpoint can only be used by Users with staff access. Auth bearer token is used
to authenticate. The path includes the customer_ULID for who to edit.

> Body Parameters

```yaml
first_name: "{{customer_first_name}}"
last_name: Akama
email: "{{cusromer_email}}"
nationality: "{{customer_nationality}}"
dob: "{{customer_dob}}"
phone_number: "{{customer_phone}}"

```

### Params

| Name           | Location | Type   | Required | Description |
|----------------|----------|--------|----------|-------------|
| body           | body     | object | no       | none        |
| » first_name   | body     | string | yes      | none        |
| » last_name    | body     | string | yes      | none        |
| » email        | body     | string | yes      | none        |
| » nationality  | body     | string | yes      | none        |
| » dob          | body     | string | yes      | none        |
| » phone_number | body     | string | yes      | none        |

> Response Examples

> 200 Response

```json
{
  "statusCode": 200,
  "body": {
    "ulid": "01HWJ8WH9X8WBK65EMGY9YKPBS",
    "first_name": "Cynthia",
    "last_name": "Norris",
    "middle_name": "Alexander",
    "nationality": "Lesotho",
    "dob": "1912-09-06",
    "email": "aaron97@example.org",
    "phone_number": "254246515866"
  }
}
```

### Responses

| HTTP Status Code | Meaning                                           | Description | Data schema |
|------------------|---------------------------------------------------|-------------|-------------|
| 204              | [No Content](https://tools.ietf.org/html/rfc7231) | Success     | Inline      |

### Responses Data Schema

## DELETE Delete Customer (Staff)

DELETE /api/customer/customer_ulid

> Response Examples

> 200 Response

```json
{
  "statusCode": 204
}
```

### Responses

| HTTP Status Code | Meaning                                                 | Description | Data schema |
|------------------|---------------------------------------------------------|-------------|-------------|
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success     | Inline      |

### Responses Data Schema

## POST Delete Customer (User) [User Request Delete]

POST /api/customer/customer_ulid/delete/request

In compiance to the data protection act 2019, users have to have a way of accessing and deleting their data. Thus, I have
provided the following two endpoints to facilitate that securely.

First a user will request for their data to be deleted, they will get a link to their email which will allow them to
delete their account and data.

**Why the origin?**  
I did it this way because the server may have dynamic ports behind a proxy or sth. In hindsight, I should have used an
environment variable.

This origin is used to create the reset link, even if the frontend is running on a completely different server. There's
more to be discussed and discovered here.

> Body Parameters

```yaml
origin: http://localhost:8000

```

### Params

| Name     | Location | Type   | Required | Description |
|----------|----------|--------|----------|-------------|
| body     | body     | object | no       | none        |
| » origin | body     | string | yes      | none        |

> Response Examples

> 200 Response

```json
{
    "statusCode": 200,
    "body": "Data deletion link sent successfully"
}
```

> 400 Response
```json
{
    "statusCode": 400,
    "body": "Customer Not Found or is Invalid"
}
```

### Responses

| HTTP Status Code | Meaning                                                 | Description | Data schema |
|------------------|---------------------------------------------------------|-------------|-------------|
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success     | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231)      | Bad Request |             |

### Responses Data Schema

## GET Delete Customer (User) [User Confirm URL]

GET /api/customer/customer_token/delete/confirm

Refer to the above, they work in conjunction to delete user data.

> Response Examples

> 200 Response

```json
{
    "statusCode": 200,
    "body": "Customer deleted successfully"
}
```
> 404 Response
```json
{
  "detail": "No Token matches the given query."
}
```
### Responses

| HTTP Status Code | Meaning                                                 | Description | Data schema |
|------------------|---------------------------------------------------------|-------------|-------------|
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success     | Inline      |
| 404              | Not Found                                               | Not Found   |             |

### Responses Data Schema