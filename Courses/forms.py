from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'Kurs adını girmek zorundasınız.'},
        )
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control'}))
