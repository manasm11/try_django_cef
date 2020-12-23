from django import forms
from .models import NameModel

class NameForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.Textarea(attrs={
        "rows":2,
        "cols":40,
        "resize":"none"
    }))
    class Meta:
        model = NameModel
        fields = [
            "first_name",
            "last_name"
        ]
