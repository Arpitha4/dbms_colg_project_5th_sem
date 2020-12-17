from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
from django.contrib.auth import logout
from django.db import connection
from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import redirect

# Create your views here.

# start of login
# def login(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = authenticate(
#                 username=form.cleaned_data.get('username'),
#                 password=form.cleaned_data.get('password')
#             )
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
# end of login

# start of logout
def logout(request):
    logout(request)
    return HttpResponseRedirect("/")
# end of logout page

# start of home page 
def home(request):
    if request.user.is_authenticated:
        user_email = request.user.email
        query = "select * from buyer where b_email='"+user_email+"';"
        user = len(list(buyer.objects.raw(query)))
        if(user == 0):
            cursor.execute("insert into buyer values('" +
                           user_email+"','"+request.user.username+"','null')")
    #     products=product.objects.all()
    #     context={
    #         'products':products
    #     }
    # else:
    #     products=product.objects.all()
    #     context={
    #         'products':products
    # }
    return render(request, 'home.html')
# end of home page

# start of sell
# def sell(request):
   
# end of sell function

