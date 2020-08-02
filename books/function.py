import requests
from .models import *


def get_data(link):
    data = requests.get(link)
    result = data.json()
    book = Book.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()

    for el in result['items']:
        volume_info = el['volumeInfo']
        if not volume_info.get('title') is None:
            if book.filter(title=volume_info['title']).exists():
                db = book.get(
                    title=volume_info['title'])
            else:
                db = Book()
        authors_list = []
        categories_list = []
        if not volume_info.get('title') is None:
            db.title = volume_info['title']
        else:
            db.title = ''
        if not volume_info.get('authors') is None:
            check_list = isinstance(volume_info['authors'], list)
            if check_list:
                for el in volume_info.get('authors'):
                    if authors.filter(author=el).exists():
                        author = Author.objects.get(author=el)
                    else:
                        author = Author()
                        author.author = el
                        author.save()
                    authors_list.append(author)
            else:
                if authors.filter(author=volume_info['authors']).exists():
                    author = Author.objects.get(author=volume_info['authors'])
                else:
                    author = Author()
                    author.author = volume_info['authors']
                    author.save()
                    authors_list.append(author)
        else:
            author = None
        if not volume_info.get('publishedDate') is None:
            if len(volume_info['publishedDate']) == 10:
                db.published_date_year = volume_info['publishedDate'][0:4]

            if len(volume_info['publishedDate']) == 4:
                db.published_date_year = int(volume_info['publishedDate'])

        if not volume_info.get('categories') is None:
            check_list = isinstance(volume_info['categories'], list)
            if check_list:
                for el in volume_info.get('categories'):
                    if categories.filter(category=el).exists():
                        category = Category.objects.get(category=el)
                    else:
                        category = Category()
                        category.category = el
                        category.save()
                    categories_list.append(category)
            else:
                if categories.filter(
                        categories=volume_info['categories']).exists():
                    category = Category.objects.get(
                        categories=volume_info['categories'])
                else:
                    category = Author()
                    category.category = volume_info['categories']
                    category.save()
                    categories_list.append(category)
        else:
            category = None
        if not volume_info.get('averageRating') is None:
            db.average_rating = volume_info['averageRating']
        if not volume_info.get('ratingsCount') is None:
            db.ratings_count = volume_info['ratingsCount']
        if not volume_info.get('imageLinks').get('thumbnail') is None:
            db.thumbnail = volume_info['imageLinks']['thumbnail']
        db.save()
        if author:
            db.authors.add(*authors_list)
        if category:
            db.categories.add(category)
        db.save()


def save_data(json_data):
    result = json_data
    book = Book.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()

    for el in result['items']:
        volume_info = el['volumeInfo']
        if not volume_info.get('title') is None:
            if book.filter(title=volume_info['title']).exists():
                db = book.get(
                    title=volume_info['title'])
            else:
                db = Book()
        authors_list = []
        categories_list = []
        if not volume_info.get('title') is None:
            db.title = volume_info['title']
        else:
            db.title = ''
        if not volume_info.get('authors') is None:
            check_list = isinstance(volume_info['authors'], list)
            if check_list:
                for el in volume_info.get('authors'):
                    if authors.filter(author=el).exists():
                        author = Author.objects.get(author=el)
                    else:
                        author = Author()
                        author.author = el
                        author.save()
                    authors_list.append(author)
            else:
                if authors.filter(author=volume_info['authors']).exists():
                    author = Author.objects.get(author=volume_info['authors'])
                else:
                    author = Author()
                    author.author = volume_info['authors']
                    author.save()
                    authors_list.append(author)
        else:
            author = None
        if not volume_info.get('publishedDate') is None:
            if len(volume_info['publishedDate']) == 10:
                db.published_date_year = volume_info['publishedDate'][0:4]

            if len(volume_info['publishedDate']) == 4:
                db.published_date_year = int(volume_info['publishedDate'])

        if not volume_info.get('categories') is None:
            check_list = isinstance(volume_info['categories'], list)
            if check_list:
                for el in volume_info.get('categories'):
                    if categories.filter(category=el).exists():
                        category = Category.objects.get(category=el)
                    else:
                        category = Category()
                        category.category = el
                        category.save()
                    categories_list.append(category)
            else:
                if categories.filter(
                        categories=volume_info['categories']).exists():
                    category = Category.objects.get(
                        categories=volume_info['categories'])
                else:
                    category = Author()
                    category.category = volume_info['categories']
                    category.save()
                    categories_list.append(category)
        else:
            category = None
        if not volume_info.get('averageRating') is None:
            db.average_rating = volume_info['averageRating']
        if not volume_info.get('ratingsCount') is None:
            db.ratings_count = volume_info['ratingsCount']
        if not volume_info.get('imageLinks').get('thumbnail') is None:
            db.thumbnail = volume_info['imageLinks']['thumbnail']
        db.save()
        if author:
            db.authors.add(*authors_list)
        if category:
            db.categories.add(category)
        db.save()
