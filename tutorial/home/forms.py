from django import forms
from home.models import Post


#class HomeForm(forms.Form):
class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post.....'

        }
    )) # to make this required field as optional pass "required=False" in the parameters

    class Meta:
        model = Post   # linking
        fields = {'post',}