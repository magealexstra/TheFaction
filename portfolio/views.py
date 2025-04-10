from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Project, InfoResource


class HomePageView(TemplateView):
    """
    Homepage landing page.
    """
    template_name = 'portfolio/home.html'


class AboutPageView(TemplateView):
    """
    About me page.
    """
    template_name = 'portfolio/about.html'


class ProjectListView(ListView):
    """
    List of all projects, potentially filterable by category.
    """
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class ProjectDetailView(DetailView):
    """
    Detail view for a single project.
    """
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class AdminLoginView(LoginView):
    template_name = 'portfolio/admin_login.html'
    next_page = reverse_lazy('admin:index')


class InfoResourceListView(ListView):
    """
    List of info/learning resources.
    """
    model = InfoResource
    template_name = 'portfolio/info_list.html'
    context_object_name = 'resources'
