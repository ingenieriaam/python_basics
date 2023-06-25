import bs4
import requests
import lxml

webpage = 'https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html'
web_request = requests.get(webpage)
print(type(web_request))
print('this is a entire webpage code')
print(web_request.text)
print("-----------------------------------------------------------------")

# Beautiful soup is a Python library for pulling data out of HTML and XML files.
websoup = bs4.BeautifulSoup(web_request.text, 'lxml')
print(websoup)
# print(websoup.select('title'))
# print(websoup.select('p'))
print(len(websoup.select('p')))
print("-----------------------------------------------------------------")

theTitle = websoup.select('title')[0].getText()
print(theTitle)
print("-----------------------------------------------------------------")

##################################################################
lateralColumn = websoup.select('.widget-content') #get class
print(lateralColumn)
print("-----------------------------------------------------------------")
lateralColumn = websoup.select('.widget-content h3') #get all headers 
print(lateralColumn)
print(f'{len(lateralColumn)} level 3 headers found')
print("-----------------------------------------------------------------")
for h in lateralColumn:
    print(h.getText())
print("-----------------------------------------------------------------")