import requests 
from bs4 import BeautifulSoup

web = requests.get("https://pypi.org/project/beautifulsoup4/") 
web.status_code
web.content
# print(web.content)
soup = BeautifulSoup(web.content ,"html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.p)
# print(soup.a) # ancle tag
tag = soup.html
tag=soup.p
print(tag)