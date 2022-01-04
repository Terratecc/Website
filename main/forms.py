from django import forms
from .models import *	

class ContactForm(forms.Form):
	name = forms.CharField(label = "name")
	email = forms.EmailField(label = "email")
	subject = forms.CharField(label="subject")	
	budget = forms.CharField(label= "budget")
	message = forms.CharField(label= "message")


