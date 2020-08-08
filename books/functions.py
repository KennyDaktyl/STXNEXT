from django.core import serializers
import requests
from .models import *
import json


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

    if parent_info:
        parent_info = Attribute.objects.get(pk=parent_info)

    try:
        attribute = Attribute.objects.get(
            name=attribute_name, parent_info=parent_info)
    except:
        attribute = Attribute()
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
    # if str(attribute.type_field.type_name) == "<class 'list'>":
    # print('lista', attribute.type_field)
    # else:
    # print(attribute.type_field.type_name, "<class 'list'>")
    attr_val = AttributeValue.objects.filter(bookId=book)
    if attr_val.filter(bookId=book).exists() and attr_val.filter(attributeId=attribute).exists():
        attrs_exist = attr_val.filter(
            bookId=book).filter(attributeId=attribute)
        for el in attrs_exist:
            if str(attribute.type_field.type_name) == "<class 'str'>":
                try:
                    attr_val = attrs_exist.get(bookId=book,
                                               attribute_value_str=str(el.attribute_value_str))
                except:
                    attr_val = AttributeValue()
                attr_val.bookId = book
                attr_val.attributeId = attribute
                attr_val.attribute_value_str = value
                attr_val.save()
            if str(attribute.type_field.type_name) == "<class 'bool'>":
                try:
                    attr_val = attrs_exist.get(bookId=book,
                                               attribute_value_bool=str(el.attribute_value_bool))
                except:
                    attr_val = AttributeValue()
                attr_val.bookId = book
                attr_val.attributeId = attribute
                attr_val.attribute_value_bool = value
                attr_val.save()
            if str(attribute.type_field.type_name) == "<class 'int'>":
                try:
                    attr_val = attrs_exist.get(bookId=book,
                                               attribute_value_float=str(el.attribute_value_float))
                except:
                    attr_val = AttributeValue()
                attr_val.bookId = book
                attr_val.attributeId = attribute
                attr_val.attribute_value_float = value
                attr_val.save()
            if str(attribute.type_field.type_name) == "<class 'float'>":
                try:
                    attr_val = attrs_exist.get(bookId=book,
                                               attribute_value_float=str(el.attribute_value_float))
                except:
                    attr_val = AttributeValue()
                attr_val.bookId = book
                attr_val.attributeId = attribute
                attr_val.attribute_value_float = value
                attr_val.save()
            if str(attribute.type_field.type_name) == "<class 'list'>":
                try:
                    attr_val = attrs_exist.get(bookId=book,
                                               attribute_value_list=str(el.attribute_value_list))
                except:
                    attr_val = AttributeValue()
                attr_val.bookId = book
                attr_val.attributeId = attribute
                attr_val.attribute_value_list = str(value)
                attr_val.save()
    else:
        if str(attribute.type_field.type_name) == "<class 'str'>":
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_str = value
            attr_val.save()
        if str(attribute.type_field.type_name) == "<class 'bool'>":
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_bool = value
            attr_val.save()
        if str(attribute.type_field.type_name) == "<class 'int'>":
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_float = value
            attr_val.save()
        if str(attribute.type_field.type_name) == "<class 'float'>":
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_float = value
            attr_val.save()
        if str(attribute.type_field.type_name) == "<class 'list'>":
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_list = value
            attr_val.save()
        if str(attribute.type_field.type_name) == "<class 'dict'>":
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_dict = value
            attr_val.save()
        if str(attribute.type_field.type_name) == "<class 'tuple'>":
            attr_val = AttributeValue()
            attr_val.bookId = book
            attr_val.attributeId = attribute
            attr_val.attribute_value_dict = el_tup
            attr_val.save()

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

    for item in data_set['items']:
        book = get_new_book(item['id'], item['etag'], item['selfLink'])
        for attr_1 in item.items():
            parent_1 = get_attribute(attr_1[0], attr_1[1])
            for attr_2 in attr_1:
                if (type(attr_2) == dict):
                    for k, v in attr_2.items():
                        parent_2 = get_attribute(k, v, parent_1.id)
                        # print(book, parent_2.name, v)
                        if (type(v) == dict):
                            for i, j in v.items():
                                if type(j) == bool:
                                    new_attr = get_attribute(i, j, parent_2.id)
                        if (type(v) == list):
                            for el in v:
                                if (type(el) == dict):
                                    for g, h in el.items():
                                        new_attr = get_attribute(
                                            g, v, parent_2.id)
                                        # print(g, type(v))
                                        if (type(h) == dict):
                                            for a, b in h.items():
                                                new_attr = get_attribute(
                                                    a, b, new_attr.id)
                                                get_attr_value(
                                                    book, new_attr, b)
                                                print(new_attr, b)
                                        else:
                                            new_attr = get_attribute(
                                                g, h, parent_2.id)
                                            get_attr_value(
                                                book, new_attr, h)
                                if type(el) != dict and (type(el) != list):
                                    new_attr = get_attribute(
                                        parent_2.name, v, parent_1.id)
                                    get_attr_value(book, parent_2, el)
                                    # print(parent_2.name, v, parent_1.id)

                        if (type(v)) != dict and (type(v)) != list:
                            # print(book, parent_2.name, v)
                            # print(book, parent_2, v)
                            get_attr_value(book, parent_2, v)
                            # if str(v) == "authors":
                            #     print(v, type(v))
                else:
                    pass
                    # print(type(attr_2), attr_2)


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
