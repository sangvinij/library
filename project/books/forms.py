from django import forms
from .models import Reader, Book


class CreateReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ("first_name", "last_name", "patronymic")
