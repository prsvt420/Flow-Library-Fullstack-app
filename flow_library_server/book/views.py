from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Tag
from .serializers import BookSerializer, TagSerializer


class BookPagination(PageNumberPagination):
    page_size: int = 4
    page_query_param: str = 'page'


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset: QuerySet[Book] = Book.objects.all()
    serializer_class: BookSerializer = BookSerializer
    pagination_class: BookPagination = BookPagination

    def get_queryset(self) -> QuerySet[Book]:
        if 'tag' in self.request.query_params:
            return self.queryset.prefetch_related('tags').filter(tags__name=self.request.query_params['tag'])
        return self.queryset


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset: QuerySet[Tag] = Tag.objects.all()
    serializer_class: TagSerializer = TagSerializer


class BookCountView(APIView):
    @staticmethod
    def get(request) -> Response:
        return Response({"book_count": Book.objects.count()})
