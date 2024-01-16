from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class ImageModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,  # Allow null values
        blank=True  # Allow the field to be blank in forms and admin
    )

    def __str__(self):
        return self.title
