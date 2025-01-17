from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from django.forms.fields import ChoiceField


# class RegisterTestForm(forms.Form):
#     # group = forms.ChoiceField()
#     group = forms.CharField(
#         max_length=30,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': "form-test",
#             'id': "inputGroup",
#             'placeholder': "Имя группы"
#         }),
#     )


class SignUpForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "login",
            'id': "inputUsername",
            'placeholder': "Имя пользователя"
        })
    )

    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "password",
            'id': "inputPassword",
            'placeholder': "Пароль"
        })
    )

    repeat_password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "repassword",
            'id': "reInputPassword",
            'placeholder': "Повторите пароль"
        })
    )

    group = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': "group",
            'id': "inputGroup",
            'placeholder': "Группа"
        })
    )

    def clean(self):
        """Если пароли не совпали очищаем поля и выкидываем исключение"""
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )
    
    def save(self):
        """Сохраняем в бд пользователя. Т.е регистрируем его"""
        user = User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class SignInForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "login",
            'id': "inputUsername",
            'placeholder': "Имя пользователя"
        })
    )

    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "password",
            'id': "inputPassword",
            'placeholder': "Пароль"
        })
    )


class ResultForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "login",
            'id': "inputUsername",
            'placeholder': "Имя пользователя"
        })
    )

    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "password",
            'id': "inputPassword",
            'placeholder': "Пароль"
        })
    )