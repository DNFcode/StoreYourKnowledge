from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField


class Goal(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100, help_text='Choose nice name for your new goal.')
    description = models.TextField(blank=True, help_text='Describe the main idea of your goal. Just for yourself.')


# class Group(models.Model):
#     name = models.CharField(max_length=200)
#     users = models.ManyToManyField(User)
#
#
# class GroupTask(models.Model):
#     group = models.ForeignKey(Group)
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     deadline = models.DateField()
#     created = models.DateField(auto_now_add=True)


class Task(models.Model):
    goal = models.ForeignKey(Goal)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    # group_task = models.ForeignKey(GroupTask)


class CodeExample(models.Model):
    goal = models.ForeignKey(Goal)
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=100)
    code = models.TextField()


class Book(models.Model):
    goal = models.ForeignKey(Goal)
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    is_read = models.BooleanField(default=False)


class Note(models.Model):
    goal = models.ForeignKey(Goal)
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField()


class MapVertex(models.Model):
    title = models.CharField(max_length=200, unique=True)
    hits = models.PositiveIntegerField()
    connections = ArrayField(models.CharField(max_length=200))
    parents = ArrayField(models.CharField(max_length=200))


class MapEdge(models.Model):
    vertexes = models.CharField(max_length=200, unique=True)
    hits = models.PositiveIntegerField()