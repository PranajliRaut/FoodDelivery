from django.urls import path

from .views import *

urlpatterns=[
    path('ind/',index, name='ind'),
    path('contact/',contact_us, name='contact'),
    path('about/',about, name ='about'),
    path('team/',team_members, name ='team'),
    path('all_dishes/',all_dishes, name='all_dishes'),
    path('register/',register,name="register"),
    path('check_user_exists/',check_user_exists,name="check_user_exist"),
    path('login/',signin, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('dish/<int:id>/', single_dish, name='dish'),

    path('payment_done/', payment_done, name='payment_done'),
    path('payment_cancel/', payment_cancel, name='payment_cancel'),
]