from django import forms
from .models import Users
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(label="Parol", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Parolni tasdiqlash", widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ('full_name', 'phone_number', 'username', 'password', 'password2', 'staff', 'data_viewer', 'data_add')
    
    def clean_username(self):
        u_name = self.cleaned_data['username']
        qs = Users.objects.filter(username = u_name)
        if qs.exists():
            raise forms.ValidationError("Bu username allaqon tanlangan")
        return u_name
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password2 is not None and password != password2:
            raise forms.ValidationError("Parolni tasdiqlashda xatolik bo'lishi mumkun")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label="Parol", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Parolni tasdiqlash", widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ('full_name', 'phone_number', 'username', 'password', 'password2')
    
    def clean_username(self):
        u_name = self.cleaned_data['username']
        qs = Users.objects.filter(username = u_name)
        if qs.exists():
            raise forms.ValidationError("Bu username allaqon tanlangan")
        return u_name
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password2 is not None and password != password2:
            raise forms.ValidationError("Parolni tasdiqlashda xatolik bo'lishi mumkun")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = Users
        fields = ('username', 'password', 'is_active', 'superuser')
    def clean_password(self):
        return self.initial['password']