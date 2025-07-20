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

# http://127.0.0.1:8000/                        => Anasayfa
# http://127.0.0.1:8000/anasayfa                => Anasayfa
# http://127.0.0.1:8000/iletisim                => İletişim Sayfası
# http://127.0.0.1:8000/hakkimizda              => Hakkımızda Sayfası
# http://127.0.0.1:8000/kurs                    => Kurs Listesi
# http://127.0.0.1:8000/kurs/liste              => Kurs Listesi
# http://127.0.0.1:8000/kurs/detay              => Kurs Detay Sayfası
# http://127.0.0.1:8000/kurs/programlama        => Programlama Sayfası
# http://127.0.0.1:8000/kurs/mobil-uygulamalar  => Mobil Uygulama Sayfası

urlpatterns = [
    path('', include('Pages.urls')),
    path('kurs/', include('Courses.urls')),
    path('admin/', admin.site.urls),
]
