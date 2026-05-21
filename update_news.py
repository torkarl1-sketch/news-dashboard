import json
from datetime import datetime

data = {
    "update_date": datetime.now().strftime("%Y-%m-%d"),
    "update_time": datetime.now().strftime("%H:%M"),
    "categories": {
        "world": [{"title": "Neue Nachrichten", "content": "Dashboard aktualisiert", "category": "News", "region": "World", "date": datetime.now().strftime("%Y-%m-%d"), "time": datetime.now().strftime("%H:%M"), "source": "News", "url": "https://news.de", "is_hot": False}],
        "germany": [],
        "ingolstadt": [],
        "tech": [],
        "sports": []
    }
}

with open("news-data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
