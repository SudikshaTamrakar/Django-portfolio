from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField()

    def __str__(self):
        return self.title
