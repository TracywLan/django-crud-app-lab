from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Plant, Fertilizer
from .forms import WateringForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

class PlantList(LoginRequiredMixin,ListView):
    model = Plant
    context_object_name = 'plants'
    
    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)


class PlantCreate(LoginRequiredMixin,CreateView):
    model = Plant
    fields = ['name', 'species', 'description','location']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
#Detail
class PlantDetail(LoginRequiredMixin,DetailView):
    model = Plant
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watering_form"] = WateringForm()
        
        fertilizer_ids = self.object.fertilizers.all().values_list('id')
        unassigned_fertilizers = Fertilizer.objects.exclude(id__in=fertilizer_ids)
        context['unassigned_fertilizers'] = unassigned_fertilizers
        return context

#Delete
class PlantDelete(LoginRequiredMixin,DeleteView):
    model = Plant
    success_url = '/plants/'
    
#Update
class PlantUpdate(LoginRequiredMixin,UpdateView):
    model = Plant
    fields = ['species', 'description','location']
    
@login_required
def add_watering(request, pk):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = pk
        new_watering.save()
    return redirect('plant-detail', pk=pk)



class FertilizerList(LoginRequiredMixin,ListView):
    model = Fertilizer
    context_object_name = 'fertilizers'
class FertilizerCreate(LoginRequiredMixin,CreateView):
    model = Fertilizer
    fields = '__all__'
    success_url = '/fertilizers/'

class FertilizerDetail(LoginRequiredMixin,DetailView):
    model = Fertilizer

class FertilizerDelete(LoginRequiredMixin,DeleteView):
    model = Fertilizer
    success_url = '/fertilizers/'
class FertilizerUpdate(LoginRequiredMixin,UpdateView):
    model = Fertilizer
    fields = ['name', 'brand']

@login_required
def assoc_fertilizer(request, pk, fertilizer_pk):
    Plant.objects.get(id=pk).fertilizers.add(fertilizer_pk)
    return redirect('plant-detail', pk=pk)

@login_required
def unassoc_fertilizer(request, pk, fertilizer_pk):
    Plant.objects.get(id=pk).fertilizers.remove(fertilizer_pk)
    return redirect('plant-detail', pk=pk)


class Login(LoginView):
    template_name='login.html'
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plant-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
