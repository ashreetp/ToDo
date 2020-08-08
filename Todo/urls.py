from django.urls import path
from .views import index,login,register,logout,updatelogin,delete,todopage,deletepost,updatepost

urlpatterns = [
    path('',index),
    path('login/',login),
    path('register/',register),
    path('logout/',logout),
    path('updatelogin/',updatelogin),
    path('delete/',delete),
    path('todopage/',todopage),
    path('todopage/deletepost/<int:id>/',deletepost),
    path('todopage/updatepost/<int:id>/',updatepost),

]
