from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(label="Kurs Adı", error_messages={
        'required': 'Kurs adını girmek zorundasınız.'
    })
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    date = forms.DateField()
    slug = forms.SlugField()
