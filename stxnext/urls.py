from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import DBLoadView, SearchBookView
from books.views_api import *


router = routers.DefaultRouter()
router.register(r'books', BooksViewSet, basename="books"),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('load_data/', DBLoadView.as_view(), name="db_load"),
    path('db/', BooksAddPost.as_view(), name="db"),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
