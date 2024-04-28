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
{}
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
{}
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
{}
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
{}
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
{}
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
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema
