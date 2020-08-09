from django.conf import settings
from django.db import models
from django.utils import timezone


class Foods(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=5)
    menu = models.CharField(max_length=20)
    time = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=30)
    call = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img/food/', null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    review = models.ForeignKey('food.Foods', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
