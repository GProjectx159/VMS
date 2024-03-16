from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from .models import User

@login_required(login_url='base:login')
def home(request):
 return render(request, "home.html", {})

def loginUser(request):
    form = None
    if request.user.is_authenticated:
        return redirect('base:home')

    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.active: 
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('base:home')
            else:
                error_message = 'اسم المستخدم او كلمة المرور خطأ'
                submitted_data = request.POST.copy() 
                submitted_data['username'] = request.POST.get('username')
                submitted_data['password'] = request.POST.get('password')
                form = MyUserCreationForm(submitted_data)

        elif user is not None and not user.active:
            error_message = 'حسابك لم ينشط بعد اتصل بالدعم'
            submitted_data = request.POST.copy() 
            submitted_data['username'] = request.POST.get('username')
            submitted_data['password'] = request.POST.get('password')
            form = MyUserCreationForm(submitted_data)

        else:
            error_message = 'اسم المستخدم او كلمة المرور خطأ'
            submitted_data = request.POST.copy() 
            submitted_data['username'] = request.POST.get('username')
            submitted_data['password'] = request.POST.get('password')
            form = MyUserCreationForm(submitted_data)

    return render(request, 'registration/login.html', {'form':form , 'error_message': error_message})

def sginup(request):
    error_messages = None
    
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:login")
        else:
            error_messages = form.errors
            submitted_data = request.POST.copy() 
            submitted_data['name'] = request.POST.get('name')  
            submitted_data['username'] = request.POST.get('username')
            submitted_data['email'] = request.POST.get('email')
            submitted_data['password1'] = request.POST.get('password1')
            submitted_data['password2'] = request.POST.get('password2')
            submitted_data['employee_identity'] = request.POST.get('employee_identity')
            submitted_data['startwork_date'] = request.POST.get('startwork_date')
            submitted_data['phone'] = request.POST.get('phone')
            submitted_data['department'] = request.POST.get('department')
            form = MyUserCreationForm(submitted_data)
    else:
        form = MyUserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form, "error_messages": error_messages})

def logoutUser(request):
    logout(request)
    return redirect("base:login")