from django.shortcuts import render

# Create your views here.
def Commoncode(request):
    return render(request , 'shop/base.html')
def home(request):
    return render(request , 'shop/home.html')

def Cart(request):
    return render(request , 'shop/cart.html')

def Product_detail(request):
    return render(request , 'shop/product-details.html')

def Checkout(request):
    return render(request , 'shop/checkout.html')

def Blog_detail(request):
    return render(request , 'shop/blog.html')

def Errors(request):
    return render(request , 'shop/404.html')

def Contact(request):
    return render(request , 'shop/contact-us.html')

def Tracking(request):
    return render(request , 'shop/tracking.html')


def Profiles(requset):
    return render(requset, 'shop/my_profile.html')
    


def login(request):
    return render(request , 'shop/login.html')

def Register(request):
    return render(request , 'shop/register.html')

def Forget_password(request):
    return render(request , 'shop/forget-password.html')

def Product(request):
    return render(request , 'shop/shop.html')

def Product_two(requset):
    return render(requset , 'shop/shop-two.html')

def Product_three(request):
    return render(request, 'shop/shop-three.html')    