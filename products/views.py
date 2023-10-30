from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from products.models import Product
from rest_framework import viewsets
# from products.serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    name='mohamed'

    return render(request, 'products/home.html',{'name':name})



def hello(request):
    return JsonResponse({'data':'hello','message':'hello json'})

@csrf_exempt
def acceptdata(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.body)
        request_data = json.loads(request.body)  # convert bytes to json
        return JsonResponse({ 'message':'post request data received','data':request_data,})
    
    return JsonResponse({'data':'accepted data','message':'get data request received'})

@csrf_exempt

def products_index(request):
    # if request.method == 'POST':
    #     products = json.loads(request.body) # convert bytes to json
    products=Product.get_all_products()
    serializ_products=[]
    for product in products:
        serializ_products.append({'id':product.id, 'title':product.title})
    return JsonResponse({'data':serializ_products})


# class productViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# ask serializer to create a object
