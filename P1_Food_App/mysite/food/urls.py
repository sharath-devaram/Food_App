from django.contrib import admin
from django.urls import path
from . import views

app_name='food'
urlpatterns=[
    path("",views.indexClassView.as_view(),name="index"),
    path("item/",views.item,name="item"),
    path("heading/",views.heading,name="heading"),
    path('<int:pk>/',views.FoodDetail.as_view(),name="detail"),

    ##add items
    path('add',views.Create_Item.as_view(),name='create_item'),
    #edit
    path('update/<int:id>/',views.update_item,name="update_item"),
    #delete
    path("delete/<int:id>",views.delete_item,name='delete_item'),
]