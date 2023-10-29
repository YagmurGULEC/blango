from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value


class Comment(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # pointing to the a generic type
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # pointing to the primary key of the object to be defined flexibly
    object_id = models.PositiveIntegerField(db_index=True)
    # field to look up the object from the two other field
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title


class AuthorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"
