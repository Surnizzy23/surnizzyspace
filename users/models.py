from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)