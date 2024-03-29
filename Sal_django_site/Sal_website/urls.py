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
# from django.conf.urls import patterns, include, url
from django.views.i18n import JavaScriptCatalog
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from main.tokens import user_tokenizer
from main import views

urlpatterns = [
    path('', include('main.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),#???? namespace='drf' is mandatory
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    # {'document_root', settings.STATIC_ROOT})



    # path('admin/', include('admin.site.urls')),
    
]

# if settings.DEBUG:
#     urlpatterns = patterns('',
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     url(r'', include('django.contrib.staticfiles.urls')),
# ) + urlpatterns