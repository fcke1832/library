import random
from django.db import migrations
from django.db.models import Max

from books.models import Book, Reader


def get_random_book():
    max_id = Book.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        try:
            book = Book.objects.filter(pk=pk)[0]
        except:
            continue
        if book:
            return book

def create_relations(apps, schema_editor):
        for reader in Reader.objects.all():
            count_of_books = random.randint(1, 3)
            books_list = []
            for _ in range(count_of_books):
                books_list.append(get_random_book())
            reader.books.add(*books_list)


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20191120_1733'),
    ]

    operations = [
        migrations.RunPython(create_relations, migrations.RunPython.noop)
    ]
