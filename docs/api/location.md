# Location

## GET Get All Nationalities

GET /api/nationalities

Returns a list of all nationalities and their shorcodes.

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

# Location/County

## POST Create Sub County

POST /api/counties

Add a county

> Body Parameters

```yaml
name: "{{county}}"

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
  "statusCode": 200,
  "body": {
    "id": 4,
    "name": "find"
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## GET Get All Counties

GET /api/counties

Get all counties

> Response Examples

> 200 Response

```json
{
  "statusCode": 200,
  "body": [
    {
      "id": 4,
      "name": "find"
    },
    {
      "id": 5,
      "name": "international"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

# Location/Subcounty

## POST Create Sub County For [CountyName]

POST /api/county/county/subcounties

Add a subcounty

**Note:**  
county_name is required, because subcounties are nested within. Thus in order to create a subcounty, a county needs to exist first.

**NB:** This pattern will repeat throughout till the lowest jurisdiction as the level of nesting increases.

county_name is case insensitive

> Body Parameters

```yaml
name: Nairobi

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |Case Insensitive|

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

## GET Get All Sub Counties For [CountyName]

GET /api/county/county/subcounties

Get's all cubcounties for a particular county

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

# Location/Ward

## POST Create Ward For [County]/county/[SubCounty]

POST /api/county/county/subcounty/subcounty/wards

Add a ward

:::
You need the county name

You still need the county name

(All are case insensitive)
:::

> Body Parameters

```yaml
name: "{{ward}}"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |Case Insensitive|

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

## GET Get All Wards For [County]/subcounty/[SubCounty]

GET /api/county/county/subcounty/subcounty/wards

Get all wards for a particulare subcounty.

**Note:**

You need the sub_county name

You still need the county name

(All are case insensitive)

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

# Location/Area (Locale)

## POST Create Area For [County]/subcounty/[SubCounty]/ward/[Ward]

POST /api/county/county/subcounty/subcounty/ward/ward/areas

**Add a ward to a particular subcounty**

**Note:**

You need the county name

You still need the sub_county name

And of course the ward_name

(All are case insensitive)

> Body Parameters

```yaml
name: "{{area}}"

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
        "name": "citizen",
        "ward_name": "deal"
    }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|

### Responses Data Schema

## GET Get All Areas For [County]/subcounty/[SubCounty]/ward/[Ward]

GET /api/county/county/subcounty/subcounty/ward/ward/areas

Get the areas for a ward

**Note:**

You need the county name

You still need the sub_county name

And of course the ward_name

(All are case insensitive)

> Response Examples

> 200 Response

```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "citizen",
            "ward_name": "deal"
        }
    ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
