"""Sal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url, include
from main import views

urlpatterns = [
    path('', include('main.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('confirm-email/<str:user_id>/<str:token>/', views.ConfirmRegistrationView.as_view(), name='confirm_email'),


    # path('admin/', include('admin.site.urls')),
    
]
