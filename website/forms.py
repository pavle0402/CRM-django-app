from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

genders = [
     ('Male', 'Male'),
     ('Female', 'Female'),
     ('Other', 'Other')
]

class RegistrationForm(UserCreationForm):
        email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control-sm"}))
        first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={"class":"form-control-sm"}))
        last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={"class":"form-control-sm"}))
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

        #Instead of doing it in template(html) file 
        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control-sm'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = 'Username'
            self.fields['username'].help_text = '<span class="form-text text-muted"><small><br>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control-sm'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = 'Password'
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control-sm'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = 'Password confirm'
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small><br>Enter the same password as before, for verification.</small></span>'





class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Your first name.",
                                                                                      "class":"form-control"}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Your last name.",
                                                                                      "class":"form-control"}))
    email = forms.CharField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder":"Your contact email.",
                                                                                      "class":"form-control"}))
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Your phone number.",
                                                                                      "class":"form-control"}))
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Your address.",
                                                                                      "class":"form-control"}))
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City you live in.",
                                                                                      "class":"form-control"}))
    country =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Country you live in.",
                                                                                      "class":"form-control"}))
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode of your region.",
                                                                                      "class":"form-control"}))




    class Meta:
        model = Record 
        exclude = ("user", )

    

    # def clean_phone_number(self):
    #      clean_number = self.phone.cleaned_data()
    #      if clean_number == int():
    #         pass
    #      else:
    #           raise ValueError("Invalid form for phone number. Try again.")
              