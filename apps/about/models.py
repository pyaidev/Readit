from django.db import models


class FeedBack(models.Model):
    name = models.CharField(max_length=221)
    position = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='about/')
    context = models.TextField()

    def __str__(self):
        return self.name
