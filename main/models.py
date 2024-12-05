from django.db import models

# Create your models here.
class ProblemSet(models.Model):
    id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    successCount = models.IntegerField()
    maxCount = models.IntegerField()
    name = models.CharField(max_length=20)

class Problem(models.Model):
    headSetId = models.IntegerField()
    order = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    score = models.FloatField()
    success = models.BooleanField()