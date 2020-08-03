from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import filters, viewsets
from books.models import *
from books.serializers import *
from books.functions import *
from django.core import serializers as ser


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'authors', 'published_date_year']
    ordering_fields = ['published_date_year']


class BooksAddPost(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        json_data = request.data
        save_in_db(json_data)
        books = Book.objects.all()
        books = ser.serialize('json', books)
        return HttpResponse(books, content_type="application/json")
