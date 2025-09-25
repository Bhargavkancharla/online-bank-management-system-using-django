from django.urls import path
from .import views


urlpatterns=[
    path('login/',views.loginpage,name='loginurl'),
    path('register/',views.registerpage,name='registerurl'),
    path('operation/<int:no>/',views.operation,name='operationurl'),
    path('balanceenquery/<int:no>/',views.balance,name='balanceurl'),
    path('withdraw/<int:no>/',views.withdraw,name='withdrawurl'),
    path('deposit/<int:no>/',views.deposit,name='depositurl'),
    path('userdetails/<int:no>/',views.details,name='detailsurl'),
]