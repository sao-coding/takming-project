from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    # email = models.EmailField()
    # phone = models.CharField(max_length=10)
    # address = models.CharField(max_length=100)
    # birthday = models.DateField()
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.username