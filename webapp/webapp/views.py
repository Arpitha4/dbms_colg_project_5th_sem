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
    if request.user.is_authenticated:
        products = product.objects.all()
        cursor = connection.cursor()
        # print(products)
        context={
            "products":products,
        }
        return render(request,"product.html",context)
    else:
        return HttpResponseRedirect('/oauth/login/google-oauth2') 
# end of all products 

# start of add_to _cart in db
def add_to_cart(request, id):
    if request.user.is_authenticated:
        products = product.objects.get(id=id)
        cursor = connection.cursor()
        user_email = request.user.email
        p_id = str(products.id)
        query = "select * from cart where bid_id='"+user_email+"' and pid_id="+p_id
        c = len(list(cart.objects.raw(query)))
        if(c == 0):
            bid = buyer.objects.get(b_email=request.user.email)
            added = cart(pid=products, bid=bid,price=products.price, sid=products.sid, quantity=1)
            added.save()
            # cursor.callproc("add_to_cart",[product_now.id,user_email,product_now.price,product_now.s_id_id])
        else:
            # print("enters else")
            cursor.execute("update cart set quantity=quantity+1 where pid_id=" + p_id+" and bid_id='"+user_email+"';")
            cursor.execute("update cart set price="+str(products.price) + "*quantity where pid_id="+p_id+" and bid_id='"+user_email+"';")

        return HttpResponseRedirect('/products')
    else:
        # print('enterd else')
        return HttpResponseRedirect('/oauth/login/google-oauth2/?next=/add_to_cart/product/'+id)
# end of add_to_cart

# start of cart page with products from db
def cartpage(request):
    cart_items = []
    if request.user.is_authenticated:
        user_email = request.user.email
        # products = product.objects.get(id=id)
        cursor = connection.cursor()
        # p_id = str(products.id)
        # query = "select * from cart where bid_id='"+user_email+"' and pid_id="+p_id
        query = "select * from buyer where b_email='"+user_email+"';"
        user = len(list(buyer.objects.raw(query)))
        cursor = connection.cursor()
        if(user == 0):
            cursor.execute("insert into buyer values('" + user_email+"','"+request.user.username+"','null')")
        # cursor.execute( "select pid_id,quantity, price from cart where bid_id='"+user_email+"';")
        
        total = 0
        cursor = cart.objects.filter(bid = request.user.email)
        for row in cursor:
            print(row)
            # products=product.objects.get(id=row[0])
            l={
                'id':row.pid.id,
                'title':row.pid.title,
                # 'quantity': row[1],
                'price':row.pid.price,
            }
            total += row.pid.price
            cart_items.append(l)
        print(total)    
        print(len(cart_items))
        context= {
            'cart_items':cart_items,
            'total':total
        }
        if(len(cart_items)==0):
            return render(request, 'cart.html') 
        else:    
            return render(request, 'cartpage.html',context)
    else:
        if(len(cart_items)==0):
            return render(request, 'cart.html') 
        return render(request, 'cart.html') 
# end of cart page

# start of remove cart function
def remove_cart(request, id):
    user_email = request.user.email
    cursor = connection.cursor()
    cursor.execute("delete from cart where bid_id='" + user_email+"' and pid_id="+str(id)+";")
    response = redirect('/cartpage')
    return response
# end of remove cart function


# start of my_order page
def orders(request):
    # if request.user.is_authenticated:
    #     user_email = request.user.email
    return render(request, 'orders.html')
# end of cart page

# start of address_form
def address_form(request):
    return render(request,'address_form.html')
# end of address_form

# start of adding address
def add_address(request):
    if request.user.is_authenticated:
        user_email = request.user.email
        print(request.POST)
        address1 = address(
            bid=buyer.objects.get(b_email=user_email),
            phno=request.POST['phone'],
            name=request.POST['name'],
            address=request.POST['address'],
            
        )
        address1.save()

        buyer1 = buyer(
            b_phno=request.POST['phone'],
            b_name=request.POST['name'],
        )
        buyer1.save()
        # cursor.execute("insert into address values('" + user_email+"','"+request.user.username+"','null')")
        return redirect('/buyer_tq')
# end of adding address

# start of thank you page
def buyer_tq(request):
    return render(request,'buyer_tq.html')
# end of thank you page