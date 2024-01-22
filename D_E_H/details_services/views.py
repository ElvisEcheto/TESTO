from django.shortcuts import render, redirect

from books.models import Book

def details_services(request):    
    details_services_list = details_service.objects.all()    
    return render(request, 'books/index.html', {'books_list': books_list})

def change_status_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.status = not book.status
    book.save()
    return redirect('books')