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

# start of my_order page
def orders(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    return render(request, 'orders.html')
# end of cart page