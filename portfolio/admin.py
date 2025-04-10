from django.contrib import admin
from .models import Project, Technology, ProjectImage, InfoResource


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_created', 'date_updated')
    list_filter = ('category', 'date_created')
    search_fields = ('title', 'description')
    inlines = [ProjectImageInline]
    filter_horizontal = ('technologies_used',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(InfoResource)
class InfoResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'content')
