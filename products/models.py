from django.db import models


class Product(models.Model):
    
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100,null=True)
    price=models.IntegerField(default=0, null=True)
    # image=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='products/images',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f'{self.title}'
    

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    @classmethod
    def get_selected_products(cls):
        return cls.objects.filter(id=id).first()

    # @classmethod
    # def get_selected_product(cls, product_id):
    #     return cls.objects.filter(id=product_id).first()

