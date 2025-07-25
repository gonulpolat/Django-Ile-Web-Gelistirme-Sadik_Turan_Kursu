from django import forms

from Courses.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = '__all__'  # bütün alanlar gelir
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
                'max_length': 'Kurs adı en fazla 50 karakter içerebilir.',  # model üzerinde max_length 50 olarak tanımladığın için 50 karakterden fazla girmene izin vermiyor zaten
            },
            'description': {
                'required': 'Lütfen bir açıklama giriniz.',
            },
        }

