from django.db import models
import uuid


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4(),
                            editable=False, unique=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()
