from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from apps.product.models import Product, ProductImage, ProductCategory, ProductReview
from django.http import JsonResponse
from apps.product.serializers import ProductSerializers
from apps.users.models import User
from django.contrib.auth.hashers import make_password



def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        users = User()
        users.user_role_id = 3
        users.first_name = first_name
        users.last_name = last_name
        users.email = email
        users.password = make_password(password)
        users.is_staff = False
        users.save()
        messages.success(request, 'Customer is register successfully.')
        return redirect('home.index')

    return render(request, 'frontends/register.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Customer is login successfully.')
            return redirect('home.index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home.login_user')

    return render(request, 'frontends/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('home.login_user')



def category(request, foo):
    foo = foo.replace('-',' ')
    
    category = ProductCategory.objects.get(name=foo)
    products = Product.objects.filter(categories=category)

    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'frontends/category.html', context)


def index(request):
    products = Product.objects.all()
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        productObj = Product.objects.get(id=int(product_id))
        product_Image = ProductImage.objects.filter(product=productObj).values()
        productSerializers = ProductSerializers(productObj)
        contextObj = {
            'product': productSerializers.data,
            'product_Image': list(product_Image)
        }
        return JsonResponse(contextObj)
    
    context = {
        "home_page": "active",
        "products": products,
    }
    return render(request, 'frontends/index.html', context)


def about(request):
    context = {"about_page": "active"}
    return render(request, 'frontends/about.html', context)



def product(request):
    productObj = Product.objects.all()
    context = {
        'product_results': productObj,
        "product_page": "active"
    }
    return render(request, 'frontends/product.html', context)


def productDetails(request, id):
    productObj = Product.objects.get(id=id)
    product_image = ProductImage.objects.filter(product=productObj)
    product_image1 = Product.objects.all()

    product_review = ProductReview.objects.all()

    context = {
        'productObj': productObj,
        'product_image': product_image,
        'product_image1':product_image1,
        'product_review': product_review,
    }
    return render(request, 'frontends/product-detail.html', context)



def shopCart(request):
    return render(request, 'frontends/shoping-cart.html')

def contacts(request):
    context = {"contact_page": "active"}
    return render(request, 'frontends/contact.html', context)


def product_review(request):
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        review = request.POST.get('review')
        rating = int(request.POST.get('rating'))

        product = get_object_or_404(Product, id=product_id)

        product_review = ProductReview()
        product_review.product = product
        product_review.user = product.user
        product_review.description = review
        product_review.rating = rating
        product_review.save()

        context = {
            'SUCCESS': 'Save'
        }

        response = JsonResponse(context)
        return response
    