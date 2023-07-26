from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Note Title", max_length=200)
    content = models.CharField(verbose_name="Note Content", max_length=10000)
    timestamp = models.DateTimeField(auto_now_add=True)
    short_title = models.CharField(verbose_name="Note Slug", max_length=12)

    class Meta:
        order_by = ['-timestamp']

    def __str__(self):
        return f"{self.title}"