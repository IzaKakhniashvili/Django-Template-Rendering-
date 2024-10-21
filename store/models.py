from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, default='default-slug')
       
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField( blank = True, null = True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.FloatField()
    image = models.ImageField(upload_to = "media/", null = True, blank = True)
    slug = models.SlugField(unique=True, default='default-slug')
    
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
       return self.quantity