from django import forms
from authors.models import Authors


# class AuthorForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100, required=True)
#     image = forms.ImageField(label='Image', required=True)
#     birth_date = forms.DateField(label='Birth Date',
#                                  widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=True)
#

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters ")
        return name
