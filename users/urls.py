from django.urls import path
from . import views


urlpatterns = [
  path('profile',views.Profile,name='profile'),
  path('register',views.Register,name='register'),
  path('login',views.Login,name='login'),
  path('logout',views.Logout,name='logout'),
  path('edit-profile',views.EditProfile,name='editprofile'),
]