# Sometimes an API lets you filter results using query parameters.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)
posts = response.json()

for post in posts:
    print(post["title"])