import requests
from bs4 import BeautifulSoup


url = "https://vostbur.github.io"
main_page = BeautifulSoup(requests.get(url).content, "html.parser")


# Bages from credly.com in header
content = '''
[![](emerging-technologies-workshop-model-driven-programmability.png)](https://www.credly.com/badges/185c22b1-6ad5-4b35-ab65-fb499041fb23/public_url)
[![](intro-to-cybersec.png)](https://www.credly.com/badges/0b0c9355-b236-4302-bdc5-aa3b6f8c9b8d/public_url/)

'''

content += f"### Last posts from [blog]({url}):\n\n"
for article_main in main_page.find_all("article", {"class": "post-entry"}):
    article_header = article_main.find("h2").text 
    article_url = article_main.find("a", href=True)
    content += f"  - [{article_header}]({article_url["href"]})\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
