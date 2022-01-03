from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Help
from .models import profileForm
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_rider', 'is_driver')

class HelpForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "rows": "6"
            }
        )
    )

    class Meta:
        model = Help
        fields = ('comment',)

# GENDER_CHOICES = [
#  ('Male', 'Male'),
#  ('Female', 'Female')
# ]
# my_choices = (
#     ('one', 'Bike'),
#     ('two', 'Car'),
#     ('three', 'CNG'),
# )

class ProfileForm(forms.ModelForm):
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    # photo = forms.ImageField(label=('Licence'), required=False)
    # vehicle = forms.MultipleChoiceField(choices=my_choices)
    class Meta:
        model = profileForm
        # fields = '__all__'
        # exclude = ('user',)
        fields = ['phoneNumber', 'address', 'licence', 'nidNo', 'plateNo', 'vehicle']
        # labels = {'userName':'User Name', 'email':'Enter Your Email', 'phoneNumber':'+880', 'address':'Dhanmondi, Dhaka', 'licence':'1234...', 'nidNo':'1234...', 'plateNo':'1234...', 'vehicle':'car'}

        widgets = {
            # 'userName': forms.TextInput(attrs={'class': 'form-control'}),
            # # 'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'licence': forms.TextInput(attrs={'class': 'form-control'}),
            'nidNo': forms.TextInput(attrs={'class': 'form-control'}),
            'plateNo': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle': forms.TextInput(attrs={'class': 'form-control'}),
            # 'photo': forms.TextInput(attrs={'class': 'form-control'}),
        }
