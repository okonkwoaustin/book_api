from rest_framework.generics import ListAPIView, RetrieveAPIView

from . serializers import BookListSerializer, BookDetailSerializer
from books . models import Book

class BookListView(ListAPIView):
    """Get all the books"""
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

class BookDetailView(RetrieveAPIView):
    """Get Detail of a book"""
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = "id"
