from django.conf.urls import url, include
# from django.contrib import admin
from .import views
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^additem$',views.additem,name="additem"),
    url(r'^addtowishlist/(?P<id>\d+)$',views.addtowishlist,name="addtowishlist"),
    url(r'^removefromwishlist/(?P<id>\d+)$',views.removefromwishlist,name="removefromwishlist"),
    url(r'^deleteprod/(?P<id>\d+)$',views.deleteprod,name="deleteprod"),
    url(r'^logout$',views.logout,name="logout"),
    url(r'^goback$',views.goback,name="goback"),
    url(r'^show_product/(?P<id>\d+)$',views.show_product,name="show_product"),

]
