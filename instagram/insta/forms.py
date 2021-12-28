from django import forms

class Form(forms.Form):
	text = forms.CharField(max_length=50)
	sessionid = forms.CharField(max_length=40)
	