from django.db import models 
from apps.users.models import User
from apps.product.models import Product


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.DecimalField(max_digits=10, decimal_places=2)
#     item_total = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.quantity} x {self.product.name} in Cart for {self.cart.user}"
