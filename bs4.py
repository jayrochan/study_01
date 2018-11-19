import requests,bs4
res =requests.get('https://tonari-it.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
print(soup.title)