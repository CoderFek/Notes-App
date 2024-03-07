from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        if len(self.title) < 50:
            return f"{self.title}"
        return f"{self.title[:50]}.."
    
    class Meta:
        verbose_name_plural = 'Notes'