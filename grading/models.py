from django.db import models
from django.utils import timezone
from django.db.models import Avg

class Project(models.Model):
    project_text = models.CharField(max_length=200, verbose_name='프로젝트명')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    description = models.TextField(blank=True, verbose_name='설명')
    avg_rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        verbose_name='평균 평점',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '프로젝트'
        verbose_name_plural = '프로젝트 목록'

    def __str__(self):
        return self.project_text

class Choice(models.Model):
    project = models.ForeignKey(Project, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='선택지 텍스트')

    class Meta:
        verbose_name = '선택지'
        verbose_name_plural = '선택지 목록'

    def __str__(self):
        return self.choice_text

class Rating(models.Model):
    project = models.ForeignKey(Project, related_name='ratings', on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(
        choices=[(i, f"{i}점") for i in range (1, 6)],
        verbose_name='별점'
        )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='평가 일시')

    class Meta:
        verbose_name = '평가'
        verbose_name_plural = '평가 목록'

    def __str__(self):
        return f"{self.project.project_text} - {self.stars}점"

