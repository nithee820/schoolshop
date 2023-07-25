
from django.urls import path
from .import views
app_name='store'



urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('base/',views.base,name='base')
]
