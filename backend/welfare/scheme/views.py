from django.shortcuts import render,redirect
from django.views import View

# Create your views here.

class schemes(View):
    def get(self, request, *args, **kwargs):
        return render(request, "scheme/scheme_list.html")




class scheme_detail(View):
    def get(self, request, *args, **kwargs):
        return render(request, "scheme/scheme_details.html")