name: Update News with Real Data

on:
  schedule:
    - cron: '0 6 * * *'
  workflow_dispatch:

jobs:
  update-news:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install requests
      - env:
          NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
        run: python update_news.py
      - run: |
          git config --local user.email "action@github.com"
          git config --local user.name "News Bot"
          git add news-data.json
          git commit -m "Update news" || exit 0
          git push
