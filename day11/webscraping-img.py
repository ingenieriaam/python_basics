import bs4
import requests
import lxml

webpage     = 'https://www.escueladirecta.com/'
web_request = requests.get(webpage)
websoup     = bs4.BeautifulSoup(web_request.text, 'lxml')
print("-----------------------------------------------------------------")

images = websoup.select('img')
for img in images:
    print(img)

# exploring images, we can see that the courses images are in a class
# course-box-image

images = websoup.select('.course-box-image')
for img in images:
    print(img)

# in src, we have the full path to the image
# e.g for course 1

img1 = websoup.select('.course-box-image')[0]['src']
imagage1 = requests.get(img1)
f = open('img1.png', 'wb')
f.write(imagage1.content)
f.close()
