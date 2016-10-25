from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"user_app/index.html")
def register(request):
    if request.method == "POST":
        user1={
        'fname':request.POST['name'],
        'username':request.POST['username'],
        'password':request.POST['Password'],
        'cpassword':request.POST['cpassword'],
        'datehired':request.POST['datehired'],
        }
        user=User.objects.validate(user1)
        if user[0] == False:
            print "false"
            print_messages(request, user[1])
            return redirect('user:index')
        else:
            context={
            'msg':"you have successfully registered",
            }
            return render(request,"user_app/index.html",context)
    # else:
    #     return redirect('/')
def login(request):
    if request.method == "POST":

        user=User.objects.login(request.POST)
        # print type(user)
        if 'error' in user:
            print user['error']
            context={
                'errors':user['error']
            }
            return render(request,"user_app/index.html",context)
        else:

            request.session['name']=user['user'].name
            request.session['userid']=user['user'].id
        return redirect("belt:index")
def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)
