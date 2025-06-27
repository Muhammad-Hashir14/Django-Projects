from django.db import models


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=10000)
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"