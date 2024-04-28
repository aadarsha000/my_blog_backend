from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "published", "Published"
        DRAFT = "draft", "Draft"

    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="post/thumbnail", null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey("account.User", on_delete=models.CASCADE)
    # likes = models.ManyToManyField("account.CustomUser", related_name="blogpost_like")
    category = models.ManyToManyField("posts.PostCategory", null=True, blank=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
