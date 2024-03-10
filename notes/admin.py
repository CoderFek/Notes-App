from django.contrib import admin
from .models import User as DjangoUser, Notes

class NotesInline(admin.TabularInline):
    model = Notes
    extra = 0

class CustomUserAdmin(admin.ModelAdmin):
    inlines = [NotesInline]
    list_display = ('username','email')  

admin.site.unregister(DjangoUser)

admin.site.register(DjangoUser, CustomUserAdmin)