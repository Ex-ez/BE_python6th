from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BooksModelView.as_view(), name='index'),
    path('book/', views.BookList.as_view(), name='book_list'),
    path('author/', views.AuthorList.as_view(), name='author_list'),
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
]
