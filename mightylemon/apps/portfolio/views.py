from portfolio.models import Project, Technology
from helpers.decorators import render_to
from django.shortcuts import get_object_or_404

@render_to('portfolio/index.html')
def index(request):
    """
    Shows a list of all projects on a single page.
    """
    projects = Project.objects.all()
    return {
        'project_list': projects,
        }

@render_to('portfolio/by_technology.html')
def by_technology(request, technology_slug):
    tech = get_object_or_404(Technology, slug=technology_slug)
    projects = Project.objects.filter(technologies=tech)
    return {
        'project_list': projects,
        'technology': tech,
        }


@render_to('portfolio/project.html')
def project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return {
        'project': project,
        }
