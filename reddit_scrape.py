import praw
import csv
from datetime import datetime

# Set up your Reddit API client properly
reddit = praw.Reddit(
    client_id="8yYiSle01EIN1x9XZUCf2w",
    client_secret="h13xtoj7CMPccNySPIsfK8t-oZ5dCQ",
    username="Web_scrape_automate",
    password="Molan_3770",
    user_agent="script:NASDAQ_search:v1.0 (by u/automate-with-python)"
)

# Enable read-only mode
reddit.read_only = True


# Choose the subreddit
subreddit = reddit.subreddit("wallstreetbets")

print(subreddit.display_name)
# Output: redditdev
print(subreddit.title)
# Output: reddit development
print(subreddit.description)
# Output: a subreddit for discussion of ..


# Search for posts containing 'NASDAQ'
for submission in subreddit.search("NASDAQ", limit=10):
    print(f"Title: {submission.title}")
    print(f"URL: {submission.url}")
    print(f"Score: {submission.score}")
    print(f"Created: {submission.created_utc}")
    print(f"Comments: {submission.num_comments}")
    print("-" * 40)


# Search for posts with the keyword "NASDAQ"
posts = subreddit.search("NASDAQ", limit=20)


# File path to save the results
csv_file_path = "nasdaq_posts.csv"

# Write to CSV
with open(csv_file_path, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Body", "Date"])  # Header row

    for post in posts:
        title = post.title
        body = post.selftext.strip()
        date = datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([title, body, date])

print(f"Saved posts to {csv_file_path}")