from django.db import models

class Book(models.Model):
    title = models.CharField("Title of book", max_length=200)
    author = models.CharField("Author", max_length=100)

    def __str__(self):
        return self.title


class Reader(models.Model):
    name = models.CharField("Full name", max_length=100)
    books = models.ManyToManyField(Book, related_name="readers", blank=True)

    def __str__(self):
        return self.name

