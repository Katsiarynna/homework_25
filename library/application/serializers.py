from rest_framework import serializers
from .models import Author, Book, Publishing


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class PublishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishing
        fields = "__all__"
