from django.db import models
from django.contrib.auth.models import User
from randomslugfield import RandomSlugField
# from autoslug import AutoSlugField

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     # email = models.EmailField()
#     # phone = models.CharField(max_length=10)
#     # address = models.CharField(max_length=100)
#     # birthday = models.DateField()
#     enabled = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username


class Profile(models.Model):
    maker = (
        ('台灣', '台灣'),
        ('日本', '日本'),
        ('香港', '香港'),
        ('越南', '越南'),
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=4, choices=maker, default='台灣')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = RandomSlugField(length=9)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.content[:20]


class Member_info(models.Model):
    room = models.PositiveIntegerField()
    bed = models.SlugField(max_length=10)
    member_class = models.CharField(max_length=5)
    student_ID = models.CharField(max_length=10)
    name = models.CharField(max_length=5)
    ID_number = models.CharField(max_length=10)
    birthday = models.DateField()
    phone = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=10)
    emergency_contact_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
