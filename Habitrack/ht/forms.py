from django import forms

class UpdateNumForm(forms.Form):
    date = forms.DateField()
    res = forms.BooleanField()

class UpdateBinForm(forms.Form):
    date = forms.DateField()
    res = forms.FloatField()