from django.db import models

class Card(models.Model):
    #videoId = models.AutoField(primary_key=True)
    videoId = models.IntegerField(primary_key=True, unique=True)  # Specify unique=True to act as primary key
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    upload_date = models.DateTimeField(auto_now_add=True)
