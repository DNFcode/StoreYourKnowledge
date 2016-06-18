from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError


class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Task(models.Model):
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

    CHOICES = (
        ('CE', 'Code example'),
        ('BK', 'Book'),
        ('NR', 'Not related')
    )
    related_to = models.CharField(
        max_length=2,
        choices=CHOICES,
        default='NR'
    )

    # Books and CodeExamples relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # Override validation
    def full_clean(self, *args, **kwargs):
        super(Task, self).full_clean(*args, **kwargs)

        permitted_models = {
            'CE': CodeExample,
            'BK': Book,
            'NR': None
        }
        model = self.content_type.model_class() if self.content_type else None

        if permitted_models[self.related_to] != model:
            raise ValidationError('related_to and content_object are not matching')


class CodeExample(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code = models.TextField()


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pages = models.PositiveIntegerField()
    is_read = models.BooleanField(default=False)