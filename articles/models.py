
from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField.auto_now()
    author = 