from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return CategoryModel.objects.all()

    def __str__(self):
        return self.name
    