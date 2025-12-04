from django.db import models

class Gift(models.Model):
    name = models.CharField(blank=True, null=False, default="", max_length=120)
    amount = models.IntegerField(blank=True, null=False, default=0)
    point = models.IntegerField(blank=True, null=False, default=0)

    def __str__(self):
        return self.name