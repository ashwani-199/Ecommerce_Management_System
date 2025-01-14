from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from apps.orders.models import Order, OrderItem, OrderHistory
from django.contrib import messages


SINGULAR_NAME = "Order"
PLURAL_NAME = "Orders"

@login_required(login_url='login')
def index(request):
    DB = Order.objects.filter().order_by('-id')
    
    totalRecord = DB.count()
    paginator = Paginator(DB, 2)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
        'totalRecord': totalRecord,
        'users_obj': DB,
        'singular_name': SINGULAR_NAME,
        'plural_name': PLURAL_NAME,
    }
    return render(request, 'orders/index.html', context)

# @login_required(login_url='login')
# def addProduct(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST or None)
#         formSet = ImageForm(request.POST,  request.FILES)
#         if form.is_valid() and formSet.is_valid():
#             formData = formSet.cleaned_data
#             image = formData.get("image")
#             product = Product()
#             product.user = request.user
#             product.categories =form.cleaned_data["categories"]
#             product.name = form.cleaned_data["name"]
#             product.description = form.cleaned_data["description"]
#             product.price = form.cleaned_data["price"]
#             product.brand_name = form.cleaned_data["brand_name"]
#             product.save()

#             productImage = ProductImage()
#             productImage.product = product
#             productImage.image = image
#             productImage.save()
#             return redirect("product.index")

#     else:
#         form = ProductForm()
#         formSet = ImageForm()
#     context = {
#         "form": form,
#         'formSet':formSet,
#         'singular_name': SINGULAR_NAME,
#         'plural_name': PLURAL_NAME,
#     }
#     return render(request, 'product/add.html', context)

# @login_required(login_url='login')
# def edit(request, id):
#     product = Product.objects.get(id=id)
#     product_image = ProductImage.objects.filter(product=product)
#     if not product:
#         return redirect('product.index')
#     initialDict = {
#         "name": product.name,
#         "description": product.description,
#         "price": product.price,
#         "brand_name": product.brand_name,
#         "categories": product.categories
#     }
#     form = ProductForm(initial=initialDict)
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "you are now logged in")
#             return redirect('product.index')

#     context = {
#         'form': form,
#         'product_data': product,
#         'product_image':product_image,
#         'singular_name': SINGULAR_NAME,
#         'plural_name': PLURAL_NAME,
#     }
#     return render(request, 'product/edit.html', context)


# @login_required(login_url='login')
# def view(request, id):
#     product = Product.objects.get(id=id)
#     product_image = ProductImage.objects.filter(product=product)

#     if not product:
#         return redirect('product.index')

#     context = {
#         'product_data': product,
#         'product_image':product_image,
#         'singular_name': SINGULAR_NAME,
#         'plural_name': PLURAL_NAME,
#     }

#     return render(request, 'product/view.html', context)


# @login_required(login_url='login')
# def delete(request, id):
#     product = Product.objects.get(id=id)
#     if not product:
#         return redirect('product.index')
#     product.delete()
#     return redirect('product.index')



# @login_required(login_url='login')
# def addCategory(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST or None)
#         if form.is_valid():
#             product_category = ProductCategory()
#             product_category.name = form.cleaned_data["name"]
#             product_category.save()
#             return redirect("product.index")

#     else:
#         form = CategoryForm()
#     context = {
#         "form": form,
#         'singular_name': 'Category',
#         'plural_name': 'Categories',
#     }
#     return render(request, 'product/category.html', context)