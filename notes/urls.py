from django.urls import path
from .views import notes_add, Homeview, notes_detail, notes_edit, notes_delete

urlpatterns = [
    path('', Homeview.as_view(), name = 'home'),
    path('notes/<int:pk>/', notes_detail, name = 'notes_detail'),
    path('notes/create/', notes_add, name = 'notes_add'),
    path('notes/<int:pk>/edit/', notes_edit, name='notes_edit'),
    path('notes/<int:pk>/delete/', notes_delete, name='notes_delete'),
]