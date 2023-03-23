import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.cet.ac.in/head-of-departments/")
source = req.content
soup = BeautifulSoup(source,"lxml")

fig=soup.find("figure",class_="wp-block-table")
tab=fig.find("table")
row=tab.find_all("tr")
row=row[1:]
for r in row:
    tds =r.find_all("td")
    n=tds[0].text
    print(n)
