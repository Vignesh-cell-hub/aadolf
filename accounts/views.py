from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import auth

# Create your views here.

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("login")
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect("/")
        else:
            return render(request, 'accounts/loginpage.html',{'invalid':'invalid'})
    else:
        return render(request, 'accounts/loginpage.html')


def logoutuser(request):
    auth.logout(request)
    return render(request, 'accounts/loginpage.html')