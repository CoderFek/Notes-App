from django.urls import path
from .views import notes_add, home_view, notes_detail, notes_edit, notes_delete, login_view, logout_view, signup_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('notes/<int:pk>/', notes_detail, name = 'notes_detail'),
    path('notes/create/', notes_add, name = 'notes_add'),
    path('notes/<int:pk>/edit/', notes_edit, name='notes_edit'),
    path('notes/<int:pk>/delete/', notes_delete, name='notes_delete'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('signup/', signup_view, name = 'signup'),


]