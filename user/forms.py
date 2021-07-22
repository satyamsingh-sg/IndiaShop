from django import forms
from django.db.models import fields
from .models import Customers,STATE
from django.contrib.auth.models import User

class Account(forms.ModelForm):
   
    class Meta:
        model=User
        fields=["username","email","password"]

        widgets={
            'username':forms.TextInput(
                attrs={
                    'type':'eamil',
                    'class':'form-control',
                    'id':'inputEmail4',
                    'placeholder':'User Name Exmple Shopindia@12',
                    'name':'name',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'type':'email',
                    'class':'form-control',
                    'id':'inputEmail4',
                    'placeholder':'Email',
                }
            ),
            'password':forms.TextInput(
                attrs={
                    'type':'password',
                    'class':'form-control',
                    'id':'inputPassword4',
                    'placeholder':'Password',
                    'name':'pass1',
                }
            )
        }





class Address(forms.ModelForm):
    
    
    class Meta:
        model=Customers
        fields=['name','phone','locality','city','state','pincode']
        widgets={
            'name':forms.TextInput(
                attrs={
                    'type':'text',
                    'class':'form-control',
                   
                    'placeholder':'Name',
                    'name':'name',
                }
            ),
            'phone':forms.TextInput(
                attrs={
                    'type':'text',
                    'class':'form-control',
                   
                    'placeholder':'Phone',
                    'name':'name',
                }
            ),
            'locality':forms.TextInput(
                attrs={
                    'type':'text',
                    'class':'form-control',
                   
                    'placeholder':'Locality',
                    'name':'name',
                    
                }
            ),
            'city':forms.TextInput(
                attrs={
                    'type':'text',
                    'class':'form-control',
                   
                    'placeholder':'City',
                    'name':'name',
                }
            ),
            "state": forms.Select(attrs={
                'class': 'form-control',
                'name': 'State',
                'choices': STATE,
                'required': True
            }),
            'pincode':forms.TextInput(
                attrs={
                    'type':'number',
                    'class':'form-control',
                    
                    'placeholder':'pincode',
                    'name':'pass1',
                }
            )
        }





