from django.contrib import admin
from .models import Employ
# Register your models here.

@admin.register(Employ)
class EmployAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name', 'job_title' , 'status' , 'phone')
    ordering = ['-created_at']
