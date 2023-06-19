from django.db import models

# Create your models here.
class Reality(models.Model):
    title = models.CharField(max_length=1024)
    image_url = models.URLField()

