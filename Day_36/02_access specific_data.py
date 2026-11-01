# Access specific data from an API
# The response.json() method returns Python data. You can access it like a dictionary

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
post = response.json()

print("User ID:", post["userId"])
print("Post ID:", post["id"])
print("Title:", post["title"])
print("Body:", post["body"])