from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    domain = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    tiktok_link = models.URLField(max_length=500)
    famous = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "locations"