# A POST request is commonly used to send data to a server.
# JSONPlaceholder provides a testing endpoint:

import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Learning Python APIs",
    "body": "Today I learned POST requests.",
    "userId": 1
}

response = requests.post(url, json=new_post)

print("Status:", response.status_code)
print("Response:", response.json())