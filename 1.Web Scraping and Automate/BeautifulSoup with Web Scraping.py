from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# store all the code in text of this particular page
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
print(soup.title.getText()) # will return a title in tab bar in browser


#_________________________Get whole of information of this web___________________________
article_titles = []
article_links = []
for article_tag in soup.find_all(name="a", rel="noreferrer"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes = []
for article in soup.find(name="span", class_="score"):
    if article.getText() is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.getText().split()[0]))

# find a max article upvote
max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}.")