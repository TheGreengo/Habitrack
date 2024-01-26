from django import forms

class UpdateNumForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class UpdateBinForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)