from django.contrib.auth.models import User
from django.db import models

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_term = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class Sample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    donor_count = models.IntegerField()
    material_type = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
