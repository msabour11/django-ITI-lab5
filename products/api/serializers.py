from rest_framework import serializers
from products.models import Product




class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=50)
    description=serializers.CharField(max_length=100)
    image=serializers.ImageField(allow_null=True, allow_empty_file=True)
    price=serializers.IntegerField(default=0)
    created_at=serializers.DateTimeField(read_only=True)
    updated_at=serializers.DateTimeField(read_only=True)


    def create(self,validated_data):
        return Product.objects.create(**validated_data)


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'




    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.price = validated_data.get('price')
        instance.image = validated_data.get('image')
        instance.save()
        return  instance