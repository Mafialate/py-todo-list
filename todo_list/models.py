from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    IS_DONE_CHOICES = [
        (True, "Done"),
        (False, "Not Done"),
    ]

    name = models.CharField(max_length=255)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False, choices=IS_DONE_CHOICES)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.name
