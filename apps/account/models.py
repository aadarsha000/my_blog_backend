from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.utils.file_validator import file_upload_path, validate_one_mb_image_size


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to=file_upload_path,
        validators=[validate_one_mb_image_size],
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "users"

    REQUIRED_FIELDS = ["email"]
