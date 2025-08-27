from django.urls import path
from . views import (
    BookListCreateView, 
    BookDetailUpdateDeleteView,
    #BookCreateView,
    #BookUpdateView,
    #BookDeleteView,
    UserListCreateView,
    UserDetailUpdateDeleteView,
    StaffView,
)

urlpatterns = [
    # Book endpoint config
    path("books/", BookListCreateView.as_view(), name="books"),
    path("books/<int:id>/", BookDetailUpdateDeleteView.as_view(), name="book-detail"),
    #path("create/", BookCreateView.as_view(), name="book-create"),
    #path("books/<pk>/update/", BookUpdateView.as_view(), name="book-update"),
    #path("books/<pk>/delete/", BookDeleteView.as_view(), name="book-delete"),

    # User endpoints config
    path("users/", UserListCreateView.as_view(), name="users"),
    path("users/<pk>/", UserDetailUpdateDeleteView.as_view(), name="user-detail"),
    path("staff/", StaffView.as_view(), name="staff"),
]