from django.db import models
import uuid 
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption=models.TextField()
    likes=models.IntegerField(default=0)
    created_at=models.DateTimeField(default=datetime.now)
    image=models.ImageField(upload_to='posty')
    def _str_(self):
        return self.user
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profimg = models.ImageField(upload_to='Profile_img',default='pro.png')
    location = models.CharField(max_length=100,blank=True)

    def _str_(self):
        return self.user.username

class heart(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    def _str_(self):
        return self.username