from django.contrib import admin
from django.db.models import Avg

from .models import Project, Choice, Rating

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_text', 'average_rating', 'pub_date')
    ordering = ('-avg_rating',)
    inlines = [ChoiceInline]
    list_filter = ('pub_date',)
    search_fields = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(rating_avg=Avg('ratings__stars'))
    
    def average_rating(self, obj):
        return round(obj.rating_avg or 0, 1)
    average_rating.admin_order_field = 'rating_avg'
    average_rating.short_description = '평균 평점'

    fieldsets = [
        (None,              {'fields': ['project_text']}),
        (None,              {'fields': ['description']}),
    ]
    
class RatingAdmin(admin.ModelAdmin):
    list_display = ('project', 'stars', 'created_at')
    list_filter = ('stars',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating)
