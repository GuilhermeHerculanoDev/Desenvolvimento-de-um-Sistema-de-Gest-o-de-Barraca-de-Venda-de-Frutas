from django.contrib import admin
from django.urls import path
from fruit_stand_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('login/', views.screen_login, name='screen_login'),

    path('register', views.register, name='_screen_register'),

    path('authentication/register', views.register_sellers, name='register_sellers'),

    path('authentication/login/', views.login, name='login'),

    path('search', views.search, name='search'),

    path('sell', views.sell, name='sell'),

    path('sell_fruit', views.sell_fruit, name='sell_fruit'),

    path('report', views.report, name='report'),

    path('exit', views.exit, name='exit')
]