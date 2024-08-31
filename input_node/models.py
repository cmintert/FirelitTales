from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Node(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    attributes = models.TextField()
    relations = models.TextField()
    description = models.TextField()
    node_created_by = models.ForeignKey(User, related_name='created_nodes', on_delete=models.CASCADE)
    node_created_on = models.DateTimeField(default=timezone.now)
    node_modified_on = models.DateTimeField(auto_now=True)
    node_last_modified_by = models.ForeignKey(User, related_name='modified_nodes', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.node_modified_on = timezone.now()
        if not self.pk:
            self.node_created_on = timezone.now()
        self.node_last_modified_by = kwargs.pop('modified_by', None)
        super().save(*args, **kwargs)