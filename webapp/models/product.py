from django.db import models
from .category import CategoryModel
from ckeditor.fields import RichTextField


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/products')

    @staticmethod
    def get_all_products():
        return ProductModel.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return ProductModel.objects.filter(category = category_id)
        else:
            return ProductModel.get_all_products()

    @staticmethod
    def get_products_by_id(ids):
        return ProductModel.objects.filter(id__in = ids)
    
    @staticmethod
    def get_single_product(id):
        return ProductModel.objects.filter(id=id)