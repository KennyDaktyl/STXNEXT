from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import admin
from django.urls import path, include
from books.models import *
from books.views import DBView
from django.contrib.auth.models import User
from rest_framework import filters, routers, serializers, viewsets, generics
# from django_filters.rest_framework import DjangoFilterBackend


# Serializers define the API representation.
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = [
            'author',
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        depth = 1
        fields = [
            'id', 'title', 'authors', 'categories', 'published_date_year',
            'average_rating', 'ratings_count', 'thumbnail'
        ]


# ViewSets define the view behavior.
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'authors', 'published_date_year']
    ordering_fields = ['published_date_year']


# class BooksSearch(APIView):
#     @classmethod
#     def get_extra_actions(cls):
#         return []

#     def get(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
router = routers.DefaultRouter()
router.register(r'books', BooksViewSet, basename="books"),
# router.register(r'db', BooksSearch, basename="search_books")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('db/', DBView.as_view(), name="db_load"),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
