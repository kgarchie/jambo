# Examples
## URL: /api/county/he/subcounty/create/ward/deal/areas
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "citizen",
        "ward_name": "deal"
    }
}
```


## URL: /api/business_categories
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "heavy"
    }
}
```

## URL: /api/business_categories
>Status Code: 200
>Content Type: application/json
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
        },
        {
            "name": "discussion"
        },
        {
            "name": "expert"
        },
        {
            "name": "this"
        },
        {
            "name": "best"
        },
        {
            "name": "wide"
        },
        {
            "name": "administration"
        },
        {
            "name": "north"
        }
    ]
}
```

## URL: /api/businesses
>Status Code: 201
>Content Type: application/json
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

## URL: /api/business/01HWJ8WG71S779RBWHCWM5NAMP
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 204,
    "body": "Business deleted successfully"
}
```

## URL: /api/business/01HWJ8WG7E2Y4N0KHRTAVP78VF/customers/
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "ulid": "01HWJ8WG864GESR1XX7VNPCKQN",
            "first_name": "David",
            "last_name": "Burnett",
            "middle_name": "Stephanie",
            "nationality": "",
            "dob": "1981-11-05",
            "email": "jacobdavis@example.net",
            "phone_number": "254788.880.3"
        },
        {
            "ulid": "01HWJ8WG8BKW0DKZZ38ZA924C3",
            "first_name": "Marvin",
            "last_name": "Mclean",
            "middle_name": "Rachel",
            "nationality": "",
            "dob": "2024-03-20",
            "email": "rodriguezkathleen@example.net",
            "phone_number": "254+1-288-62"
        },
        {
            "ulid": "01HWJ8WG8FNBH5R27D77Q3SQEW",
            "first_name": "Sheila",
            "last_name": "Davis",
            "middle_name": "Lauren",
            "nationality": "",
            "dob": "1922-11-18",
            "email": "brad20@example.net",
            "phone_number": "254+1-866-45"
        },
        {
            "ulid": "01HWJ8WG8HPTHEXC3WJWKSGHWS",
            "first_name": "Michael",
            "last_name": "Blake",
            "middle_name": "David",
            "nationality": "",
            "dob": "1925-07-01",
            "email": "mercedes47@example.com",
            "phone_number": "254001-586-3"
        }
    ]
}
```

## URL: /api/business/invalid/customers/
>Status Code: 404
>Content Type: application/json
```json
{
    "detail": "No Business matches the given query."
}
```

## URL: /api/businesses
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "business_name": "Payne, Jimenez and Petty",
            "created_at": "2024-04-28T11:54:13.693678Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "kayleerodriguez@example.com",
            "business_website": "http://www.taylor.org/",
            "business_address": "970 Zachary Vista Suite 152\nCarolynside, MP 51943",
            "business_phone": "+254(567)367-"
        },
        {
            "business_name": "Smith Ltd",
            "created_at": "2024-04-28T11:54:13.695681Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "megantaylor@example.org",
            "business_website": "https://hernandez.org/",
            "business_address": "826 Rivera Loop\nSouth Carol, MO 38889",
            "business_phone": "+254887.763.5"
        },
        {
            "business_name": "Stein, Lopez and Neal",
            "created_at": "2024-04-28T11:54:13.698683Z",
            "business_category": "Test Category",
            "business_age": 0,
            "business_email": "william05@example.com",
            "business_website": "https://www.ramirez.com/",
            "business_address": "967 Campbell Crest\nMillerbury, NM 25900",
            "business_phone": "+254+1-951-39"
        },
    ]
}
```

## URL: /api/counties
>Status Code: 200
>Content Type: application/json
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
        },
        {
            "id": 6,
            "name": "firm"
        }
    ]
}
```

## URL: /api/customers
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "ulid": "01HWJ8WH8998JFA9A7T1CFKQJN",
        "first_name": "Christina",
        "last_name": "Rodriguez",
        "middle_name": "Andrew",
        "nationality": "El Salvador",
        "dob": "1977-07-06",
        "email": "patrickrobertson@example.org",
        "phone_number": "254260-960-9"
    }
}
```

## URL: /api/customer/01HWJ8WH8ZT7ATH54B2FCYAJ5A
>Status Code: 204
>Content Type: application/json
```json
{
    "statusCode": 204
}
```

## URL: /api/customer/01HWJ8WH9X8WBK65EMGY9YKPBS
>Status Code: 200
>Content Type: application/json
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

## URL: /api/customers
>Status Code: 200
>Content Type: application/json
```json
{
    "count": 15,
    "next": null,
    "previous": null,
    "results": {
        "statusCode": 200,[
            {
                "ulid": "01HWJ8WHBKAVVYTH97J7BMWK6Z",
                "first_name": "Vanessa",
                "last_name": "Jenkins",
                "middle_name": "Karen",
                "nationality": "Ireland",
                "dob": "2014-08-19",
                "email": "huntjohn@example.com",
                "phone_number": "254374372730"
            },
            {
                "ulid": "01HWJ8WHBN260KG7XHYC53Y9DN",
                "first_name": "Andrea",
                "last_name": "Anderson",
                "middle_name": "Kenneth",
                "nationality": "Bahrain",
                "dob": "1971-08-07",
                "email": "campbelltimothy@example.net",
                "phone_number": "254001-875-6"
            },
            {
                "ulid": "01HWJ8WHBPZQ1XG6HZ5K31M4S9",
                "first_name": "Ryan",
                "last_name": "Martin",
                "middle_name": "James",
                "nationality": "Nicaragua",
                "dob": "1928-10-28",
                "email": "mckeeandrea@example.org",
                "phone_number": "254(640)335-"
            },
        ]
    }
}
```

## URL: /api/customer/01HWJ8WHCR763WXRX6G1YHBQ3T
>Status Code: 200
>Content Type: application/json
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

## URL: /api/county/term/subcounties
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "and",
        "county_name": "term"
    }
}
```

## URL: /api/county/into/subcounties
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "anyone",
            "county_name": "into"
        },
        {
            "name": "only",
            "county_name": "into"
        },
        {
            "name": "short",
            "county_name": "into"
        },
        {
            "name": "drug",
            "county_name": "into"
        },
        {
            "name": "industry",
            "county_name": "into"
        },
        {
            "name": "mean",
            "county_name": "into"
        }
    ]
}
```

## URL: /api/county/measure/subcounty/building/wards
>Status Code: 201
>Content Type: application/json
```json
{
    "statusCode": 201,
    "body": {
        "name": "easy",
        "sub_county_name": "building"
    }
}
```

## URL: /api/county/everything/subcounty/tend/wards
>Status Code: 200
>Content Type: application/json
```json
{
    "statusCode": 200,
    "body": [
        {
            "name": "finally",
            "sub_county_name": "tend"
        },
        {
            "name": "boy",
            "sub_county_name": "tend"
        },
        {
            "name": "light",
            "sub_county_name": "tend"
        },
        {
            "name": "paper",
            "sub_county_name": "tend"
        }
    ]
}
```
