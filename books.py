import requests
from bs4 import BeautifulSoup
req=requests.get("https://books.toscrape.com/")
s=req.content
soup=BeautifulSoup(s,"lxml")
fig=soup.find_all("article",class_="product_pod") #list of article elements
for fv in fig:
    n=fv.find("h3")
    z=n.find("a")
    x=z['title']
    div = fv.find("div",class_="product_price")
    p=div.find("p")
    pr=p.text
    print(x,pr)