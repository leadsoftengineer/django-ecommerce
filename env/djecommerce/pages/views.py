from django.http import HttpResponse
from django.shortcuts import render

# KYIV MEDIA 15.11.2019
# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})
def contact_view(*args,**kwargs):
    return HttpResponse("<h1>Contact</h1>")
def about_view(request,*args,**kwargs):
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list":[1,2,3,4,5,6,7,8,9],
        "title":"django e-commerce"
    }
    return  render(request, "about.html", my_context)
