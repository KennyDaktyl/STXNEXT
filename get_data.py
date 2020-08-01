import requests
from books.models import *

data = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')
result = data.json()

authors = Author.objects.all()
categories = Category.objects.all()
for el in result['items']:
    db = Book()
    if not el['volumeInfo'].get('title') is None:
        print(el['volumeInfo']['title'])
        db.title = el['volumeInfo']['title']
    else:
        print('Brak tytułu')
        db.title = ''
    if not el['volumeInfo'].get('authors') is None:
        print(el['volumeInfo']['authors'])

        if authors.filter(author=el['volumeInfo']['authors']).exists():
            author = Author.objects.get(author=el['volumeInfo']['authors'])
        else:
            author = Author()
            author.author = el['volumeInfo']['authors']
            author.save()

    else:
        print('Brak autora')
        author = None
    if not el['volumeInfo'].get('publishedDate') is None:
        if len(el['volumeInfo']['publishedDate']) == 10:
            db.published_date_year = el['volumeInfo']['publishedDate'][0:4]
            print(el['volumeInfo']['publishedDate'])
        if len(el['volumeInfo']['publishedDate']) == 4:
            db.published_date_year = int(el['volumeInfo']['publishedDate'])
            print(el['volumeInfo']['publishedDate'])
    else:
        print('Brak daty publikacji')
    if not el['volumeInfo'].get('categories') is None:
        print(el['volumeInfo']['categories'])
        if categories.filter(category=el['volumeInfo']['categories']).exists():
            category = Category.objects.get(
                category=el['volumeInfo']['categories'])
        else:
            category = Category()
            category.category = el['volumeInfo']['categories']
            category.save()
    else:
        print('Brak kategorii')
        category = None
    if not el['volumeInfo'].get('averageRating') is None:
        print(el['volumeInfo']['averageRating'])
        db.average_rating = el['volumeInfo']['averageRating']
    else:
        print('Brak ratingu')
    if not el['volumeInfo'].get('ratingsCount') is None:
        print(el['volumeInfo']['ratingsCount'])
        db.ratings_count = el['volumeInfo']['ratingsCount']
    else:
        print('Brak ratingu')
    if not el['volumeInfo'].get('imageLinks').get('thumbnail') is None:
        print(el['volumeInfo']['imageLinks']['thumbnail'])
        db.thumbnail = el['volumeInfo']['imageLinks']['thumbnail']
    else:
        print('Brak zdjęcia')
    db.save()
    if author:
        db.authors.add(author)
    if category:
        db.categories.add(category)
    db.save()