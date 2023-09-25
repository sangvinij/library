from django import forms

from .models import Reader


class CreateReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ("first_name", "last_name", "patronymic")
