from django.apps import AppConfig


class GradingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grading'
    verbose_name = 'Grading'
    def ready(self):
        import grading.signals
