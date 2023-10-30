
from django.contrib import admin
from django.urls import path,include
from products.api.views import index,hello_world,product_resource
urlpatterns = [
    path('', index, name='api.index'),
    path('hello/',hello_world, name='api.hello_world'),
    path('<int:id>',product_resource, name='api.product_resource'),
  
  

]