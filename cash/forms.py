from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cash
# UserCreationForm is Django built-in UserCreationForm
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

class CashForm(forms.ModelForm):

    class Meta:
        model = Cash

        fields = [
            "title",
            "amount",
            "transaction_type",
            "note",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "amount": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "transaction_type": forms.Select(attrs={
                "class": "form-select"
            }),

            "note": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
        }

