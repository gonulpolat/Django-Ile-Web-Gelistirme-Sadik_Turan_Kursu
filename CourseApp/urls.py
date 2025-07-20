"""CourseApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# http://127.0.0.1:8000/                                 => HTML SAYFASI
# http://127.0.0.1:8000/anasayfa                         => HTML SAYFASI
# http://127.0.0.1:8000/index                            => HTML SAYFASI
# http://127.0.0.1:8000/iletisim                         => HTML SAYFASI
# http://127.0.0.1:8000/hakkimizda                       => HTML SAYFASI
# http://127.0.0.1:8000/kurs                             => HTML SAYFASI
# http://127.0.0.1:8000/kurs/liste                       => Kurs Listesi
# http://127.0.0.1:8000/kurs/<>                          => <> Detay Sayfası
# http://127.0.0.1:8000/kurs/kategori/1                  => Programlama Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/2                  => Web Geliştirme Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/3                  => Mobil Uygulama Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/int:<>             => Yanlış Kategori Seçimi
# http://127.0.0.1:8000/kurs/kategori/programlama        => Programlama Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/web-gelistirme     => Web Geliştirme Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/mobil-uygulama     => Mobil Uygulama Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/str:<>                      => Yanlış Kategori Seçimi

urlpatterns = [
    path('', include('Pages.urls')),
    path('kurs/', include('Courses.urls')),
    path('admin/', admin.site.urls),
]
