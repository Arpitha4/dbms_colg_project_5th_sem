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
        cursor = connection.cursor()
        #cursor.execute(
         #   "select pid_id,quantity,price from cart where bid_id='"+user_email+"';")
        #query = "select * from buyer where b_email='"+user_email+"';"
        #user = len(list(buyer.objects.raw(query)))
        #cursor = connection.cursor()
        #query = "select * from buyer where b_email='"+user_email+"';"
        # user = len(list(buyer.objects.raw(query)))
        # cursor=connection.cursor()
        # if(user == 0):
        #     cursor.execute("insert into buyer values('" +user_email+"','"+request.user.username+"','null')")
    #     products=product.objects.all()
    #     context={
    #         'products':products
    #     }
    # else:
    #     products=product.objects.all()
    #     context={
    #         'products':products
    # }
    return render(request, 'sell.html')
    
# end of sell function

