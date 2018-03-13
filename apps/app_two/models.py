from django.db import models
from ..app_one.models import *

# Create your models here.
class Idea(models.Model):
    post = models.TextField()
    adds_idea = models.ForeignKey(User, related_name="added_by")
    likes_idea = models.ManyToManyField(User, related_name="liked_by")
    times_liked = models.IntegerField(default=0, null=True, blank=True)
