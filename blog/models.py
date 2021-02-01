from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default ="")
    author = models.ForeignKey(
        'auth.User', 
        on_delete = models.CASCADE,
    )
    haulier = models.CharField(max_length = 200, default="")
    origin = models.CharField(max_length = 200, default="")
    material = models.CharField(max_length = 200, default="")
    destination = models.CharField(max_length =200, default = "")
    Vehicle_reg = models.CharField(max_length=15, default="")
    date = models.CharField(max_length = 200, default="")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', args="")
        







