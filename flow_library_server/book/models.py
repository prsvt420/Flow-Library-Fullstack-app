from django.db import models


class Book(models.Model):
    objects = None
    title: str = models.CharField(max_length=100)
    description: str = models.TextField(blank=True, null=True)
    year: int = models.IntegerField()
    author: 'Author' = models.ManyToManyField(to='Author')
    genre: 'Genre' = models.ForeignKey('Genre', on_delete=models.CASCADE)
    publisher: 'Publisher' = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    isbn: str = models.CharField(max_length=30)
    quantity_pages: int = models.IntegerField()
    image: str = models.ImageField(upload_to='book_images', blank=True, null=True)
    file: str = models.FileField(upload_to='book_files', blank=True, null=True)
    tags: 'Tag' = models.ManyToManyField(to='Tag', blank=True)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    objects = None
    name: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Publisher(models.Model):
    name: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
