from django.db import models

# Create your models here.
class Db(models.Model):
    name=models.CharField(max_length=30)
    img = models.FileField(upload_to='media/abc')
    def __str__(self):
        return self.name
