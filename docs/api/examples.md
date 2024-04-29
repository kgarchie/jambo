# Examples

## POST - /api/customers
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "ulid": "01HWMHCAP5M05KNF4TDMKK8VW0",
        "first_name": "Alfred",
        "last_name": "Haas",
        "middle_name": "Paul",
        "nationality": "Chad",
        "dob": "1943-11-29",
        "email": "hallcrystal@example.com",
        "phone_number": "254+1-496-42"
    }
}
```

## DELETE - /api/customer/01HWMHCAQJTT4KNRTPANS37TT7
>Status Code: 204
>Content Type: application/json
```json
{
    "statusCode": 204
}
```

## GET - /api/customer/98009c1b28410ef3311b76299f19c6f5cd7cb040/delete/confirm
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": "Customer deleted successfully"
}
```

## GET - /api/customer/17f49567a67ec439c625ca3479c10923130dc174invalid/delete/confirm
>Status Code: 404
>Content Type: application/json
```json
{
    "detail": "No Token matches the given query."
}
```

## DELETE - /api/customer/01HWMHCARGSB3MMXBNF3BF460G
>Status Code: 204
>Content Type: application/json
```json
{
    "statusCode": 204
}
```

## GET - /api/customer/01HWMHCARWBTABKQ7MZ8WAE0PT
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": {
        "ulid": "01HWMHCARWBTABKQ7MZ8WAE0PT",
        "first_name": "Amy",
        "last_name": "Harding",
        "middle_name": "Nicholas",
        "nationality": "Holy See",
        "dob": "1967-10-09",
        "email": "gary38@example.com",
        "phone_number": "254+1-820-97"
    }
}
```

## GET - /api/customers
>Status Code: 200
>Content Type: application/json
```json
{
    "count": 15,
    "next": null,
    "previous": null,
    "results": {
        "statusCode": 200,
        "body": [
            {
                "ulid": "01HWMHCASJSAB6S9910F16VMFD",
                "first_name": "Jennifer",
                "last_name": "Burns",
                "middle_name": "John",
                "nationality": "Taiwan",
                "dob": "2020-01-26",
                "email": "paul24@example.org",
                "phone_number": "254943.724.5"
            },
            {
                "ulid": "01HWMHCASM0Q1P341P04Q6M68Z",
                "first_name": "Brett",
                "last_name": "Smith",
                "middle_name": "James",
                "nationality": "Mauritania",
                "dob": "1975-02-24",
                "email": "schaefersteven@example.com",
                "phone_number": "254412898975"
            },
            {
                "ulid": "01HWMHCASPFE9MS8W2B1NJSDB6",
                "first_name": "Leslie",
                "last_name": "Kennedy",
                "middle_name": "Frank",
                "nationality": "Denmark",
                "dob": "2006-10-20",
                "email": "kyates@example.org",
                "phone_number": "254733-569-4"
            }
        ]
    }
}
```

## POST (PUT) - /api/customer/01HWMHCAV2F9WMTCA78YV2JJSV/delete/request
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": "Data deletion link sent successfully"
}
```

## POST (PUT) - /api/customer/01HWMHCBP7YZWM9EJ5M9T9HVFM/delete/request
>Status Code: 400
>Content Type: application/json
```json
{
    "statusCode": 400,
    "body": "Customer Not Found or is Invalid"
}
```

## PUT - /api/customer/01HWMHCBPJGTGZBCPAXQ4GK0P6
>Status Code: 200
>Content Type: application/json
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

## POST - /api/businesses
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "business_name": "Fowler Inc",
        "created_at": "2024-04-29T09:01:11.876006Z",
        "business_category": "Test Category",
        "business_age": 0,
        "business_email": "seancolon@example.org",
        "business_website": "https://huffman.org/",
        "business_address": "8313 Barbara Bypass\nEast Michaelburgh, MP 53306",
        "business_phone": "+254552446065"
    }
}
```

## DELETE - /api/business/01HWMHCCTRJEB2GDA5H8ZX69VM
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 204,
    "body": "Business deleted successfully"
}
```

