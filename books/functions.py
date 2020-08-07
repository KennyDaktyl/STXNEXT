from django.core import serializers
import requests
from .models import *
import json


# def save_in_db(load_data):
#     result = load_data
#     book = Book.objects.all()


# def get_data(link):
#     data_set = requests.get(link)
#     data_set = data_set.json()
#     save_in_db(data_set)


def get_type_field(field_element):
    """The Function create type_field instance

    Parameters:
    argument1 (field_element): Name of type_field in list

    Returns:
    field_element:Instance TypeField

   """
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
    """The Function create Attribute instance
    Parameters:
    argument1 (attribute_name): Name of attribute
    argument2 (type_field): Type of value
    argument3 (parent_info): Information about - If Attribute in dictionary has parent

    Returns:
    attribute:Instance Attribute
    """
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


def get_new_book(bookId, etag, selfLink):
    """The Function create or edit Book instance
    Parameters:
    argument1 (bookId): Name of attribute
    argument2 (type_field): Type of value
    argument3 (parent_info): Information about - If Attribute in dictionary has parent

    Returns:
    attribute:Instance Attribute
    """
    books = Book.objects.all()
    if books.filter(bookId=bookId).exists():
        book = books.get(bookId=bookId)
    else:
        book = Book()
        book.bookId = bookId
        book.etag = etag
        book.selfLink = selfLink
        book.save()
    return book


def get_attr_value(book, attribute, value):
    """The Function create value of attribute in book
    Parameters:
    argument1 (book): Book instance
    argument2 (attribute): Attribute instance
    argument3 (valueo): Value of attribte

    Returns:
    attr_value:Value of Attribute in Book's 
    """
    attr_val = AttributeValue.objects.filter(bookId=book)
    if attr_val.filter(bookId=book).exists() and attr_val.filter(attributeId=attribute).exists():
        attrs_exist = attr_val.filter(
            bookId=book).filter(attributeId=attribute)
        for el in attrs_exist:
            if (type(value)) == str:
                if not str(el.attribute_value_str) == str(value):
                    attr_val = AttributeValue()
                    attr_val.bookId = book
                    attr_val.attributeId = attribute
                    attr_val.attribute_value_str = value
                    attr_val.save()
            if (type(value)) == bool:
                if not el.attribute_value_bool == value:
                    attr_val = AttributeValue()
                    attr_val.bookId = book
                    attr_val.attributeId = attribute
                    attr_val.attribute_value_bool = value
                    attr_val.save()
            if (type(value)) == int:
                if not el.attribute_value_float == value:
                    attr_val = AttributeValue()
                    attr_val.bookId = book
                    attr_val.attributeId = attribute
                    attr_val.attribute_value_float = value
                    attr_val.save()
            # if (type(value)) == list:
            #     if not el.attribute_value_list == value:
            #         for el_list in value:
            #             try:
            #                 # attr_val = attr_val.objects.get(
            #                 #     attribute_value_list=el_list)
            #                 print(str(el_list)+":"+str(value))
            #             except:
                    # attr_val = AttributeValue()
                    # attr_val.bookId = book
                    # attr_val.attributeId = attribute
                    # attr_val.attribute_value_list = str(value)
                    # attr_val.save()
    else:
        if (type(value)) == str:
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_str = value
            attr_val.save()
        if (type(value)) == bool:
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_bool = value
            attr_val.save()
        if (type(value)) == int:
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_float = value
            attr_val.save()
        if (type(value)) == list:
            for el_list in value:
                attr_val = AttributeValue()
                attr_val.bookId = book
                attr_val.attributeId = attribute
                attr_val.attribute_value_list = el_list
                attr_val.save()
        # if (type(value)) == dict:
        #     for k, v in value:
        #         attr_val = AttributeValue()
        #         attr_val.bookId = book
        #         attr_val.attributeId = attribute
        #         attr_val.attribute_value_dict = el_list
        #         attr_val.save()

    return attr_val


def get_new_data(link):
    """The Function create data from dataset in database
    Parameters:
    argument1 (link): Link with dataset
    """
    data_set = requests.get(link)
    data_set = data_set.json()
    books = Book.objects.all()
    attributes = Attribute.objects.all()
    types = AttributeType.objects.all()

    for el in data_set['items']:
        book = get_new_book(el['id'], el['etag'], el['selfLink'])
        volume_info = el['volumeInfo']

        for el in el.items():
            parent_info = (el[0])
            if type(el[1]) == str:
                attr_inst = get_attribute(el[0], el[1])
                get_attr_value(book, attr_inst, el[1])
            if type(el[1]) == dict:
                attr_inst = get_attribute(el[0], el[1])
                for k, v in el[1].items():
                    if type(v) == dict:
                        attr_inst = get_attribute(
                            k, v, parent_info=Attribute.objects.get(name=parent_info))
                        for el in v.items():
                            attr_inst = get_attribute(
                                el[0], el[1], parent_info=Attribute.objects.get(name=k))
                            get_attr_value(book, attr_inst, el[1])

                    else:
                        attr_inst = get_attribute(
                            k, v, parent_info=Attribute.objects.get(name=parent_info))
                        get_attr_value(book, attr_inst, v)


def get_book(book):
    """The Function get all attributes for book
    Parameters:
    argument1 (book): Book instance
    Returns:
    attrs_dict: List with filter of Attributes in Book 
    """
    attrs = AttributeValue.objects.filter(bookId=book)
    attrs_dict = {}
    authors_list = []
    categories_list = []
    for attr in attrs:
        if str(attr.attributeId.name) == 'title':
            attrs_dict[attr.attributeId.name] = attr.attribute_value_str
        if str(attr.attributeId.name) == 'authors':
            authors_list.append(attr.attribute_value_list)
            attrs_dict[attr.attributeId.name] = authors_list
        if str(attr.attributeId.name) == 'publishedDate':
            attrs_dict[attr.attributeId.name] = attr.attribute_value_str
        if str(attr.attributeId.name) == 'rating':
            attrs_dict[attr.attributeId.name] = attr.attribute_value_str
        if str(attr.attributeId.name) == 'categories':
            categories_list.append(attr.attribute_value_list)
            attrs_dict[attr.attributeId.name] = categories_list
        if str(attr.attributeId.name) == 'averageRating':
            attrs_dict[attr.attributeId.name] = attr.attribute_value_float
        if str(attr.attributeId.name) == 'ratingsCount':
            attrs_dict[attr.attributeId.name] = attr.attribute_value_float
        if str(attr.attributeId.name) == 'thumbnail':
            attrs_dict[attr.attributeId.name] = attr.attribute_value_str

    return attrs_dict
