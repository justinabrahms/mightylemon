from django.views.generic.list_detail import object_list
from speaking.models import Talk

def index(request):
    return object_list(request,
                       queryset=Talk.objects.all(),
                       template_object_name="talk",
                       template_name="speaking.html")
