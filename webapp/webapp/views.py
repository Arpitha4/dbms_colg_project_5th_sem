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
    print("Logged out")
    return HttpResponseRedirect("/")
# end of logout page

# start of home page 
def home(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    return render(request, 'home.html')
# end of home page

#start of products
def product(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    return render(request, 'product.html')
# end of products

# start of cart page
def cart(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    return render(request, 'cart.html')
# end of cart page

# start of add to cart page
def add_to_cart(request,id):
    if request.user.is_authenticated:
        user_email = request.user.email
        cursor=connection.cursor()
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
    # return render(request, 'cart.html')
        for row in cursor:
<<<<<<< HEAD
    	    l={
    	        'id' : row[0],
    	        'quantity':row[1],
    	        'price' : row[2],
    	        'title' : row[3],
    	        'image':product.objects.get(id=row[0]).image
=======
    	    l=  {
    	    'id' : row[0],
    	    'quantity':row[1],
    	    'price' : row[2],
    	    'title' : row[3],
    	    'image':product.objects.get(id=row[0]).image
>>>>>>> 6532790974203d81aa7192362ce9c223c741d646
    	    }
    	    print(l["image"])
    	    total+=row[2]
    	    print(row)
    	    items.append(l)
    	    s_total=total+120
    	    context={
<<<<<<< HEAD
    	        'items':items,
    	        'total':total,
    	        'total_s':s_total
=======
    	    'items':items,
    	    'total':total,
    	    'total_s':s_total
>>>>>>> 6532790974203d81aa7192362ce9c223c741d646
    	    }
        

        return render(request, 'cart.html', context)
    else:
        return HttpResponseRedirect('/oauth/login/google-oauth2/?next=/cart')
# end of add to cart page

    

# end of cart function
# start of my_order page
def orders(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    return render(request, 'orders.html')
# end of cart page