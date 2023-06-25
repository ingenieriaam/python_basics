import bs4
import requests
import lxml


# Explore different elements of multiple pages

base_url    = 'http://books.toscrape.com/catalogue/page-{}.html'
# if i want to use a different pages number:
# e.g. print(base_url.format(2)) for page 2
# Free to use page for scraping practice
web_request = requests.get(base_url.format('1')) # only first page
websoup     = bs4.BeautifulSoup(web_request.text, 'lxml')

# Extracting data from the webpage where califications are 4 or 5
# in this page we have this structure:
# <p class="star-rating Three">...</p>
# <p class="star-rating Four">...</p> etc
# califications and title is in product_pod class
products = websoup.select('.product_pod')
print(f'page 1 have {len(products)} books')

print("-----------------------------------------------------------------")
print(f'This is the product structure: \n{products[0]}\n\n')
eg1Rating = products[0].select('.star-rating.Three') # replace space with dot
print(f'This is the product rating structure: \n{eg1Rating}\n\n')
eg1Title = products[0].select('a')[1]['title']
print(f'This is the product title : \n{eg1Title}\n\n')

print("-----------------------------------------------------------------")
high_rating_books = []

for page in range(1,51):
    # creating soups
    web_request = requests.get(base_url.format(page))
    websoup     = bs4.BeautifulSoup(web_request.text, 'lxml')
    
    # Data select
    books = websoup.select('.product_pod')
    for book in books:
        # rating check
        rating4 = book.select('.star-rating.Four')
        rating5 = book.select('.star-rating.Five')
        goodRating = len(rating4)>0 or len(rating5)>0
        
        if goodRating:
            bookTitle = book.select('a')[1]['title']
            high_rating_books.append(bookTitle)

# High rating books presentation
i = 0
print('High rating books:')
for book in high_rating_books:
    print(f'{i}: {book}')
    i += 1



