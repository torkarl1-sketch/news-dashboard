```yaml
name: Update News with Real Data

on:
  schedule:
    - cron: '0 6 * * *'
  workflow_dispatch:

jobs:
  update-news:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install requests
      
      - name: Fetch and update news
        env:
          NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
        run: python update_news.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "News Bot"
          git add news-data.json
          git commit -m "📰 Auto-update: $(date '+%d.%m.%Y %H:%M')" || exit 0
          git push
```
