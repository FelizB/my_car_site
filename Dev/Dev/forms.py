from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name= forms.CharField(label='Lat Name', max_length=30)
    email= forms.EmailField(label='Email')
    review= forms.CharField(label='Review', max_length=500)
