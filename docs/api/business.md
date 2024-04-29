# Business

## POST Create Business

POST /api/businesses

Creation of a business, business name should match one in the existing business categories. Case insensitive of course.

> Body Parameters

```yaml
business_name: Test Business
business_category: test
business_phone: string
business_email: string
business_address: string
business_website: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» business_name|body|string| yes |none|
|» business_category|body|string| yes |Case Insensitive|
|» business_phone|body|string| yes |none|
|» business_email|body|string| yes |none|
|» business_address|body|string| yes |none|
|» business_website|body|string| yes |none|

> Response Examples

> 200 Response

```json
{
    "statusCode": 201,
    "body": {
        "business_name": "Morris, Gonzalez and Patterson",
        "created_at": "2024-04-28T11:54:13.592688Z",
        "business_category": "Test Category",
        "business_age": 0,
        "business_email": "shermanmaria@example.org",
        "business_website": "http://www.mejia.org/",
        "business_address": "60031 White Dale\nSouth Lisaberg, OK 03668",
        "business_phone": "+254803.952.4"
    }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## GET Get All Businesses

GET /api/businesses

Endpoint to get all businesses

> Response Examples

> 200 Response

```json
{
    "statusCode": 200,
    "body": [
        {
            "business_name": "Williams, Simmons and Lewis",
            "created_at": "2024-04-28T11:54:13.678721Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "karenrivera@example.net",
            "business_website": "https://hahn.com/",
            "business_address": "977 Gregory Union\nNorth Ryanton, NM 87743",
            "business_phone": "+254001-540-5"
        },
        {
            "business_name": "Gordon, Friedman and King",
            "created_at": "2024-04-28T11:54:13.680686Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "psimmons@example.org",
            "business_website": "http://www.carter.com/",
            "business_address": "19474 Briana Courts Suite 988\nPatriciafurt, MI 72587",
            "business_phone": "+254+1-765-71"
        },
        {
            "business_name": "Gordon Ltd",
            "created_at": "2024-04-28T11:54:13.681680Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "joannestevens@example.com",
            "business_website": "http://www.wolfe.com/",
            "business_address": "740 Smith Viaduct Suite 222\nNorth Joshuaton, DE 57008",
            "business_phone": "+254752.698.5"
        }
    ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## PUT Update Business (Staff)

PUT /api/business/business_ilid

Endpoint to retrieve a particular business. Only staff users are able to

> Body Parameters

```yaml
business_name: Test Business
business_category: test
business_phone: " 0712345678"
business_email: " business@gmail.com"
business_address: " Office Park"
business_website: " hello@eng.com"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» business_name|body|string| yes |none|
|» business_category|body|string| yes |none|
|» business_phone|body|string| yes |none|
|» business_email|body|string| yes |none|
|» business_address|body|string| yes |none|
|» business_website|body|string| yes |none|

> Response Examples

> 200 Response

```json
{
    "statusCode": 200,
    "body": {
        "ulid": "01HWMHCBPMKDWD47WXFZRR6V5R",
        "first_name": "Mark",
        "last_name": "Lewis",
        "middle_name": "Shelly",
        "nationality": "Andorra",
        "dob": "1920-06-11",
        "email": "barberangela@example.com",
        "phone_number": "254(763)238-"
    }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## DELETE Delete Business (Staff)

DELETE /api/business/business_ilid

End point to delete a business, only staff users are able to

> Response Examples

> 200 Response

```json
{
    "statusCode": 204,
    "body": "Business deleted successfully"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

# Business/Category

## POST Add Business Category

POST /api/business_categories

Add a business category to the database

> Body Parameters

```yaml
name: Test

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |none|

> Response Examples

> 200 Response

```json
{
    "statusCode": 201,
    "body": {
        "name": "Test"
    }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## GET Get Business Categories

GET /api/business_categories

Get all the business categories

> Response Examples

> 200 Response

```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "seat"
        },
        {
            "name": "pretty"
        },
        {
            "name": "ready"
        },
        {
            "name": "west"
        },
        {
            "name": "mouth"
        },
        {
            "name": "suggest"
        },
        {
            "name": "federal"
        },
        {
            "name": "assume"
        }
    ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema
