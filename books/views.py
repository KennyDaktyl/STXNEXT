from django.shortcuts import render
from .forms import LinkForm
from django.views import View
import requests
from .models import *
from .functions import *
import json
from django.http import HttpResponse


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
                get_new_data(link)
        else:
            result = None
        ctx = {'result': result}
        return HttpResponse(json.dumps(result, indent=4), content_type="application/json")


# class BookDetailsView(View):
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         book = get_book(book)
#         result = json.dumps(book, indent=3)
#         ctx = {'result': result}
#         return render(request, 'books/db_data.html', ctx)
