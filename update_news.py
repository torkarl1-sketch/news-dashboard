#!/usr/bin/env python3
import requests
import json
import os
from datetime import datetime

api_key = os.environ.get("NEWS_API_KEY")
if not api_key:
    print("ERROR: NEWS_API_KEY not set")
    exit(1)

news_data = {
    "update_date": datetime.now().strftime("%Y-%m-%d"),
    "update_time": datetime.now().strftime("%H:%M"),
    "categories": {
        "world": [{"title": "Breaking: International News", "content": "Latest updates", "category": "World", "region": "International", "date": datetime.now().strftime("%Y-%m-%d"), "time": datetime.now().strftime("%H:%M"), "source": "News", "url": "https://newsapi.org", "is_hot": False}],
        "germany": [],
        "ingolstadt": [],
        "tech": [],
        "sports": []
    }
}

with open("news-data.json", "w") as f:
    json.dump(news_data, f, ensure_ascii=False, indent=2)
    
print("News updated!")
