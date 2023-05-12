from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

genders = [
     ('male', 'male'),
     ('female', 'female'),
     ('other', 'other')
]

class RegistrationForm(UserCreationForm):
        email = forms.EmailField()
        first_name = forms.CharField(max_length=255, required=True)
        last_name = forms.CharField(max_length=255, required=True)
        gender = forms.ChoiceField(choices=genders, widget=forms.Select(attrs={"class":"selector", "class":"form-control-sm"}))

        class Meta:
            model = User
            fields = ('first_name', 'last_name','gender', 'email','username', 'password1', 'password2')



            def clean_email(self):
                clean_email = self.email.cleaned_data()
                if "@" or ".com" not in clean_email:
                    raise ValueError("This form of email is not acceptable.")
                else:
                    pass