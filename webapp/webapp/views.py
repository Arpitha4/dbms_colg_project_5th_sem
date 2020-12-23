from django.shortcuts import render
from django.shortcuts import redirect
import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
from django.contrib.auth import logout
from django.db import connection
from django.shortcuts import render, redirect,get_object_or_404
# Create your views here.

# start of logout
def logout_app(request):
    logout(request)
    return HttpResponseRedirect("/")
# end of logout page

# start of home page 
def home(request):
    if request.user.is_authenticated:
        user_email=request.user.email
        query="select * from buyer where b_email='"+user_email+"';"
        user = len(list(buyer.objects.raw(query)))
        cursor=connection.cursor()
        if(user == 0):
            cursor.execute("insert into buyer values('" + user_email+"','"+request.user.username+"','null')")
        cursor = connection.cursor()
    return render(request, 'home.html')
  
# end of home page
        
# start of all products
def all_products(request):
    products = product.objects.all()
    #products=product.objects.get(id=id)
    cursor = connection.cursor()
    print(products)
    context={
        "products":products,
    }
    return render(request,"product.html",context)

# end of all products 

# start of adding products to cart
# def add_to_cart(request,id):
#     if request.user.is_authenticated:
#         user_email = request.user.email
#         products = product.objects.get(id=id)
#         cursor = connection.cursor()
#         p_id = str(product_now.id)
#         query = "select * from cart where bid_id='"+user_email+"' and pid_id="+p_id
#         c = len(list(cart.objects.raw(query)))
#         if(c == 0):
#             bid = buyer.objects.get(b_email=request.user.email)
#     else:
#         return HttpResponseRedirect('/oauth/login/google-oauth2')  
# end of adding products to cart

# start of cart page
def cart(request):
    # if request.user.is_authenticated:
        # user_email = request.user.email
    return render(request, 'cart.html')
# end of cart page

# start of cart page
def cartpage(request):
    if request.user.is_authenticated:
        # user_email = request.user.email
        return render(request, 'cartpage.html')
# end of cart page

# start of my_order page
def orders(request):
    if request.user.is_authenticated:
        user_email = request.user.email
        return render(request, 'orders.html')
# end of cart page

# start of address_form
def address_form(request):
    return render(request,'address_form.html')
