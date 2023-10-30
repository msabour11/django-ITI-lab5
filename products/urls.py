from django.contrib import admin
from django.urls import path,include
from products.views import home,hello,acceptdata,products_index

urlpatterns = [
    path('api/', include('products.api.urls')),
  
    path('home/',home,name='products.home'),
    path('hello/',hello,name='products.hello'),
    path('accept/',acceptdata,name='acceptdata'),
    path('index/',products_index,name='products_index'),
    # path('api/',include('products.api.urls')),

]
