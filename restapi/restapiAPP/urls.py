from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.get_all_persons),
    path('personDetails/<str:pn>/', views.get_person),
    path('addPerson/', views.add_person),
    path('editPerson/<str:pn>/', views.edit_person),
    path('deletePerson/<str:pn>/', views.delete_person),
]