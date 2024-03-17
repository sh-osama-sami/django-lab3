from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from authors.models import Authors
from books.models import Books


# Create your views here.


#home
def home(request):
    return render(request, 'books/home.html')
#list_books
def list_books(request):
    return render(request, 'books/allBooks.html'
                  , context={'books': Books.objects.all()})


#show book details
def book_details(request, id):
    book = Books.objects.get(pk=id)
    return render(request, 'books/bookDetails.html',
                  context={'book': book}
                  )


#create a new book
@login_required(login_url='/users/login/')
def create_book(request):
    authors = Authors.get_all_authors()
    if request.method == 'POST':
        title = request.POST["title"]
        author_id = request.POST['author']
        author = Authors.get_author_by_id(author_id)
        book = Books()
        book.title = title
        if request.POST["number_of_pages"]:
            book.number_of_pages = request.POST['number_of_pages']
        book.author = author
        book.price = request.POST['price']
        try:
            book.image = request.FILES['image']
        except Exception as e:
            pass

        book.save()
        url = reverse("list_books")
        return redirect(url)
    return render(request, 'books/create.html' , context={'authors': authors})


#update a book
@login_required(login_url='/users/login/')
def update_book(request, id):
    authors = Authors.get_all_authors()
    book = Books.objects.get(pk=id)
    if request.method == 'POST':
        title = request.POST["title"]
        author_id = request.POST['author']
        author = Authors.get_author_by_id(author_id)
        book.title = title
        if request.POST["number_of_pages"]:
            book.number_of_pages = request.POST['number_of_pages']
        book.author = author
        book.price = request.POST['price']
        try:
            book.image = request.FILES['image']
        except Exception as e:
            pass

        book.save()
        url = reverse("list_books")
        return redirect(url)
    return render(request, 'books/update.html', context={'book': book , 'authors': authors})


def books_by_author_view(request, author_id):
    author = Authors.objects.get(pk=author_id)
    books = Books.objects.filter(author=author)
    return render(request, 'books/books_by_author.html', {'author': author, 'books': books})


#delete a book
@login_required(login_url='/users/login/')
def delete_book(request, id):
    book = Books.objects.get(pk=id)
    book.delete()
    url = reverse("list_books")
    return redirect(url)