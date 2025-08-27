from rest_framework import serializers
from django.contrib.auth.models import User
from books . models import Book

#class BookListSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Book
   #     fields = ("title", "author",)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "email", "is_staff", "is_active",
        )