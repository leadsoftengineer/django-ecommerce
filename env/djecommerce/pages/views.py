from django.http import HttpResponse
from django.shortcuts import render

# KYIV MEDIA 15.11.2019
# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})
def contact_view(*args,**kwargs):
    return HttpResponse("<h1>Contact</h1>")
def about_view(*args,**kwargs):
    return HttpResponse("<h1>About</h1>")