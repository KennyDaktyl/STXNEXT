from django.shortcuts import render
from .forms import LinkForm
from django.views import View
import requests
from .models import *
from .functions import get_data
import json
from django.http import HttpResponse

# Create your views here.


class DBLoadView(View):
    def get(self, request):
        form = LinkForm()
        ctx = {
            'form': form,
        }
        return render(request, 'books/db_load.html', ctx)

    def post(self, request):
        form = LinkForm(request.POST)
        if form.is_valid():
            link = request.POST.get("link")
            try:
                data = requests.get(link)
                status = data.status_code
                result = data.json()
            except:
                result = "No data in link"
                status = None
            if status == 200:
                get_data(link)
        else:
            result = None
        ctx = {'result': result}
        return render(request, 'books/db_data.html', ctx)


class SearchBookView(View):
    def post(self, request):
        q = request.POST.get("q")
        books = Book.objects.filter(titile__icontains=q)
        return HttpResponse(json.dumps(books), content_type="application/json")
