from django.db import models


class Chat(models.Model):
    user = models.CharField(max_length=20, null=True, blank=True)
    stupid = models.IntegerField(null=True, blank=True, default=0)
    fat = models.IntegerField(null=True, blank=True, default=0)
    dumb = models.IntegerField(null=True, blank=True, default=0)

    def save(self, *args, **kwargs):
        result = super(Chat, self).save(*args, **kwargs)
        return result