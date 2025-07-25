from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    date = forms.DateField()
    slug = forms.SlugField()
