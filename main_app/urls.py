from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    path('plants/', views.PlantList.as_view(), name='plant-index'),
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
    path('plants/<int:pk>/', views.PlantDetail.as_view(), name='plant-detail'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),
    path('plants/<int:pk>/add_watering/', views.add_watering, name='add-watering'),
    
    path('fertilizers/', views.FertilizerList.as_view(), name='fertilizer-index'),
    path('fertilizers/create/', views.FertilizerCreate.as_view(), name='fertilizer-create'),
    path('fertilizers/<int:pk>/', views.FertilizerDetail.as_view(), name='fertilizer-detail'),
    path('fertilizers/<int:pk>/update/', views.FertilizerUpdate.as_view(), name='fertilizer-update'),
    path('fertilizers/<int:pk>/delete/', views.FertilizerDelete.as_view(), name='fertilizer-delete'),
    path('plants/<int:pk>/assoc_fertilizer/<int:fertilizer_pk>/', views.assoc_fertilizer, name='assoc-fertilizer'),
    ]



