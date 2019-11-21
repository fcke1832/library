from django.db import migrations

from faker import Faker
fake = Faker()


def create_books(apps, schema_editor):
    Book = apps.get_model("books", "Book")
    Reader = apps.get_model("books", "Reader")
    db_alias = schema_editor.connection.alias
    for _ in range(1000):
        books_list = [Book(title=fake.sentence(nb_words=3)[:-1], author=fake.name()) for b in range(100)]
        readers_list = [Reader(name=fake.name()) for r in range(50)]
        Book.objects.using(db_alias).bulk_create(books_list)
        Reader.objects.using(db_alias).bulk_create(readers_list)


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_books, migrations.RunPython.noop),
    ]
