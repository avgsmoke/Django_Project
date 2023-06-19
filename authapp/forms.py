from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from authapp.models import User

from django import forms


class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'
            item.help_text = ''

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'password1',
            'password2'
        )
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for name, item in self.fields.items():
                item.widget.attrs['class'] = 'form-control'
                item.help_text = ''

