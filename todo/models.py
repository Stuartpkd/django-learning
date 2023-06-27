from django.db import models

# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length=50, null=False, black=False)
    done = models.BooleanField(null=False, black=False, default=False)
