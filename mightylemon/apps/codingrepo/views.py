from codingrepo.models import CodeProject
from django.views.generic.list_detail import object_list, object_detail

def index(request):
    return object_list(request,
                       queryset=CodeProject.objects.all(),
                       template_name='code/project_list.html',
                       template_object_name="project")

def detail(request, slug):
    return object_detail(request,
                         queryset=CodeProject.objects.all(),
                         template_name='code/project_detail.html',
                         template_object_name='project',
                         slug=slug)
