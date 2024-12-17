from django.db.models import Count
from .models import Address
from django.shortcuts import render

def task7_view(request):
    city_stats = Address.objects.annotate(student_count=Count('students'))
    return render(request, 'students/task7.html', {'city_stats': city_stats})
