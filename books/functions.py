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
        type_atr = AttributeType.get(type_name=check_field)
    return type_atr


def get_attribute(attribute_name, type_field, parent_info=None):
    attributes = Attribute.objects.all()
    types = AttributeType.objects.all()
    check_field = type(type_field)

    if not types.filter(type_name=check_field).exists():
        type_atr = AttributeType()
    else:
        type_atr = AttributeType.objects.get(type_name=check_field)
    type_atr.parent_info = parent_info
    type_atr.type_name = str(check_field)
    type_atr.save()

    if not attributes.filter(name=attribute_name).exists():
        attribute = Attribute()
    else:
        attribute = Attribute.objects.get(name=attribute_name)

    attribute.name = attribute_name
    attribute.type_field = type_atr
    attribute.parent_info = parent_info
    attribute.save()
    return attribute


def get_new_book(book_id, etag, selfLink):
    books = Book.objects.all()
    if books.filter(book_Id=book_id).exists():
        book = books.get(book_Id=book_id)
    else:
        book = Book()
        book.book_Id = book_id
        book.etag = etag
        book.selfLink = selfLink
        book.save()
    return book


def get_attr_value(book, attribute, value):
    attr_val = AttributeValue.objects.filter(book_id=book)
    # if attr_val.filter(book_id=book).exists() and attr_val.filter(attribute_id=attribute).exists():
    # attr_val.filter(book_id=book).filter(attribute_id=attribute)
    # for el in attr_val:
    #     if (type(value)) == str:
    #         if el.attribute_value_str != str(value):
    #             print(el.attribute_value_str, value)
    #             attr_val = AttributeValue()
    #             attr_val.book_id = book
    #             attr_val.attribute_id = attribute
    #             attr_val.attribute_value_str = value
    #             attr_val.save()
    #     if (type(value)) == bool:
    #         if attr_val.attribute_value_bool != bool(value):
    #             attr_val = AttributeValue()
    #             attr_val.book_id = book
    #             attr_val.attribute_id = attribute
    #             attr_val.attribute_value_bool = value
    #             attr_val.save()
    #     if (type(value)) == int:
    #         if attr_val.attribute_value_float != float(value):
    #             attr_val = AttributeValue()
    #             attr_val.attribute_value_float = value
    #             attr_val.book_id = book
    #             attr_val.attribute_id = attribute
    #             attr_val.save()
    # else:
    # print(type(value), value)
    if (type(value)) == str:
        attr_val = AttributeValue()
        attr_val.book_id = book
        attr_val.attribute_id = attribute
        attr_val.attribute_value_str = value
        attr_val.save()
    if (type(value)) == bool:
        attr_val = AttributeValue()
        attr_val.book_id = book
        attr_val.attribute_id = attribute
        attr_val.attribute_value_bool = value
        attr_val.save()
    if (type(value)) == int:
        attr_val = AttributeValue()
        attr_val.book_id = book
        attr_val.attribute_id = attribute
        attr_val.attribute_value_float = value
        attr_val.save()


def get_new_data(link):
    data_set = requests.get(link)
    data_set = data_set.json()
    books = Book.objects.all()
    attributes = Attribute.objects.all()
    types = AttributeType.objects.all()

    for el in data_set['items']:
        book = get_new_book(el['id'], el['etag'], el['selfLink'])
        volume_info = el['volumeInfo']
        for el in el.items():
            if type(el[1]) == str:
                attr_inst = get_attribute(el[0], el[1])
                get_attr_value(book, attr_inst, el[1])
            if type(el[1]) == dict:
                attr_inst = get_attribute(el[0], el[1])
                # print(el[0], el[1])
                for k, v in el[1].items():
                    if type(v) == dict:
                        pass
                        # print(v, type(v))
                    else:
                        # print(attr_inst)
                        attr_inst = get_attribute(k, v, attr_inst)
                        get_attr_value(book, attr_inst, v)
                # print(el_2, type(el_2))
                # attr_inst = get_attribute(el_2[0], el_2[1], attr_inst)
                #     attr_inst = get_attribute(el[0], el[1])
                #     if (type(el)) == tuple:
                #         for el_2 in el:
                #             if (type(el_2)) == dict:
                #                 print(el_2, el[str(el_2)])
                # print(el_2, type(el_2))
                #     for el_2 in el:
                #         print(el_2, type(el_2))
                #         if (type(el_2)) == tuple:
                #             for el_3 in el_2:
                #                 print(el_3, type(el_3))
                # else:
                # print(el_2, type(el_2))
                # else:
                # print(el, type(el))

                # for el in volume_info.items():
                #     attr = get_attribute(el[0], el[1])
                #     # get_attr_value(book, attr, el)
                #     # attr_val = AttributeValue()
                #     # attr_val.book_id = book
                #     # attr_val.attribute_id = attr
                #     if not (type(el[1])) == dict and not (type(el[1])) == list:
                #         pass
                #         # if (type(el[1])) == str:
                #         #     attr_val.attribute_value_str = el[1]
                #         # if (type(el[1])) == bool:
                #         #     attr_val.attribute_value_bool = el[1]
                #         # if (type(el[1])) == int:
                #         #     attr_val.attribute_value_float = el[1]
                #         # attr_val.save()
                #     else:
                #         for el_list in el[1]:
                #             if not (type(el_list)) == dict and not (type(el_list)) == list:
                #                 get_attr_value(book, attr, el_list)
                # print(book, attr, el_list)
                # attr_val = AttributeValue()
                # attr_val.book_id = book
                # attr_val.attribute_id = attr
                # if (type(el_list)) == str:
                #     attr_val.attribute_value_str = el_list
                # if (type(el_list)) == bool:
                #     attr_val.attribute_value_bool = el_list
                # if (type(el_list)) == int:
                #     attr_val.attribute_value_float = el_list
                # attr_val.save()
                # else:
                #     for el_list_list in el_list.items():
                #         attr_in_list = get_attribute(
                #             el_list_list[0], el_list_list[1], attr)
                #         get_attr_value(
                #             book, el_list_list[0], el_list_list[1])
                # attr_val = AttributeValue()
                # attr_val.book_id = book
                # attr_val.attribute_id = attr
                # if (type(el_list_list)) == str:
                #     attr_val.attribute_value_str = el_list_list
                # if (type(el_list_list)) == bool:
                #     attr_val.attribute_value_bool = el_list_list
                # if (type(el_list_list)) == int:
                #     attr_val.attribute_value_float = el_list_list
                # attr_val.save()
