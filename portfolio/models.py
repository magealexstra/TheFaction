from django.db import models

class Technology(models.Model):
    """
    Represents a technology or tool used in projects.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Represents a portfolio project.
    """
    CATEGORY_CHOICES = [
        ('Software', 'Software'),
        ('Home Automation', 'Home Automation'),
        ('Automotive Integration', 'Automotive Integration'),
        ('RV Enhancements', 'RV Enhancements'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    technologies_used = models.ManyToManyField(Technology, blank=True)
    github_repo_link = models.URLField(blank=True, null=True)
    purchase_links = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """
    Represents images associated with a project.
    """
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"


class InfoResource(models.Model):
    """
    Represents an informational or learning resource.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='info_resources/', blank=True, null=True)

    def __str__(self):
        return self.title
