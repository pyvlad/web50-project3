from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')    # fields from User to be included in form

    def clean_password2(self):
        # This check is done when the form is validated via is_valid() method.
        # The clean_<fieldname>() method for any of form fields will be used to clean the value
        # or raise form validation errors for that field.
        # The general clean() method can be used to validate the entire form, which is useful to
        # validate fields that depend on each other.
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Password don't match.")
        return cd["password2"]
