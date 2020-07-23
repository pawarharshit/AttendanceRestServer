from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length = 50,null=True)
    image = models.ImageField(upload_to = "images/photos/",null=True)
    