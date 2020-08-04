from rest_framework import serializers
from books.models import *


# class AuthorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = [
#             'author',
#         ]


# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = [
#             'category',
#         ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        depth = 1
        fields = [
            'book_id',
        ]