import os
import uuid
from django.core.exceptions import ValidationError


def file_upload_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return f"{instance._meta.model_name}/{uuid.uuid4()}{file_extension}"


def validate_one_mb_image_size(image):
    file_size = image.size
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max allowed size of image is %s MB" % limit_mb)
