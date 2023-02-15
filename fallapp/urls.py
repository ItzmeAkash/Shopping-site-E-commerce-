
from django.urls import path
from fallapp import views

urlpatterns = [
    path('',views.index,name='index')
]