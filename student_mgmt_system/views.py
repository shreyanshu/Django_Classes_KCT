from django.shortcuts import render, redirect
from django.http import HttpResponse
from student_mgmt_system.models import Cordinator, Stream
from student_mgmt_system.forms import CordinatorForm
from django.views import View
from django.views.generic import  ListView

# Create your views here.
def home(request):
    return render(request, 'index.html')


def add_cord(request                         ):
    if request.method == 'GET':
        cord_form = CordinatorForm()
        return render(request, 'add_cord.html', context={'cordForm': cord_form})
    elif request.method == 'POST':
        data = request.POST
        cord_form = CordinatorForm(data)
        if cord_form.is_valid():
            cord_form.save()
            return HttpResponse('Saved!')
        else:
            return render(request, 'add_cord.html', {'cordForm': cord_form})

def update_cord(request, id):
    if request.method == 'GET':
        cord = Cordinator.objects.get(id=id)
        cord_form = CordinatorForm(instance=cord)
        return render(request, 'update_cord.html', context={'cordForm': cord_form})
    elif request.method=='POST':
        cord = Cordinator.objects.get(id=id)
        data = request.POST
        cordFrom = CordinatorForm(data, instance=cord)
        if cordFrom.is_valid():
            cordFrom.save()
            return HttpResponse('Updated !!')
        else:
            return render(request, 'update_cord.html', context={'cordForm': cordFrom})


def list_cord(request):
    cord = Cordinator.objects.all()
    return render(request, 'list_cord.html', {'list_cord': cord})

#
# class ListCord(View):
#     def get(self, request):
#         cord = Cordinator.objects.all()
#         return render(request, 'list_cord.html', {'list_cord': cord})


class ListCord(ListView):
    model = Cordinator
    template_name = 'list_cord.html'
    context_object_name = 'list_cord'


class DeleteCordView(View):
    def get(self, request, id):
        streams = Stream.objects.filter(cordinator__id=id)
        if len(streams)==0:
            cord = Cordinator.objects.get(id=id)
            cord.delete()
            return redirect('list_cord')
        else:
            return HttpResponse('Can\'t delete the cordinator')