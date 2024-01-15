# Tests

import requests

# URL = 'http://localhost:8000/api/reviews'
# # URL = 'http://localhost:8000/api/reviews?page=6&limit=2'
# HEADERS = {'accept': 'application/json'}
# QUERYSET = {'page': 1, 'limit': 2}

# # GET
# response = requests.get(URL, headers=HEADERS, params=QUERYSET)

# if response.status_code == 200:
#     print("Status code: 200")
#     # print(response.content)
#     print(response.headers)

#     if response.headers.get('content-type') == 'application/json':
#         reviews = response.json()
#         for review in reviews:
#             print(f'score: {review["score"]} - {review["review"]}')


# POST
# URL = 'http://localhost:8000/api/reviews'

# REVIEW = {
#     'score': 5,
#     'review': 'This is a test review',
#     'user_id': 1,
#     'movie_id': 1
# }

# respones = requests.post(URL, json=REVIEW)


# if respones.status_code == 200:
#     print("Status code: 200")

# else: 
#     print("Status code: 404")

# # PUT 

# REVIEW_ID = 1

# REVIEW = {
#     'score': 5,
#     'review': 'This is a test review',
#     'user_id': 1,
#     'movie_id': 1
# }

# URL = f'http://localhost:8000/api/reviews/{REVIEW_ID}'

# respones = requests.put(URL, json=REVIEW)


# if respones.status_code == 200:
#     print("Status code: 200")

# else:
#     print("Status code: 404")

# Cookies

URL = 'http://localhost:8000/api/users/'

USERS = {
  'username': "user2",
  "password": "password"
}

response = requests.post(URL + "login", json=USERS)

if response.status_code == 200:
  print("User logged in successfully")
  print("Status code: 200")

  print(response.json())

  # Obtenemos el valor de la cookie
  # print(response.cookies.get_dict()) # Convertimos las cookies en un diccionario

  user_id = response.cookies.get_dict()["user_id"]

  cookies = { "user_id": user_id }
  response = requests.get(URL + "reviews", cookies=cookies)

  if response.status_code == 200:
    print("Status code: 200")

    print(response.json())
