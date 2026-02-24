from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Plant


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# CBV Class based Views
'''
    ListView - List stuff
    CreateView - Create stuff
    DeleteView - Delete stuff
    UpdateView - Update Stuff
    DetailView - Show Page

'''

# Listing
class PlantList(ListView):
    model = Plant
    context_object_name = 'plants'


class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'species', 'description','location']
    
#Detail
class PlantDetail(DetailView):
    model = Plant
    
#Delete
class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'
    
#Update
class PlantUpdate(UpdateView):
    model=Plant
    fields = ['species', 'description','location']