from django.shortcuts import render
from django.http import HttpResponse
from student_mgmt_system.models import Cordinator
from student_mgmt_system.forms import CordinatorForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


def add_cord(request):
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