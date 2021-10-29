from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model): #Class client
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #un utilisateur est lié à un unique client et vice versa
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100,null=True)
    phone = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    phone = models.CharField(max_length=30, null=False,blank=False)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model): #Class produit
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="uncategorized")
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(default="pas de description")
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False) #pour dire que le produit est physique ou numérique
    provider = models.ManyToManyField(Provider)
    tags = models.ManyToManyField(Tag)
    #image

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    provider = models.ManyToManyField(Provider) #un service peut avoir plusieur fournisseur et un fournisseur peur prosse pluisieurs services

    def __str__(self):
        return self.name


class ShippingInfo(models.Model):
    shipping_type = models.CharField(max_length=200)
    cost = models.FloatField()
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    quater = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.address    


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) # si on supprime un client on ne supprime pas la commande on la met à null
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    shippinginfo = models.ForeignKey(ShippingInfo, on_delete=models.SET_NULL, null=True)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True) #plusieurs ligne de commande peuvent concerner un produit
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) #une commande peut avoir plusieurs lignes de commande
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
