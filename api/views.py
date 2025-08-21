from rest_framework import generics

from . serializers import BookListSerializer, BookSerializer
from books . models import Book

class BookListView(generics.ListAPIView):
    """Get all the books"""
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

class BookDetailView(generics.RetrieveAPIView):
    """Get Detail of a book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"

class BookCreateView(generics.CreateAPIView):
    """Create new book view"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.RetrieveUpdateAPIView):
    """Update book view"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.RetrieveDestroyAPIView):
    """Delete a book for the database view"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
