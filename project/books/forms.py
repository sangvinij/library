from .models import Reader

from django import forms


class CreateReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ("first_name", "last_name", "patronymic")
