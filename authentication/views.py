from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.
class HomeView(View):
    template_name = 'authentication/home.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = {
            'user': request.user if request.user.is_authenticated else ''
        }
        return render(request, self.template_name, context)
    
class RegisterView(View):
    template_name = 'authentication/register.html'
    success_url = 'authentication:login'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            print("Username taken!")
            return redirect('authentication:register')

        if User.objects.filter(email=email).exists():
            print("Email already exists!")
            return redirect('authentication:register')
        
        if password1 != password2:
            print("Passwords don't match!")
            return redirect('authentication:register')

        new_user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        print(f"User '{new_user.username}' created")
        return redirect(self.success_url)

class LoginView(View):
    referer = []
    template_name = 'authentication/login.html'
    success_url = 'notes:index'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = {}
        if request.GET != {}: 
            self.referer.append(request.GET['next'])
        else:
            pass
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        email_or_username = request.POST['email_or_username']
        password = request.POST['password']

        if User.objects.filter(username=email_or_username).exists():
            user = User.objects.get(username=email_or_username)
        elif User.objects.filter(email=email_or_username).exists():
            user = User.objects.get(email=email_or_username)
        
        user_object = authenticate(username=user.username, password=password)
        login(request, user)
        print("Logged in")

        if len(self.referer) == 0:
            return redirect(self.success_url)
        else:
            return redirect(self.referer[0])

class LogoutView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        logout(request)
        return redirect('authentication:home')
    
home = HomeView.as_view()
register = RegisterView.as_view()
login_view = LoginView.as_view()
logout_view = LogoutView.as_view()