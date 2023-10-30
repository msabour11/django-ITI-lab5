from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from products.api.serializers import ProductSerializer


@api_view(['POST', 'GET'])
def  hello_world(request):
    if request.method == 'POST':
        return Response({'message':'post message received'})
    
    return Response({'message':'get message received'})
        




# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         product = ProductSerializer(data=request.data)
#         if product.is_valid():
#             product.save()
#             return Response({"messsage": 'object add received', "product":product.data}, status=201)
#         return Response(product.errors, status=400)

#     elif request.method=='GET':
#         products = Product.get_all_products()  # query set of model objects
#         serlized_products = ProductSerializer(products, many=True)
#         return Response({"message": "products data receieved", 'products': serlized_products.data})



# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         product=Product.objects.create(title=request.data['title'],
#                                         description=request.data['description'],
#                                         price=request.data['price'],
#                                         image=request.data['image'])
        
#         product.save()
#         return Response({'products':ProductSerializer(product).data})


#     elif request.method == 'GET':

#         products=Product.get_all_products()

#         products_serialized=[]
#         for product in products:
#             print(ProductSerializer(product).data)
#             products_serialized.append(ProductSerializer(product).data)


#         return Response({"products": products_serialized})


# ask serializer to create objects

# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'GET':

#         serialized_products = ProductSerializer(data=request.data)
#         if serialized_products.is_valid():
#             serialized_products.save()
#             return Response({'products': serialized_products.data},status=200)
        
#         return Response({'error':serialized_products.errors},status=status.HTTP_400_BAD_REQUEST)
    



#     elif request.method == 'GET':
#         products=Product.get_all_products()
#         serialized_products=ProductSerializer(products,many=True)

#         return Response({'products': serialized_products.data})


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        # Create a new product using data from the request
        serialized_products = ProductSerializer(data=request.data)
        if serialized_products.is_valid():
            serialized_products.save()
            return Response({'product': serialized_products.data}, status=status.HTTP_201_CREATED)
        
        return Response({'error': serialized_products.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # Retrieve a list of all products
        products = Product.get_all_products()
        serialized_products = ProductSerializer(products, many=True)

        return Response({'products': serialized_products.data}, status=status.HTTP_200_OK)
    





@api_view(['GET', 'DELETE', 'PUT'])
def product_resource(request, id):
    product = Product.objects.filter(id=id).first()
    if request.method=='GET':
        product = Product.objects.filter(id=id).first()
        serlized_product = ProductSerializer(product)
        return Response({'data':serlized_product.data}, status=200)

    elif request.method=='DELETE':
        product.delete()
        return Response({"message":"object deleted"}, status= 204)

    elif request.method=="PUT":
        serlized_product = ProductSerializer(instance=product,data=request.data, partial=True)
        if serlized_product.is_valid():
            serlized_product.save()
            return Response({"messsage": 'object add received', "product": serlized_product.data}, status=201)
        return Response(serlized_product.errors, status=400)