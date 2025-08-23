from django.urls import path
from . views import (
    BookListView, 
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    UserListView,
    UserDetailView,
    StaffView,
)

urlpatterns = [
    # Book endpoint config
    path("books/", BookListView.as_view(), name="books"),
    path("books/<int:id>/", BookDetailView.as_view(), name="book-detail"),
    path("create/", BookCreateView.as_view(), name="book-create"),
    path("books/<pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("books/<pk>/delete/", BookDeleteView.as_view(), name="book-delete"),

    # User endpoints config
    path("users/", UserListView.as_view(), name="users"),
    path("users/<pk>/", UserDetailView.as_view(), name="user-detail"),
    path("staff/", StaffView.as_view(), name="staff"),
]