## GET - /api/business/01HWMHCCV5S790A13076G4G1Z3/customers/
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "ulid": "01HWMHCCV6F1NJPXYNA6KP57F0",
            "first_name": "Beth",
            "last_name": "Lloyd",
            "middle_name": "Jenny",
            "nationality": "",
            "dob": "1960-01-04",
            "email": "ibond@example.org",
            "phone_number": "254+1-732-39"
        },
        {
            "ulid": "01HWMHCCVAJ6ZZ2EQGA0KW2WQD",
            "first_name": "Yvonne",
            "last_name": "Obrien",
            "middle_name": "Stephanie",
            "nationality": "",
            "dob": "1963-07-20",
            "email": "coxbrenda@example.net",
            "phone_number": "254(666)866-"
        },
        {
            "ulid": "01HWMHCCVCMB5KE7KB50126J80",
            "first_name": "Edwin",
            "last_name": "Bennett",
            "middle_name": "Travis",
            "nationality": "",
            "dob": "2021-10-05",
            "email": "robinfarrell@example.org",
            "phone_number": "254001-299-6"
        }
    ]
}
```

## GET - /api/business/invalid/customers/
>Status Code: 404
>Content Type: application/json
```json
{
    "detail": "No Business matches the given query."
}
```

## GET - /api/businesses
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "business_name": "Wilson-Collins",
            "created_at": "2024-04-29T09:01:11.980471Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "pollardleslie@example.org",
            "business_website": "https://www.peterson.net/",
            "business_address": "130 Brown Brook\nWilsonhaven, MI 52842",
            "business_phone": "+254353.408.2"
        },
        {
            "business_name": "Pruitt Inc",
            "created_at": "2024-04-29T09:01:11.981996Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "kimberlyblake@example.com",
            "business_website": "http://www.ali.com/",
            "business_address": "489 Valencia Road Apt. 941\nKellyshire, DC 92730",
            "business_phone": "+254891795260"
        },
        {
            "business_name": "Forbes, Robbins and Moore",
            "created_at": "2024-04-29T09:01:11.983187Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "rogersgerald@example.com",
            "business_website": "http://sutton.com/",
            "business_address": "301 Foster Brooks Suite 605\nNorth Susan, KY 04155",
            "business_phone": "+254(561)670-"
        }
    ]
}
```

## POST - /api/business_categories
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "character"
    }
}
```

## GET - /api/business_categories
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "various"
        },
        {
            "name": "experience"
        },
        {
            "name": "edge"
        }
    ]
}
```

## POST - /api/counties
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "id": 1,
        "name": "future"
    }
}
```

## GET - /api/counties
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "id": 2,
            "name": "partner"
        },
        {
            "id": 3,
            "name": "only"
        },
        {
            "id": 4,
            "name": "back"
        }
    ]
}
```

## POST - /api/county/prevent/subcounties
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "sing",
        "county_name": "prevent"
    }
}
```

## GET - /api/county/turn/subcounties
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "fall",
            "county_name": "turn"
        },
        {
            "name": "represent",
            "county_name": "turn"
        },
        {
            "name": "throw",
            "county_name": "turn"
        }
    ]
}
```

## POST - /api/county/back/subcounty/whole/wards
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "say",
        "sub_county_name": "whole"
    }
}
```

## GET - /api/county/door/subcounty/leg/wards
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "sell",
            "sub_county_name": "leg"
        },
        {
            "name": "what",
            "sub_county_name": "leg"
        },
        {
            "name": "member",
            "sub_county_name": "leg"
        }
    ]
}
```

## POST - /api/county/already/subcounty/painting/ward/across/areas
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "oil",
        "ward_name": "across"
    }
}
```
political big federal

## GET - /api/county/political/subcounty/big/ward/federal/areas
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "government",
            "ward_name": "federal"
        },
        {
            "name": "sport",
            "ward_name": "federal"
        },
        {
            "name": "entire",
            "ward_name": "federal"
        }
    ]
}
```
