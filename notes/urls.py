from django.urls import path
from .views import notes_add, Homeview, notes_detail

urlpatterns = [
    path('', Homeview.as_view(), name = 'home'),
    path('notes/<int:pk>/', notes_detail, name = 'notes_detail'),
    path('notes/create/', notes_add, name = 'notes_add'),

]