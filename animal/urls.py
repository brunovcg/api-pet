from django.urls import path
from .views import AnimalView, AnimalFilterView



urlpatterns = [
  path('animal/', AnimalView.as_view()),
  path('animal/<int:animal_id>',AnimalFilterView.as_view())
]