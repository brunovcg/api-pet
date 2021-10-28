from django.urls import path
from .views import AnimalView, AnimalFilterView



urlpatterns = [
  path('animals/', AnimalView.as_view()),
  path('animals/<int:animal_ID>/',AnimalFilterView.as_view())
]