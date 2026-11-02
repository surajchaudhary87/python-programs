# You can also request a collection of records.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
posts = response.json()

for post in posts[:5]:
    print("ID:", post["id"])
    print("Title:", post["title"])
    print("-" * 30)