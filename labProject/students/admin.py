from django.contrib import admin
from .models import Address, Student

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')
    search_fields = ('city',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address')
    search_fields = ('name',)
    list_filter = ('age', 'address__city')
