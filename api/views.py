from rest_framework import generics, permissions
from django.contrib.auth.models import User

from . serializers import BookSerializer, UserSerializer
from books . models import Book

class BookListCreateView(generics.ListCreateAPIView):
    """Get all and create new books"""
    permission_classes = [permissions.AllowAny,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    page_size = 3

class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Get Detail, Update, and Delete a book"""
    permission_classes = [permissions.AllowAny,]    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"

#class BookCreateView(generics.CreateAPIView):
#    """Create new book view"""
#    permission_classes = [permissions.IsAdminUser,]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

#class BookUpdateView(generics.RetrieveUpdateAPIView):
#    """Update book view"""
#    permission_classes = [permissions.IsAdminUser,]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

#class BookDeleteView(generics.RetrieveDestroyAPIView):
#    """Delete a book for the database view"""
#    permission_classes = [permissions.IsAdminUser,]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

    # Users views

class UserListCreateView(generics.ListCreateAPIView):
    """List and Create of users"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    page_size = 3

class UserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """User details, update, and delets"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StaffView(generics.ListAPIView):
    """List of Staffs"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
