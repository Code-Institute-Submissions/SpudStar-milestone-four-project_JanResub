import uuid

from django.db import models

from goods.models import Info
from profiles.models import UserProfile

# Create your models here.


class Order(models.Model):

    order_number = models.CharField(max_length=16, null=False, editable=False)
    full_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    user_trainer_code = models.CharField(max_length=255,
                                         null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')

    def _generate_order_number(self):

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Info, null=False, blank=False,
                                on_delete=models.CASCADE, default="")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
    # NEED SKU RETURN HERE, CHECKOUT2
