from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    path('changePass/', views.user_change_pass, name="changePass"),
    path('forgotPass/', views.forgotPass, name="forgotPass"),

    path('rider/', views.rider, name='rider'),
    path('driver/', views.driver, name='driver'),

    path('home/', views.home, name='home'),
    path('settings/', views.settings, name="settings"),
    path('wallet/', views.wallet, name="wallet"),
    path('ratting/', views.ratting, name="ratting"),
    path('profile/', views.profile, name="profile"),
    path('profile_view/', views.profile_view, name="profile_view"),
    path('review/', views.review, name='review'),
    # path('home/help', views.help, name="help"),

]
