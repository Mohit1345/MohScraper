from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('scrapped_data',views.scrapped_data,name="scrapped_data"),
    path('download_pdf',views.download_pdf,name = "download_pdf")

]
