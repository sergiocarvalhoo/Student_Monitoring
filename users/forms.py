from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    User._meta.get_field('first_name').blank = False
    User._meta.get_field('email').blank = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255}),
        }

    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
