from django.conf import settings
from django.db import models
from django.utils import timezone


class FileUpload(models.Model):
    file = models.FileField(upload_to='documents//%Y/%m/%d/')
