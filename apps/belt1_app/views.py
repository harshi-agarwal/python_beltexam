from django.shortcuts import render,redirect
from ..user_app .models import User
from .models import Product
from django.contrib import messages
# Create your views here.
def index(request):
    context={
    'msg': "redirected from add item also",
    'products':Product.objects.all(),
    'user':User.objects.get(id=request.session['userid'])
    }
    return render(request,"belt1_app/index.html",context)
def additem(request):
    if request.method == "POST":
        user=User.objects.get(id=request.session['userid'])
        valid=Product.objects.validate_product(request.POST,user)
        if valid[0] == False:
            print "false"
            print_messages(request, valid[1])
            return redirect('belt:additem')
        else:
            return redirect('belt:index')
    else:
        return render(request,"belt1_app/additem.html")
def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)
def addtowishlist(request,id):
    this_product=Product.objects.get(id=id)
    this_user=User.objects.get(id=request.session['userid'])
    this_product.join.add(this_user)
    return redirect('belt:index')
def removefromwishlist(request,id):
    this_product=Product.objects.get(id=id)
    this_user=User.objects.get(id=request.session['userid'])
    this_product.join.remove(this_user)
    return redirect('belt:index')
def deleteprod(request,id):
    this_product=Product.objects.get(id=id)
    this_product.delete()
    return redirect('belt:index')
def logout(request):
    request.session.clear()
    return redirect('user:index')
def goback(request):
    return redirect('belt:index')
def show_product(request,id):
    context={
    'prods':Product.objects.get(id=id)

    }
    return render(request,"belt1_app/show.html",context)
