from django.shortcuts import render
from .models import Shotinfo
from django.shortcuts import render,get_object_or_404
from .forms import ShotinfoForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
import json
from django.http import Http404, HttpResponse


# Create your views here.

def shot_list(request):
	return render(request, 'mastershotinfo/shot_list.html')

#take value only from javascript
def get_projects(request):
    if request.is_ajax():
        #projects = ['Red', 'Green',]
        projects = Shotinfo.objects.all()
        results = []
        for project in projects:
            project_json = {}
            project_json['type'] = project.shot_type
            project_json['record'] = project.shot_record
            project_json['status'] = project.shot_status
            results.append(project_json)
        data = json.dumps(results)
        return HttpResponse(data, content_type='application/json')
    else:
        #data = 'fail'
        raise Http404
        
def add_projects(request):
    if request.is_ajax() and request.POST:
        data = {'message': "%s added" % request.POST.get('item')}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404



