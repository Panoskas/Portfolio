from django.db import models

class Project (models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    image = models.FilePathField(path = "/home/panos/Desktop/rp-portofolio/staticfiles  /img")
