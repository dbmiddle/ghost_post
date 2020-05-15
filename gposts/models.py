from django.db import models
from django.utils import timezone

# Create your models here.


class BoastsAndRoasts(models.Model):
    is_boast = models.BooleanField()
    content = models.CharField(max_length=500)
    votescore = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
