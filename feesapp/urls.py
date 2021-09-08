from django.contrib import admin
from django.urls import path
from feesapp import views
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('student_registeration',views.student_registeration,name='student_registeration'),
    path('search_students',views.search_students,name='search_students'),
    path('fees_collection',views.fees_collection,name='fees_collection'),
    path('adminpanel',views.adminpanel,name='adminpanel'),
    path('invoice',views.invoice,name='invoice')
]
