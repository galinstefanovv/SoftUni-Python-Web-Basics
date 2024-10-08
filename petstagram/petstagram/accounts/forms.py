from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    username = forms.TextInput(
        attrs={
            'class': 'ala-bala'
        }
    )


# Create your views here.
class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
