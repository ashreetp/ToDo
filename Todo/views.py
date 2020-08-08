from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import List,User
from django.contrib import messages
from werkzeug.security import generate_password_hash,check_password_hash
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        try:
            passwordobj = User.objects.filter(username=name).values()
            print('ok => ',passwordobj[0]['password'])
            if check_password_hash(passwordobj[0]['password'],password):
                request.session['login']=True
                request.session['username'] = name
                return redirect('/todopage')
            else:
                messages.add_message(request, messages.INFO,'Please check your username and password and try again')
        except:
            messages.add_message(request, messages.INFO,'No User Found')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['password']
        password = generate_password_hash(password)
        try:
            model_instance = User(username=name,password=password)
            model_instance.save()
            return redirect('/login')
        except:
            messages.add_message(request, messages.INFO,'No')
    return render(request,'register.html')

def logout(request):
    request.session['login']=False
    return redirect('/')

def updatelogin(request):
    if request.method=='POST':
        password = request.POST['password']
        password = generate_password_hash(password)
        User.objects.filter(username=request.session['username']).update(password = password)
        return redirect('/')
    return render(request,'updatelogin.html')

def delete(request):
    User.objects.filter(username=request.session['username']).delete()
    List.objects.filter(username=request.session['username']).delete()
    request.session['login'] = False
    request.session['username'] = ''
    return redirect('/')


def todopage(request):
    obj = List.objects.filter(username=request.session['username']).values()
    if request.method == 'POST':
        desc = request.POST['description']
        model_instance = List(username=request.session['username'],description=desc)
        model_instance.save()
    return render(request,'todopage.html', {'obj':obj} )

def updatepost(request,id):
    obj=List.objects.filter(id=id).values()
    if request.method == 'POST':
        desc = request.POST['description']
        List.objects.filter(id = id).update(description = desc)
        return redirect('/todopage')
    return render(request,'updatepage.html',{'obj': obj})

def deletepost(request,id):
    List.objects.filter(id=id).delete()
    return redirect('/todopage')