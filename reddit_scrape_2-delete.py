import requests
import csv
from datetime import datetime

# Define Pushshift API search endpoint
url = "https://api.pushshift.io/reddit/search/submission/"

# Define search parameters
params = {
    "q": "NASDAQ",
    "subreddit": "wallstreetbets",
    "after": "2005-06-01",
    "size": 100,  # Max allowed per request
    "sort": "asc"
}

# Create CSV file
csv_file_path = "nasdaq_pushshift_posts.csv"
with open(csv_file_path, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Body", "Date"])

    while True:
        response = requests.get(url, params=params)
        data = response.json()["data"]
        if not data:
            break  # No more results

        for post in data:
            title = post.get("title", "")
            body = post.get("selftext", "")
            timestamp = post.get("created_utc", 0)
            date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([title, body, date])

        # Update 'after' to fetch next page
        params["after"] = data[-1]["created_utc"]
        print(f"Fetched up to: {date}")

print(f"Saved historical posts to {csv_file_path}")