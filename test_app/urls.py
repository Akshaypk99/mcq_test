from django.urls import path,include
from . import views  
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.loginPage,name='loginpage'),
    path('logout/', views.logoutUser, name='logout'),
]