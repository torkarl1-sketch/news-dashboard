#!/usr/bin/env python3
"""
News Update Script - Echte aktuelle Nachrichten von NewsAPI
Läuft automatisch um 6:00 Uhr via GitHub Actions
"""

import requests
import json
import os
from datetime import datetime

def get_news_from_api(api_key):
    """Hole Nachrichten von NewsAPI.org"""
    
    base_url = "https://newsapi.org/v2/everything"
    
    news_data = {
        "update_date": datetime.now().strftime("%Y-%m-%d"),
        "update_time": datetime.now().strftime("%H:%M"),
        "categories": {
            "world": [],
            "germany": [],
            "ingolstadt": [],
            "tech": [],
            "sports": []
        }
    }
    
    # WELTNACHRICHTEN
    print("🌍 Fetching world news...")
    try:
        params = {
            "q": "international politics security",
            "language": "de",
            "sortBy": "publishedAt",
            "pageSize": 5,
            "apiKey": api_key
        }
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:5]:
                news_data["categories"]["world"].append({
                    "title": article.get("title", "")[:80],
                    "content": article.get("description", "")[:200],
                    "category": "International",
                    "region": "World",
                    "date": article.get("publishedAt", "").split("T")[0],
                    "time": article.get("publishedAt", "").split("T")[1][:5] if "T" in article.get("publishedAt", "") else "",
                    "source": article.get("source", {}).get("name", "News"),
                    "url": article.get("url", ""),
                    "is_hot": False
                })
    except Exception as e:
        print(f"⚠️ Fehler bei Weltnachrichten: {e}")
    
    # DEUTSCHLAND
    print("🇩🇪 Fetching Germany news...")
    try:
        params = {
            "q": "Deutschland Germany",
            "language": "de",
            "sortBy": "publishedAt",
            "pageSize": 5,
            "apiKey": api_key
        }
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:5]:
                news_data["categories"]["germany"].append({
                    "title": article.get("title", "")[:80],
                    "content": article.get("description", "")[:200],
                    "category": "Deutschland",
                    "region": "Germany",
                    "date": article.get("publishedAt", "").split("T")[0],
                    "time": article.get("publishedAt", "").split("T")[1][:5] if "T" in article.get("publishedAt", "") else "",
                    "source": article.get("source", {}).get("name", "News"),
                    "url": article.get("url", ""),
                    "is_hot": False
                })
    except Exception as e:
        print(f"⚠️ Fehler bei Deutschland: {e}")
    
    # INGOLSTADT
    print("🏛️ Fetching Ingolstadt news...")
    try:
        params = {
            "q": "Ingolstadt",
            "language": "de",
            "sortBy": "publishedAt",
            "pageSize": 5,
            "apiKey": api_key
        }
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:5]:
                news_data["categories"]["ingolstadt"].append({
                    "title": article.get("title", "")[:80],
                    "content": article.get("description", "")[:200],
                    "category": "Ingolstadt",
                    "region": "Ingolstadt",
                    "date": article.get("publishedAt", "").split("T")[0],
                    "time": article.get("publishedAt", "").split("T")[1][:5] if "T" in article.get("publishedAt", "") else "",
                    "source": article.get("source", {}).get("name", "News"),
                    "url": article.get("url", ""),
                    "is_hot": False
                })
    except Exception as e:
        print(f"⚠️ Fehler bei Ingolstadt: {e}")
    
    # TECHNOLOGIE
    print("💻 Fetching tech news...")
    try:
        params = {
            "q": "technology AI KI",
            "language": "de",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "apiKey": api_key
        }
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:3]:
                news_data["categories"]["tech"].append({
                    "title": article.get("title", "")[:80],
                    "content": article.get("description", "")[:200],
                    "category": "Technology",
                    "region": "World",
                    "date": article.get("publishedAt", "").split("T")[0],
                    "time": article.get("publishedAt", "").split("T")[1][:5] if "T" in article.get("publishedAt", "") else "",
                    "source": article.get("source", {}).get("name", "News"),
                    "url": article.get("url", ""),
                    "is_hot": False
                })
    except Exception as e:
        print(f"⚠️ Fehler bei Tech: {e}")
    
    # SPORT
    print("⚽ Fetching sports news...")
    try:
        params = {
            "q": "sport fussball",
            "language": "de",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "apiKey": api_key
        }
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:3]:
                news_data["categories"]["sports"].append({
                    "title": article.get("title", "")[:80],
                    "content": article.get("description", "")[:200],
                    "category": "Sports",
                    "region": "Germany",
                    "date": article.get("publishedAt", "").split("T")[0],
                    "time": article.get("publishedAt", "").split("T")[1][:5] if "T" in article.get("publishedAt", "") else "",
                    "source": article.get("source", {}).get("name", "News"),
                    "url": article.get("url", ""),
                    "is_hot": False
                })
    except Exception as e:
        print(f"⚠️ Fehler bei Sport: {e}")
    
    return news_data

def main():
    """Hauptprogramm"""
    
    api_key = os.environ.get("NEWS_API_KEY")
    
    if not api_key:
        print("❌ Fehler: NEWS_API_KEY nicht gesetzt!")
        return False
    
    print("=" * 60)
    print("📰 NEWS UPDATE - NEWSAPI")
    print("=" * 60)
    print()
    
    # Hole News
    news_data = get_news_from_api(api_key)
    
    # Zähle Artikel
    total = sum(len(v) for v in news_data["categories"].values())
    
    # Speichere
    try:
        with open("news-data.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Erfolgreich aktualisiert!")
        print(f"📊 {total} Artikel geladen")
        print(f"📅 {news_data['update_date']} {news_data['update_time']}")
        print()
        
        return True
        
    except Exception as e:
        print(f"\n❌ Fehler beim Speichern: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
