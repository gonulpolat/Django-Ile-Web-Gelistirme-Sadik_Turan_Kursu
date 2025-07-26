from django import forms

from Courses.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'imageUrl', 'slug')
        labels = {
            'title': 'Kurs Adı',
            'description': 'Açıklama',
            'imageUrl': 'Resim URLsi',
            'slug': 'Slug',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'imageUrl': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'title': {
                'required': 'Lütfen kurs adını giriniz.',
                'max_length': 'Kurs adı en fazla 50 karakter içerebilir.',
            },
            'description': {
                'required': 'Lütfen bir açıklama giriniz.',
            },
        }


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'imageUrl', 'slug', 'categories', 'isActive', 'isHome')
        labels = {
            'title': 'Kurs Adı',
            'description': 'Açıklama',
            'imageUrl': 'Resim URLsi',
            'slug': 'Slug',
            'categories': 'Kategoriler',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'imageUrl': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'title': {
                'required': 'Lütfen kurs adını giriniz.',
                'max_length': 'Kurs adı en fazla 50 karakter içerebilir.',
            },
            'description': {
                'required': 'Lütfen bir açıklama giriniz.',
            },
        }

    
class UploadForm(forms.Form):
    image = forms.ImageField()
