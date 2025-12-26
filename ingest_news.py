import time
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("GNEWS_API_KEY")
URL = "https://gnews.io/api/v4/top-headlines"
DATA_FILE = "data/news.txt"

def fetch_and_save_news():
    params = {
        "token": API_KEY,
        "lang": "en",
        "country": "in",
        "max": 5
    }

    r = requests.get(URL, params=params)
    data = r.json()

    if "articles" not in data:
        print("❌ API ERROR:", data)
        return

    titles = []
    for a in data["articles"]:
        title = a.get("title")
        if title:
            titles.append(title)

    if not titles:
        print("⚠️ No new news")
        return

    # overwrite file each minute (clean)
    with open(DATA_FILE, "w") as f:
        for t in titles:
            f.write(t.strip() + "\n")

    print(f"✅ NEWS UPDATED ({len(titles)} items)")

# 🔁 AUTO LOOP: every 60 seconds
while True:
    fetch_and_save_news()
    print("⏳ Waiting 60 seconds...\n")
    time.sleep(60)
