from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import News


class BlogModelForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "image"]

    def __init__(self, *args, **kwargs):
        super(BlogModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].help_text = ""
        self.fields["title"].label = ""
        self.fields["title"].widget = forms.Textarea(
            attrs={
                "placeholder": "Название новости",
                "rows": 1,
                "class": "form-control",
            }
        )

        self.fields["content"].help_text = ""
        self.fields["content"].label = ""
        self.fields["content"].widget = forms.Textarea(
            attrs={
                "placeholder": "Содержание",
                "rows": 10,
                "class": "form-control",
            }
        )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')