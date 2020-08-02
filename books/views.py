from django.shortcuts import render
from .forms import LinkForm
from django.views import View
import requests
from .models import *
from .function import get_data
# Create your views here.


class DBView(View):
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
                result = "Not connection"
                status = None
            if status == 200:
                get_data(link)
        else:
            result = None
        ctx = {'result': result}
        return render(request, 'books/db_data.html', ctx)
