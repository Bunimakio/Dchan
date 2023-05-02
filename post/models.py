from django.db import models
from django.contrib.auth.models import User

class ForumUser(models.Model):

    forum_user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField()

class Post (models.Model):

    author = models.ForeignKey(ForumUser,on_delete=models.CASCADE)
    post_id = models.IntegerField()
    posted = models.DateField()
    body = models.TextField()
    link = models.CharField(max_length=250)
