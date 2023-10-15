from django.shortcuts import render,redirect
from logapp.models import register_db
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login
# from django.contrib import messages


# Create your views here.
def log_page(req):
    return render(req,'login.html')


def save_regdb(request):
    if request.method=="POST":
        na = request.POST.get('name')
        mail = request.POST.get('email')
        pas = request.POST.get('pass')
        obj=register_db(uname=na,uemail=mail,upass=pas,)
        obj.save()
        return redirect(log_page)



def userlogin(req):
    if req.method=="POST":
        uname = req.POST.get('username')
        pwd = req.POST.get('password')
        if register_db.objects.filter(uname=uname,upass=pwd).exists():
            req.session['username']=uname
            req.session['password']=pwd
            return redirect(home_page)

        else:
            return redirect(log_page)

    return redirect(log_page)


def home_page(req):
    return render(req,'home.html')
