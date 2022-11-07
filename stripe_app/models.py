from django.db import models

# Create your models here.

class ProtineProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_des = models.TextField()
    product_price = models.IntegerField()


    # def get_display_price(self):
    #     return "{0:.2f}".format(self.product_price * 100)