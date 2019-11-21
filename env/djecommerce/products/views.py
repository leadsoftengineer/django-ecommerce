#KYIV MEDIA 19.11.19
from django.shortcuts import render,get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form":my_form
#     }
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     #print(request.POST)
#     if request.method =="POST":
#      my_new_title=request.POST.get('title')
#      print(my_new_title)
#      #Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
     form = ProductForm(request.POST or None)
     if form.is_valid():
         form.save()

     context ={
               'form': form
     }
     return render(request,"products/product_create.html", context)
# Create your views here.
def product_detail_view(request):
     obj = Product.objects.get(id=1)
     context ={
         #'title':obj.title,
         #'description':obj.description

         'object': obj
     }
     return render(request,"products/product_detail.html", context)

# Create view with initial data
def product_initial_data(request):

    initial_data={
         'title': "This is awesome title"

    }
    obj = Product.objects.get(id=1)

    form= RawProductForm(request.POST or None, initial=initial_data)
    context={
        'form':form
    }
    return  render(request, "products/product_create.html",context)
# Create dynamic_lookup_view
def dynamic_lookup_view(request,my_id):
    obj = get_object_or_404(Product,id=my_id)
    context ={
        "object":obj
    }
    return render(request, "products/product_detail.html", context)

# Create a product_delete_view
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        #confirming delete
        obj.delete()
    context={
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

# Create a product_list_view
def product_list_view(request):
    #list of objects
    queryset = Product.objects.all()
    context ={
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)
