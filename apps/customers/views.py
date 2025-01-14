from django.shortcuts import render
from apps.users.models import User
from django.core.paginator import Paginator



SINGULAR_NAME = "Customer"
PLURAL_NAME = "Customers"


def index(request):
    DB = User.objects.filter(user_role_id=3, is_active=True)

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
    return render(request, 'customers/index.html', context)
