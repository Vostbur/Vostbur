import requests
from bs4 import BeautifulSoup


url = "https://vostbur.github.io"
main_page = BeautifulSoup(requests.get(url).content, "html.parser")

content = '''
<div 
    data-iframe-width="150" 
    data-iframe-height="270" 
    data-share-badge-id="185c22b1-6ad5-4b35-ab65-fb499041fb23" data-share-badge-host="https://www.credly.com">
</div>
<script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js">
</script>

'''
content += f"### Last posts from [blog]({url}):\n\n"
for article_div in main_page.find_all("div", {"class": "mb-4"}):
    article_url = article_div.find("a", href=True)
    content += f"  - [{article_url.text}]({url + article_url['href']})\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
