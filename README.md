# URL Shortner

Live app on heroku : \
base_url: https://sandeep-urlshortner.herokuapp.com/


## Create short_code for long URL

#### [POST] <base_url>/urls/
##### request body
{\
"url" : "https://google.com"\
}
##### response body
[200]
{\
"url": "https://google.com",\
"short_code": "0",\
"created_at": "2021-12-05T19:45:37.639376Z",\
"updated_at": "2021-12-05T19:45:37.639323Z",\
"count": 0,\
"hourly_hits": 0\
}\
[400]\
{\
"message": "Invalid url"\
}

## Get details of any short code

#### [GET] <base_url>/urls/<short_code>
##### response body
[200]\
{\
"url": "https://google.com",\
"short_code": "0",\
"created_at": "2021-12-05T19:45:37.639376Z",\
"updated_at": "2021-12-05T19:45:37.639323Z",\
"count": 5,\
"hourly_hits": 3\
}\
[400]\
{\
"message": "Something went wrong"\
}


## Redirect to URL

#### [GET] <base_url>/<short_code>
It should redirect to the original url

## Search all the Urls for given keyword
#### [GET] <base_url>/urls/search/?keyword=<search_key>
This API will return list of urls which contains the given keyword

##### response body
[200]\
[\
{\
"url": "https://google.com",\
"short_code": "0",\
"created_at": "2021-12-05T19:45:37.639376Z",\
"updated_at": "2021-12-05T19:45:37.639323Z",\
"count": 1,\
"hourly_hits": 1\
},\
{\
"url": "https://googlefacebook.com",\
"short_code": "2",\
"created_at": "2021-12-05T20:07:33.604457Z",\
"updated_at": "2021-12-05T20:07:33.604395Z",\
"count": 0,\
"hourly_hits": 0\
}\
]
