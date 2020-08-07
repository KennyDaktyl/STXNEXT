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
    filterset_fields = ['title', 'authors', 'publishedDate']
    ordering_fields = ['publishedDate']


class BooksAddPost(APIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        json_data = request.data
        q = json_data['q']
        books = Book.objects.filter(title__icontains=json_data['q'])
        books = serializers.serialize('json', list(books))
        return HttpResponse(books, content_type="application/json")
