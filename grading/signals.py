from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg

from .models import Rating, Project

@receiver([post_save, post_delete], sender=Rating)
def update_project_avg(sender, instance, **kwargs):
    project = instance.project
    agg = project.ratings.aggregate(avg=Avg('stars'))['avg'] or 0
    project.avg_rating = round(agg, 1)
    project.save(update_fields=['avg_rating'])
