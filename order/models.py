from django.db import models

class Order(models.Model):
    gift = models.ForeignKey('gift.Gift', on_delete=models.SET_NULL, null=True, blank=True, related_name="order_gift")
    amount = models.IntegerField(blank=True, null=False, default=0)
    point = models.IntegerField(blank=True, null=False, default=0)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True, related_name="order_user")

    def __str__(self):
        return self.amount * self.point