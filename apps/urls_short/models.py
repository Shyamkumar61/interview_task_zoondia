from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class Urls(TimeStampedModel):

    name = models.CharField(max_length = 20, blank=False, null=False)
    shortend_url = models.CharField(max_length=255, unique=True, db_index = True, blank=False, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    actual_url = models.URLField()
    


class UrlVistors(TimeStampedModel):

    url = models.ForeignKey(Urls, on_delete=models.CASCADE, related_name='url_vistitors')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()

