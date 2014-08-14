from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    STORY = 'ST'
    TODO = 'TD'
    IN_PROGRESS = 'IP'
    TESTING = 'TE'
    DONE = 'DN'
    STATUS_CHOICES = (
        (STORY, 'Stories'),
        (TODO, 'To do'),
        (IN_PROGRESS, 'In Progress'),
        (TESTING, 'Testing'),
        (DONE, 'Done')
    )
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=STORY)
    owner = models.ForeignKey(User, related_name="owned_tasks")
    moderator = models.ForeignKey(User, related_name="moderated_tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
