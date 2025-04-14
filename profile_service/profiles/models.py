from django.db import models

class Profile(models.Model):
    user_id = models.IntegerField(unique=True)  # ID из auth_service
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
