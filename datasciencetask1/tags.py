# import requests
# from bs4 import BeautifulSoup
# with open('data/ebay.html','r') as f:
#     html_doc=f.read()
# soup=BeautifulSoup(html_doc,'html.parser')

# print(soup.title)
# import requests

# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# # Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
# # r = requests.get(url=URL, headers=headers)

import requests
from bs4 import BeautifulSoup
URL = "https://www.ebay.com"
  

r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
categories=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 