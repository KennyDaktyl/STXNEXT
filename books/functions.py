import requests
from .models import *


def save_in_db(load_data):
    result = load_data
    book = Book.objects.all()

    # for el in result['items']:
    #     volume_info = el['volumeInfo']
    #     authors_list = []
    #     categories_list = []
    #     if not volume_info.get('title') is None:
    #         if book.filter(title=volume_info['title']).exists():
    #             db = book.get(
    #                 title=volume_info['title'])
    #         else:
    #             db = Book()
    #         db.title = volume_info.get('title')
    #         if not volume_info.get('authors') is None:
    #             check_list = isinstance(volume_info['authors'], list)
    #             if check_list:
    #                 for el in volume_info.get('authors'):
    #                     if authors.filter(author=el).exists():
    #                         author = Author.objects.get(author=el)
    #                     else:
    #                         author = Author()
    #                         author.author = el
    #                         author.save()
    #                     authors_list.append(author)
    #             else:
    #                 if authors.filter(author=volume_info['authors']).exists():
    #                     author = Author.objects.get(
    #                         author=volume_info['authors'])
    #                 else:
    #                     author = Author()
    #                     author.author = volume_info['authors']
    #                     author.save()
    #                     authors_list.append(author)
    #         else:
    #             author = None
    #         if not volume_info.get('publishedDate') is None:
    #             if len(volume_info['publishedDate']) == 10:
    #                 db.published_date_year = volume_info['publishedDate'][0:4]

    #             if len(volume_info['publishedDate']) == 4:
    #                 db.published_date_year = int(volume_info['publishedDate'])

    #         if not volume_info.get('categories') is None:
    #             check_list = isinstance(volume_info['categories'], list)
    #             if check_list:
    #                 for el in volume_info.get('categories'):
    #                     if categories.filter(category=el).exists():
    #                         category = Category.objects.get(category=el)
    #                     else:
    #                         category = Category()
    #                         category.category = el
    #                         category.save()
    #                     categories_list.append(category)
    #             else:
    #                 if categories.filter(
    #                         categories=volume_info['categories']).exists():
    #                     category = Category.objects.get(
    #                         categories=volume_info['categories'])
    #                 else:
    #                     category = Author()
    #                     category.category = volume_info['categories']
    #                     category.save()
    #                     categories_list.append(category)
    #         else:
    #             category = None
    #         if not volume_info.get('averageRating') is None:
    #             db.average_rating = volume_info['averageRating']
    #         if not volume_info.get('ratingsCount') is None:
    #             db.ratings_count = volume_info['ratingsCount']
    #         if not volume_info.get('imageLinks').get('thumbnail') is None:
    #             db.thumbnail = volume_info['imageLinks']['thumbnail']
    #         db.save()
    #         if author:
    #             db.authors.add(*authors_list)
    #         if category:
    #             db.categories.add(*categories_list)
    #         db.save()


def get_data(link):
    data_set = requests.get(link)
    data_set = data_set.json()
    save_in_db(data_set)


def get_type_field(field_element):
    types = AttributeType.objects.all()
    check_field = type(field_element)
    if not types.filter(type_name=check_field).exists():
        type_atr = AttributeType()
        type_atr.type_name = str(check_field)
        type_atr.save()
    else:
        type_atr = AttributeType.objects.get(type_name=check_field)
    return type_atr


def get_attribute(attribute, type_field):
    attributes = Attribute.objects.all()
    if not attributes.filter(name=attribute).exists():
        attribute = Attribute()
        attribute.name = attribute
        attribute.type_field = get_type_field(type_field)
        attribute.save()
    else:
        attribute = Attribute.objects.get(name=attribute)
    return attribute


def get_new_book(book_id, etag, selfLink):
    books = Book.objects.all()
    if books.filter(book_Id=book_id).exists():
        book = books.objects.get(book_Id=book_id)
    else:
        book = Book()
        book.book_Id = book_id
        book.etag = etag
        book.selfLink = selfLink
        book.save()
    return book


def get_new_data(link):
    data_set = requests.get(link)
    data_set = data_set.json()
    books = Book.objects.all()
    attributes = Attribute.objects.all()
    types = AttributeType.objects.all()
    for el in data_set['items']:
        get_new_book(el['id'], el['etag'], el['selfLink'])
    # for el in data_set['items']:
    #     volume_info = el['volumeInfo']
    #     for el in volume_info.items():
    #         # get_attribute(el[0], el[1])
    #         if not attributes.filter(name=el[0]).exists():
    #             attribute = Attribute()
    #             attribute.name = el[0]
    #             attribute.type_field = get_type_field(el[1])
    #             attribute.save()

        # if (type(el[1])) == str:
        #     print(el[1])
        # if (type(el[1])) == int:
        #     print(el[1])
        # if (type(el[1])) == dict:
        #     for el in el[1].items():
        #         print(type(el))
        # if (type(el[1])) == list:
        #     for el in el[1]:
        #         # if (type(el)) == dict:
        #         #     print(type(el))
        #         # if (type(el)) == str:
        #         #     print(type(el))
        #         print(type(el))
        #         print(el)
        # print(volume_info.items())
        #     check_list = isinstance(el, list)
        #     # print(check_list)
        #     print(el)
        # # if not check_list:
        # #
