from django.db import models
from datetime import datetime

# Create your models here.


class cool_connections(models.Model):
    source_ip = models.CharField(max_length=128)
    source_port = models.CharField(max_length=6)
    dest_ip = models.CharField(max_length=128)
    dest_port = models.CharField(max_length=6)


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(
        'date published', default=datetime.now())

    def __str__(self):
        return self.totorial_title
