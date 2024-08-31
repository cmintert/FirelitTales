from django import forms

class NodeForm(forms.Form):
    name = forms.CharField(max_length=100)
    label = forms.CharField(max_length=100)
    attributes = forms.CharField(widget=forms.Textarea)
    relations = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
