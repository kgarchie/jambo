---
title: My Project
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# My Project

Base URLs:

# Authentication

- HTTP Authentication, scheme: bearer

# Default

## GET Status

GET /api/status

Get's the server status.

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

# Sample APIs

## GET Find pet by ID

GET /pet/{petId}

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|petId|path|string| yes |pet ID|

> Response Examples

> OK

```json
{
  "code": 0,
  "data": {
    "name": "Hello Kitty",
    "photoUrls": [
      "http://dummyimage.com/400x400"
    ],
    "id": 3,
    "category": {
      "id": 71,
      "name": "Cat"
    },
    "tags": [
      {
        "id": 22,
        "name": "Cat"
      }
    ],
    "status": "sold"
  }
}
```

> 400 Response

```json
{
  "code": 0,
  "message": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid input|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Record not found|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||status code|
|» data|[Pet](#schemapet)|true|none||pet details|
|»» id|integer(int64)|true|none||Pet ID|
|»» category|[Category](#schemacategory)|true|none||group|
|»»» id|integer(int64)|false|none||Category ID|
|»»» name|string|false|none||Category Name|
|»» name|string|true|none||name|
|»» photoUrls|[string]|true|none||image URL|
|»» tags|[[Tag](#schematag)]|true|none||tag|
|»»» id|integer(int64)|false|none||Tag ID|
|»»» name|string|false|none||Tag Name|
|»» status|string|true|none||Pet Sales Status|

#### Enum

|Name|Value|
|---|---|
|status|available|
|status|pending|
|status|sold|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|

HTTP Status Code **404**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|

## DELETE Deletes a pet

DELETE /pet/{petId}

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|petId|path|string| yes |Pet id to delete|
|api_key|header|string| no |none|

> Response Examples

> OK

```json
{
  "code": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|

## POST Add a new pet to the store

POST /pet

> Body Parameters

```yaml
name: Hello Kitty
status: sold

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |Pet Name|
|» status|body|string| yes |Pet Sales Status|

> Response Examples

> OK

```json
{
  "code": 0,
  "data": {
    "name": "Hello Kitty",
    "photoUrls": [
      "http://dummyimage.com/400x400"
    ],
    "id": 3,
    "category": {
      "id": 71,
      "name": "Cat"
    },
    "tags": [
      {
        "id": 22,
        "name": "Cat"
      }
    ],
    "status": "sold"
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|OK|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|[Pet](#schemapet)|true|none||pet details|
|»» id|integer(int64)|true|none||Pet ID|
|»» category|[Category](#schemacategory)|true|none||group|
|»»» id|integer(int64)|false|none||Category ID|
|»»» name|string|false|none||Category Name|
|»» name|string|true|none||name|
|»» photoUrls|[string]|true|none||image URL|
|»» tags|[[Tag](#schematag)]|true|none||tag|
|»»» id|integer(int64)|false|none||Tag ID|
|»»» name|string|false|none||Tag Name|
|»» status|string|true|none||Pet Sales Status|

#### Enum

|Name|Value|
|---|---|
|status|available|
|status|pending|
|status|sold|

## PUT Update an existing pet

PUT /pet

> Body Parameters

```json
{}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> OK

```json
{
  "code": 0,
  "data": {
    "name": "Hello Kitty",
    "photoUrls": [
      "http://dummyimage.com/400x400"
    ],
    "id": 3,
    "category": {
      "id": 71,
      "name": "Cat"
    },
    "tags": [
      {
        "id": 22,
        "name": "Cat"
      }
    ],
    "status": "sold"
  }
}
```

> 404 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Record not found|Inline|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Validation error|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|[Pet](#schemapet)|true|none||pet details|
|»» id|integer(int64)|true|none||Pet ID|
|»» category|[Category](#schemacategory)|true|none||group|
|»»» id|integer(int64)|false|none||Category ID|
|»»» name|string|false|none||Category Name|
|»» name|string|true|none||name|
|»» photoUrls|[string]|true|none||image URL|
|»» tags|[[Tag](#schematag)]|true|none||tag|
|»»» id|integer(int64)|false|none||Tag ID|
|»»» name|string|false|none||Tag Name|
|»» status|string|true|none||Pet Sales Status|

#### Enum

|Name|Value|
|---|---|
|status|available|
|status|pending|
|status|sold|

## GET Finds Pets by status

GET /pet/findByStatus

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|status|query|string| yes |Status values that need to be considered for filter|

> Response Examples

> OK

```json
{
  "code": 0,
  "data": [
    {
      "name": "Hello Kitty",
      "photoUrls": [
        "http://dummyimage.com/400x400"
      ],
      "id": 3,
      "category": {
        "id": 71,
        "name": "Cat"
      },
      "tags": [
        {
          "id": 22,
          "name": "Cat"
        }
      ],
      "status": "sold"
    },
    {
      "name": "White Dog",
      "photoUrls": [
        "http://dummyimage.com/400x400"
      ],
      "id": 3,
      "category": {
        "id": 71,
        "name": "Dog"
      },
      "tags": [
        {
          "id": 22,
          "name": "Dog"
        }
      ],
      "status": "sold"
    }
  ]
}
```

> 400 Response

```json
{
  "code": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid status value|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|*anonymous*|[[Pet](#schemapet)]|false|none||none|
|» id|integer(int64)|true|none||Pet ID|
|» category|[Category](#schemacategory)|true|none||group|
|»» id|integer(int64)|false|none||Category ID|
|»» name|string|false|none||Category Name|
|» name|string|true|none||name|
|» photoUrls|[string]|true|none||image URL|
|» tags|[[Tag](#schematag)]|true|none||tag|
|»» id|integer(int64)|false|none||Tag ID|
|»» name|string|false|none||Tag Name|
|» status|string|true|none||Pet Sales Status|

#### Enum

|Name|Value|
|---|---|
|status|available|
|status|pending|
|status|sold|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|

# Customers

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

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» first_name|body|string| yes |none|
|» last_name|body|string| yes |none|
|» email|body|string| yes |none|
|» nationality|body|string| yes |none|
|» dob|body|string| yes |none|
|» phone_number|body|string| yes |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## GET Get All Customers

GET /api/customers

An endpoint to retrieve all customers

> Body Parameters

```yaml
origin: postman

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» origin|body|string| no |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

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

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» first_name|body|string| yes |none|
|» last_name|body|string| yes |none|
|» email|body|string| yes |none|
|» nationality|body|string| yes |none|
|» dob|body|string| yes |none|
|» phone_number|body|string| yes |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## GET Get Customer

GET /api/customer/customer_ulid

An endpoint to the customer details.

**Note:**  
An auth token is needed. The auth token will be used to retrieve the customer, thus, a customer can only retrieve their details.

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## PUT Edit Customer (Staff)

PUT /api/customer/customer_ulid

An endpoint to edit the customer, this endpoint can only be used by Users with staff access. Auth bearer token is used to authenticate. The path includes the customer_ULID for who to edit.

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

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» first_name|body|string| yes |none|
|» last_name|body|string| yes |none|
|» email|body|string| yes |none|
|» nationality|body|string| yes |none|
|» dob|body|string| yes |none|
|» phone_number|body|string| yes |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## DELETE Delete Customer (Staff)

DELETE /api/customer/customer_ulid

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## POST Delete Customer (User) [User Request Delete]

POST /api/customer/customer_ulid/delete/request

In compiance to the data protection act 2019, users have to have a way of accessing and deleting their data. Thus I have provided the following two endpoints to facilitate that securely.

First a user will request for their data to be deleted, they will get a link to their email which will allow them to delete their account and data.

**Why the origin?**  
I did it this way because the server may have dynamic ports behind a proxy or sth. In hindsight I should have used an environment variable.

This origin is used to create the reset link, even if the frontend is running on a completely different server. There's more to be discussed and discovered here.

> Body Parameters

```yaml
origin: http://localhost:8000

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» origin|body|string| yes |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## GET Delete Customer (User) [User Confirm URL]

GET /api/customer/customer_token/delete/confirm

Refer to the above, they work in conjunction to delete user data.

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema