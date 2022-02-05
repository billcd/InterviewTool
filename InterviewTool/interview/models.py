from django.db import models
from accounttree.models import Account

# Create your models here.


class Interview(models.Model):
    interviewee = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    # interviewer = models.ForeignKey(Account, on_delete=models.CASCADE())
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

