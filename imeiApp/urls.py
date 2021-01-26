from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

app_name = 'imeiApp'
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('check_imei/', views.check_imei, name='check_imei'),
    path('phone_base/', views.phone_base, name='phone_base'),
    path('phone_details/<model_id>/', views.phone_details, name='phone_details'),
    path("report/", views.report_stolen_phone, name='report_theft'),
    # path("map/", views.MapStolenPhones.as_view(), name='map_stolen_phones'),
    path("map/", login_required(views.MapStolenPhones.as_view()), name='map_stolen_phones'),
]
