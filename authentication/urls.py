from django.urls import path
from authentication.views import home, register, login_view, logout_view

app_name = 'authentication'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout_view')
]