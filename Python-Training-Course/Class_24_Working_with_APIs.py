# Class 24 - Working with APIs

# First install requests
# pip install requests

import requests

# GET request - fetch data from API
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

# Check status code
print(response.status_code)    # 200 means success

# Read response as JSON
data = response.json()
print(data["name"])             # Leanne Graham
print(data["email"])            # Sincere@april.biz

# Fetch list of posts
posts_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(posts_url)
posts = response.json()

# Print first 3 posts
for post in posts[:3]:
    print(f"Title: {post['title']}")
    print(f"Body: {post['body'][:50]}...")
    print()

# practical example - get random activity
activity_url = "http://www.boredapi.com/api/activity/"
response = requests.get(activity_url)
if response.status_code == 200:
    activity = response.json()
    print(f"Try this: {activity['activity']}")
