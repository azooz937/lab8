from django.db.models import Q
from django.shortcuts import render
from .models import Book
from django.db.models import Avg, Max, Min, Sum, Count

def task1_view(request):
    books = Book.objects.filter(price__lte=50)
    return render(request, 'books/task1.html', {'books': books})


def task2_view(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(authors__icontains='qu')))
    return render(request, 'books/task2.html', {'books': books})


def task3_view(request):
    books = Book.objects.exclude(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(authors__icontains='qu')))
    return render(request, 'books/task3.html', {'books': books})


def task4_view(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books/task4.html', {'books': books})


def task5_view(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'books/task5.html', {'stats': stats})
