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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy, include
from django.conf.urls import url, include
from django.views.i18n import JavaScriptCatalog
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from .tokens import user_tokenizer
from django.contrib.auth.tokens import default_token_generator
from .views import contactView, successView, volunteerView



urlpatterns = [
    path("", views.homepage, name="homepage"),
    # path("signup", views.signup, name="signup"),
    # path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name="logout"),
    # path("reset-password-confirmation", views.reset_confirmation_sent, name='password_reset_confirm_sent'),
    # path("email-test1", views.email_test1, name="email-test1"),
    # path("email-test2", views.email_test2, name="email_test2"),
    # path('confirm-email', views.account_activation_sent, name='confirm_email_sent'),
    # path('map_page', views.map_page, name='map_page'),
    # path('profile-edit', views.profile_edit, name='profile_edit'),
    # path('profile-view', views.profile_view, name='profile-view'),
    # path('my-posts', views.my_posts, name='my-posts'),
    # path('new-dpost', views.new_dpost, name='new_dpost'),
    # path('new-rpost', views.new_rpost, name='new_rpost'),
    # path('my-account', views.my_account, name='my_account'),
    # path('contact', contactView, name='contact'),
    # path('success', successView, name='success'),
    # path('volunteer', volunteerView, name='volunteer'),

    # path('<single_slug>/delete/', views.delete, name='delete'),
    # path('<single_slug>/edit-rpost/', views.edit_rpost, name='edit-rpost'),
    # path('<single_slug>/edit-dpost/', views.edit_dpost, name='edit-dpost'),
    # path("<single_slug>", views.single_slug, name="single_slug"),



    path('confirm-email/<str:user_id>/<str:token>/', views.ConfirmRegistrationView.as_view(), name='confirm_email'),
    
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='main/reset_password.html',
      html_email_template_name='main/reset_password_email.html',
      success_url=settings.LOGIN_URL,
      token_generator=default_token_generator),
      name='reset_password'),
    
    path(
        'reset-password-confirmation/<str:uidb64>/<str:token>/',
        auth_views.PasswordResetConfirmView.as_view(
        template_name='main/reset_password_update.html', 
        post_reset_login=True,
        post_reset_login_backend='django.contrib.auth.backends.ModelBackend',
        token_generator=default_token_generator,
        success_url=settings.LOGIN_REDIRECT_URL),
        name='password_reset_confirm'),


    path("signup/", views.signup, name="signup"),
    # url(r'^signup$', RedirectView.as_view(url = 'signup/')),
    
    path("login/", views.login_request, name="login"),
    # url(r'^login$', RedirectView.as_view(url = 'login/')),
    
    path("logout/", views.logout_request, name="logout"),
    # url(r'^logout$', RedirectView.as_view(url = '/logout/')),
    
    path("reset-password-confirmation/", views.reset_confirmation_sent, name='password_reset_confirm_sent'),
    # url(r'^reset-password-confirmation$', RedirectView.as_view(url = '/reset-password-confirmation/')),
    
    path("email-test1/", views.email_test1, name="email-test1"),
    # url(r'^email-test1$', RedirectView.as_view(url = '/email-test1/')),
    
    path("email-test2/", views.email_test2, name="email_test2"),
    # url(r'^email-test2$', RedirectView.as_view(url = '/email-test2/')),
    
    path('confirm-email/', views.account_activation_sent, name='confirm_email_sent'),
    # url(r'^confirm-email$', RedirectView.as_view(url = '/confirm-email/')),
    
    path('map_page/', views.map_page, name='map_page'),
    # url(r'^map_page$', RedirectView.as_view(url = 'map_page/')),
    
    path('profile-edit/', views.profile_edit, name='profile_edit'),
    # url(r'^profile-edit$', RedirectView.as_view(url = '/profile-edit/')),
    
    path('profile-view/', views.profile_view, name='profile_view'),
    # url(r'^profile-view$', RedirectView.as_view(url = '/profile-view/')),
    
    url('my-posts/', views.my_posts, name='my-posts'),
    # url(r'^my-posts', RedirectView.as_view(url = '/my-pos')),
    
    path('new-dpost/', views.new_dpost, name='new_dpost'),
    # url(r'^new-dpost$', RedirectView.as_view(url = 'new_dpost/')),
    
    path('new-rpost/', views.new_rpost, name='new_rpost'),
    # url(r'^new-rpost$', RedirectView.as_view(url = 'new-rpost/')),
    
    path('my-account/', views.my_account, name='my_account'),
    # url(r'^my-account$', RedirectView.as_view(url = '/my-account/')),
    
    path('contact/', contactView, name='contact'),
    # url(r'^contact$', RedirectView.as_view(url = '/contact/')),
    
    path('success/', successView, name='success'),
    # url(r'^success$', RedirectView.as_view(url = '/success/')),
    

    path('volunteer/', volunteerView, name='volunteer'),
    # url(r'^volunteer$', RedirectView.as_view(url = '/volunteer/')),
    
    
    path('<single_slug>/delete/', views.delete, name='delete'),
    # url(r'^<single_slug>/delete$', RedirectView.as_view(url = '/<single_slug>/delete/')),
    
    path('<single_slug>/edit-rpost/', views.edit_rpost, name='edit-rpost'),
    # url(r'^<single_slug>/edit-rpost$', RedirectView.as_view(url = '/<single_slug>/edit-rpost/')),
    
    path('<single_slug>/edit-dpost/', views.edit_dpost, name='edit-dpost'),
    # url(r'^<single_slug>/edit-dpost$', RedirectView.as_view(url = '/<single_slug>/edit-dpost/')),
    
    path("<single_slug>/", views.single_slug, name="single_slug"),
    # url(r'^<single_slug>$', RedirectView.as_view(url = '/<single_slug>/')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# If you already have a js_info_dict dictionary, just add
# 'recurrence' to the existing 'packages' tuple.
js_info_dict = {
    'packages': ('recurrence', ),
}

# jsi18n can be anything you like here
urlpatterns += [
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), js_info_dict),
]