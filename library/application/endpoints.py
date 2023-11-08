from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AuthorSerializer, BookSerializer, PublishingSerializer
from .models import Author, Book, Publishing
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


# ListAPIView##################################
class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]


# CreateAPIView######################################
class AuthorCreateAPIView(CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAdminUser]


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]


# RUD #################################################
class AuthorRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAdminUser]


class BookRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]


# modelViewSet ##############################################
class PublishingAPIViewSet(ModelViewSet):
    serializer_class = PublishingSerializer
    queryset = Publishing.objects.all()
    permission_classes = [permissions.AllowAny]


# show authors for one publishing
class PublishingAuthorsAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        publishing = self.kwargs["id"]
        return Author.objects.filter(publishing_id=publishing)


