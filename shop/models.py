from django.db import models
from django import forms
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    count_on_stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} - {self.price}$ - {self.count_on_stock} - {self.category}'

    def get_absolute_url(self):
        return f'/product/{self.id}'

class Client(models.Model):
    name = models.CharField(max_length=50)
    order = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.name} - {self.order}"

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'price', 'count_on_stock', 'category']