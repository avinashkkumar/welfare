from django.shortcuts import render,redirect
from django.views import View
# Create your views here.


class land(View):
    def get(self,request,*args, **kwargs):
        return render(request, "home/index.html")

