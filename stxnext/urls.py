from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import DBLoadView, SearchBookView, BookDetailsView
from books.views_api import *


router = routers.DefaultRouter()
router.register(r'books', BooksViewSet, basename="books"),
# router.register(r'book_attrs', BookAttrsViewSet, basename="book_attrs"),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('books/<int:pk>', BookDetailsView.as_view(), name="book_details"),
    path('load_data/', DBLoadView.as_view(), name="db_load"),
    path('db/', BooksAddPost.as_view(), name="db"),
    path('test/', SearchBookView.as_view(), name="text"),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
