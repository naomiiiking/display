import requests, os, json
from dotenv import load_dotenv

load_dotenv()

class newsClient():
    def __init__(self):
        self.api_key = os.environ.get("NEWS_API_KEY")
        self.country = "gb"

    def get_news(self, source, category, keyword):
        url = f"https://newsapi.org/v2/top-headlines?sources={source}&q={keyword}&apiKey={self.api_key}"
        try:
            resp = requests.get(url)
            resp.raise_for_status
            resp = resp.json()

            articles = resp.get("articles")
            output = f"News: {category}"
            for article in articles:
                title = article.get("title")
                title = title.replace("| TechCrunch", "")
                output += f"\n - {title}"

            print(output)
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

#sources wired, bbc-news, techcrunch, the-next-web, the-verge