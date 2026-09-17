import requests

headers = {"User-Agent": "TrendPulse/1.0"}

# Task 1: Get top 500 story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

story_ids = response.json()[:500]

# Get story details
stories = []

for i, story_id in enumerate(story_ids):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )

        if response.ok:
            story = response.json()

            if story:
                stories.append(story)

        else:
            print("Request failed:", story_id)

    except requests.exceptions.RequestException:
        print("Request failed:", story_id)

    if (i + 1) % 50 == 0:
        print("Fetched:", i + 1)

print("Stories:", len(stories))

# Task 2: Extract fields
posts = []

for story in stories:
    post = {
        "post_id": story.get("id"),
        "title": story.get("title", ""),
        "category": "",
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0)
    }
    posts.append(post)

print("Posts:", len(posts))
print(posts[:3])



import time

categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

for category, keywords in categories.items():

    for post in posts:
        title = post["title"].lower()

        if post["category"] == "":
            for keyword in keywords:
                if keyword.lower() in title:
                    post["category"] = category
                    break

print(posts[:10])