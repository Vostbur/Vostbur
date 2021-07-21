import requests
from bs4 import BeautifulSoup


url = "https://vostbur.github.io"
main_page = BeautifulSoup(requests.get(url).content, "html.parser")
urls = []

content = f"### Last posts from [blog]({url}):\n\n"
for article_div in main_page.find_all("div", {"class": "mb-4"}):
    article_url = article_div.find("a", href=True)
    content += f"  - [{article_url.text}]({article_url['href']})\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
