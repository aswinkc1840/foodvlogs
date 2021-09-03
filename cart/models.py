from django.db import models

# Create your models here.
from shop.models import product


class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return format(self.cart_id)


class item(models.Model):
    prod = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return format(self.prod)

    def total(self):
        return self.prod.price*self.quan

