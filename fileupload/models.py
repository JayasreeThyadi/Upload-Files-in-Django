from django.db import models

# Create your models hec
class FilesUpload(models.Model):
    file = models.FileField()