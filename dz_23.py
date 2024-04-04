# import requests
# from bs4 import BeautifulSoup

# def get_books_titles(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     books = soup.find_all('h3')[:20]
#     titles = [book.a['title'] for book in books]
#     return titles

# def main():
#     url = 'https://books.toscrape.com/catalogue/category/books/science_22/index.html'
#     books_titles = get_books_titles(url)
    
#     print("Название 20 книг с сайта:")
#     for i, title in enumerate(books_titles, 1):
#         print(f"{i}. {title}")

# if __name__ == "__main__":
#     main()