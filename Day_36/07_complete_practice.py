
"""
Working with APIs in Python

Topics:
1. GET request
2. HTTP status codes
3. Reading JSON responses
4. Query parameters
5. Error handling
6. POST request
"""

import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_single_post():
    """Fetch one post from the API."""
    url = f"{BASE_URL}/posts/1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        post = response.json()

        print("\n--- Single Post ---")
        print("User ID:", post["userId"])
        print("Post ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except ValueError:
        print("Invalid JSON response.")


def get_multiple_posts():
    """Fetch the first five posts."""
    url = f"{BASE_URL}/posts"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        posts = response.json()

        print("\n--- First Five Posts ---")

        for post in posts[:5]:
            print("ID:", post["id"])
            print("Title:", post["title"])
            print("-" * 30)

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except ValueError:
        print("Invalid JSON response.")


def get_user_posts(user_id):
    """Fetch posts belonging to a particular user."""
    url = f"{BASE_URL}/posts"

    try:
        response = requests.get(
            url,
            params={"userId": user_id},
            timeout=10
        )
        response.raise_for_status()

        posts = response.json()

        print(f"\n--- Posts by User {user_id} ---")

        for post in posts:
            print(post["title"])

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except ValueError:
        print("Invalid JSON response.")


def create_post():
    """Send a POST request to create a test post."""
    url = f"{BASE_URL}/posts"

    new_post = {
        "title": "Learning Python APIs",
        "body": "I am learning API requests in Python.",
        "userId": 1
    }

    try:
        response = requests.post(
            url,
            json=new_post,
            timeout=10
        )
        response.raise_for_status()

        created_post = response.json()

        print("\n--- Created Test Post ---")
        print("Status:", response.status_code)
        print("Response:", created_post)

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except ValueError:
        print("Invalid JSON response.")


def main():
    print("PYTHON API PRACTICE PROJECT")

    get_single_post()
    get_multiple_posts()
    get_user_posts(1)
    create_post()


if __name__ == "__main__":
    main()
