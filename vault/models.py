from django.db import models

class password(models.Model):
    website = models.CharField(max_length=200)
    username = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.website} - {self.username}"