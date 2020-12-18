from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
from django.contrib.auth import logout
from django.db import connection
from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import redirect
import requests
from django.conf import settings

# Create your views here.

# start of logout
def logout_app(request):
    logout(request)
    print("Logged out")
    return HttpResponseRedirect("/")
# end of logout page

# start of sell_logout
def logout_sell(request):
    logout(request)
    print("Logged out")
    return HttpResponseRedirect("/sell")
    
# end of logout page

# start of home page 
def home(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    return render(request, 'home.html')
# end of home page

# start of sell
def sell(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    
    return render(request, 'sell.html')
    
# end of sell function

def cart_page(request):
    if request.user.is_authenticated:
        user_email = request.user.email
        cursor = connection.cursor()
        query = "select * from buyer where b_email='"+user_email+"';"
        user = len(list(buyer.objects.raw(query)))
        cursor = connection.cursor()
        if(user == 0):
            cursor.execute("insert into buyer values('" +
                           user_email+"','"+request.user.username+"','null')")
        cursor.execute(
            "select pid_id,quantity,price from cart where bid_id='"+user_email+"';")
        cart_items = []
        total = 0
        categories_now = []
        for row in cursor:
            print(row)
            product_now = product.objects.get(id=row[0])
            l = {
                'id': row[0],
                'quantity': row[1],
                'price': row[2],
                'title': product_now.title,
                'image': product_now.first_photo
            }
            print(l["image"])
            total += row[2]
            print(row)
            cart_items.append(l)
            categories_now.append(product_now.category)
        recommended_products_list = []
        recommended_prod = recommended_products.objects.all()
        recommended_products_list = [i.pid for i in recommended_prod]
        num_items = len(cart_items)
        user_address = address.objects.filter(bid=request.user.email)
        addr_len = len(list(address.objects.filter(bid=request.user.email)))

        context = {
            'cart_items': cart_items,
            'total': total,
            'user_address': user_address,
            'addr_len': addr_len,
            'num_items': num_items,
            "recommended_products": recommended_products_list
        }

        return render(request, 'cart.html', context)
    else:
        return HttpResponseRedirect('/oauth/login/google-oauth2/?next=/cart')

