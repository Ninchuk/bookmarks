from django.db import models


class Actions(models.Model):
    user = models.ForeignKey('auth.User', related_name='actions', on_delete=models.CASCADE)
    verd = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        idexes = models.Index(fields=['-created'])
        ordering = ['-created']
