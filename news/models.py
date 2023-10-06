from django.db import models
from datetime import datetime

# Create your models here.
class News(models.Model):
    Active = "ac"
    Expired = "ex"
    Inactive = "in"
    Periodic = "pr"

    STATUS_N = [
        (Active, "Active"),
        (Expired, "Expired"),
        (Inactive, "Inactive"),
        (Periodic, "Periodic")
    ]

    Urgent = "ur"
    Low_priority = "lp"
    Trending = "tr"

    TAG_N = [
        (Urgent, "Urgent"),
        (Low_priority, "Low_priority"),
        (Trending, "Trending")
    ]

    title = models.CharField(max_length=300, null=False, default="title")
    text = models.TextField(null=False, default="text")
    expiration_date = models.DateField(null=False, default=datetime.now)
    creation_date = models.DateTimeField(null=False, default=datetime.now)
    author = models.TextField(null=False,  default='admin')
    status = models.CharField(
        max_length=2,
        choices=STATUS_N,
        default=Active,
    )
    tag =  models.CharField(
        max_length=2,
        choices=TAG_N,
        default="",
    )
