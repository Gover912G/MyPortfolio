from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False, default='text')
    category = models.CharField(blank=True, max_length=30)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
       return self.name