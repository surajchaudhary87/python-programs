# An API request can fail because of network problems, an invalid URL, or a server error.

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    post = response.json()
    print("Title:", post["title"])

except requests.exceptions.Timeout:
    print("The request timed out.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

except ValueError:
    print("The response was not valid JSON.")