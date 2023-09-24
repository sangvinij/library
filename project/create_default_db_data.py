import contextlib

import django

import os

from django.contrib.auth import get_user_model

from project.config.env_config import env

os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"
from django.conf import settings

if not settings.configured:
    django.setup()

from books.models import Author, Book

User = get_user_model()


def create_superuser_for_admin_panel():
    User.objects.create_superuser(username=env.SUPERUSER_USERNAME, password=env.SUPERUSER_PASSWORD)


def create_authors():
    Author(first_name="Alexander", last_name="Pushkin", patronymic="Sergeevich").save()
    Author(first_name="Vladimir", last_name="Mayakovski", patronymic="Vladimirovich").save()
    Author(first_name="Michail", last_name="Lermontov", patronymic="Yurievich").save()


def create_books():
    authors = Author.objects.all()
    for author in authors:
        Book(title=f"{author}'s book", author=author).save()


if __name__ == "__main__":
    with contextlib.suppress(django.db.utils.IntegrityError):
        create_superuser_for_admin_panel()

    all_books = Book.objects.all()
    if len(all_books) == 0:
        with contextlib.suppress(django.db.utils.IntegrityError):
            create_authors()
            create_books()
