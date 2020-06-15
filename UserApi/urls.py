from django.urls import path,include
from .views import UserApiView
urlpatterns=[
    path('user/getUsers/',UserApiView.as_view()),
    path('user/addUser/',UserApiView.as_view()),
    path('user/Login',UserApiView.as_view())
]