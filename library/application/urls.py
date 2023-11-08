from django.urls import path, include
from .endpoints import AuthorListAPIView, BookListAPIView, \
    AuthorCreateAPIView, BookCreateAPIView, \
    AuthorRUDAPIView, BookRUDAPIView, \
    PublishingAPIViewSet, PublishingAuthorsAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("publishing", PublishingAPIViewSet)

urlpatterns = [
    # list
    path('author_list/', AuthorListAPIView.as_view(), name='author_list'),
    path('book_list/', BookListAPIView.as_view(), name='book_list'),
    # create
    path('author_create/', AuthorCreateAPIView.as_view(), name='author_create'),
    path('book_create/', BookCreateAPIView.as_view(), name='book_create'),
    # RUD
    path('author_rud/<ink:pk', AuthorRUDAPIView.as_view(), name='author_rud'),
    path('book_rud/<ink:pk', BookRUDAPIView.as_view(), name='book_rud'),
    # apiViewSet
    path("", include(router.urls), name="publishing_viewset"),
    # show authors for one publishing
    path("publishing/<int:id>/authors", PublishingAuthorsAPIView.as_view(), name="publishing_authors")
]
