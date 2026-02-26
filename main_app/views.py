from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Plant, Fertilizer
from .forms import WateringForm


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watering_form"] = WateringForm()
        
        fertilizer_ids = self.object.fertilizers.all().values_list('id')
        unassigned_fertilizers = Fertilizer.objects.exclude(id__in=fertilizer_ids)
        context['unassigned_fertilizers'] = unassigned_fertilizers
        return context

#Delete
class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'
    
#Update
class PlantUpdate(UpdateView):
    model = Plant
    fields = ['species', 'description','location']
    
    
def add_watering(request, pk):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = pk
        new_watering.save()
    return redirect('plant-detail', pk=pk)


class FertilizerList(ListView):
    model = Fertilizer
    context_object_name = 'fertilizers'
class FertilizerCreate(CreateView):
    model = Fertilizer
    fields = '__all__'
    success_url = '/plants/'

class FertilizerDetail(DetailView):
    model = Fertilizer
class FertilizerDelete(DeleteView):
    model = Fertilizer
    success_url = '/fertilizers/'
class FertilizerUpdate(UpdateView):
    model = Fertilizer
    fields = ['name', 'brand']
    
def assoc_fertilizer(request, pk, fertilizer_pk):
    Plant.objects.get(id=pk).fertilizers.add(fertilizer_pk)
    return redirect('plant-detail', pk=pk)

def unassoc_fertilizer(request, pk, fertilizer_pk):
    Plant.objects.get(id=pk).fertilizers.remove(fertilizer_pk)
    return redirect('plant-detail', pk=pk)