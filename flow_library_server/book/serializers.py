from rest_framework import serializers
from .models import Book, Author, Genre, Publisher, Tag


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model: Author = Author
        fields: str = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model: Genre = Genre
        fields: str = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model: Publisher = Publisher
        fields: str = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model: Tag = Tag
        fields: str = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author: AuthorSerializer = AuthorSerializer(many=True)
    tags: TagSerializer = TagSerializer(many=True)
    genre: GenreSerializer = GenreSerializer()
    publisher: PublisherSerializer = PublisherSerializer()

    class Meta:
        model: Book = Book
        fields: str = '__all__'
