from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput,PasswordInput,EmailInput
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import widgets



class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=["username", "password"]
        widgets={
            "username": forms.TextInput(attrs={
                "class": "form-control", 'placeholder':"Enter username"
            }),
            "password": forms.TextInput(attrs={ "class": "form-control", 'placeholder':"Enter password", 'type': "password"
            })
        }


class RregisterForm(ModelForm):
    class Meta:
        model=User
        fields=["username", "email","password"]
        widgets={
            "username": forms.TextInput(attrs={
                "class": "form-control", 'placeholder':"Enter username"
            }),
            "password": forms.TextInput(attrs={ "class": "form-control", 'placeholder':"Enter password", 'type': "password"
            }),
             "email": forms.TextInput(attrs={ "class": "form-control", 'placeholder':"Enter email", 'type': "email"
            })
        }
    

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})


class UserUpdateInfoForm(forms.Form):
    username= forms.CharField(max_length=50, required=False, label='Username', widget=TextInput(attrs={"class":"form-control","type":"text","placeholder":"Username"})) 
    email= forms.EmailField(label='Email', required=False, widget=EmailInput(attrs={"class":"form-control","type":"email","placeholder":"Email address"})) 
    first_name= forms.CharField(label='Name', required=False, widget=TextInput(attrs={"class":"form-control","type":"text","placeholder":"Name"}))
    last_name= forms.CharField(label='Surname', required=False, widget=TextInput(attrs={"class":"form-control","type":"text","placeholder":"Surname"}))