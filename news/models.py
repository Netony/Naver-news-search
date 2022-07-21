from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    pub_date = models.DateTimeField()