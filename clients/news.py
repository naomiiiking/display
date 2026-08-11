import requests, os, json
from dotenv import load_dotenv

load_dotenv()

class newsClient():
    def __init__(self):
        self.api_key = os.environ.get("NEWS_API_KEY")
        self.country = "gb"

    def get_news(self, source, keyword):
        url = f"https://newsapi.org/v2/top-headlines?sources={source}&q={keyword}&apiKey={self.api_key}"
        try:
            resp = requests.get(url)
            resp.raise_for_status
            resp = resp.json()

            output = ""
            articles = resp.get("articles")
            articles = articles[:3]

            for article in articles:
                title = article.get("title")
                title = title.replace("| TechCrunch", "")
                output += f"\n - {title}"

            return output
        except requests.RequestException as e:
            return f"Error fetching news data: {e}"

#sources wired, bbc-news, techcrunch, the-next-web, the-verge