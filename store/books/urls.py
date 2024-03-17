
from django.urls import path


from .views import  list_books ,home, book_details, create_book, update_book, delete_book, books_by_author_view

urlpatterns = [

    path('all/', list_books, name='list_books'),
    path('<int:id>/', book_details, name='book.details'),
    path('home/', home, name='home'),
    path('create/', create_book, name='create_book'),
    path('update/<int:id>/', update_book, name='update_book'),
    path('delete/<int:id>/', delete_book, name='delete_book'),
    path('author/<int:author_id>/books/', books_by_author_view, name='books_by_author'),

]
