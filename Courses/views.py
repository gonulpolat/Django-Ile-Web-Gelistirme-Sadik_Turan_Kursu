from datetime import date
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Course

data = {
    'programlama': 'Programlama Kategorisine Ait Kurslar',
    'web-gelistirme': 'Web Geliştirme Kategorisine Ait Kurslar',
    'mobil-uygulama': 'Mobil Uygulama Kategorisine Ait Kurslar',
}

db = {
    'courses': [
        {
            'title': 'JavaScript Kursu',
            'description': "JavaScript (genellikle JS olarak kısaltılır), HTML ve CSS ile birlikte World Wide Web'in temel teknolojilerinden biri olan programlama dilidir. Web sitelerinin %97'sinden fazlası, web sayfası hareketleri için istemci tarafında JavaScript kullanırlar ve kullanılan kodlar genellikle üçüncü taraf kitaplıkları içerir. Tüm büyük web tarayıcılarında, kaynak kodunu kullanıcıların cihazlarında yürütebilmek için özel bir JavaScript motoru bulunur.",
            'imageUrl': "1.jpeg",
            'slug': 'javascript-kursu',
            'date': date(2020, 7, 21),
            'isActive': True,
            'isUpdated': True
        },
        {
            'title': 'Python Kursu',
            'description': "Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli bir programlama dilidir.",
            'imageUrl': "2.jpeg",
            'slug': 'python-kursu',
            'date': date(2025, 7, 21),
            'isActive': True,
            'isUpdated': False
        },
        {
            'title': 'Java Kursu',
            'description': "Java, Sun Microsystems mühendislerinden James Gosling tarafından geliştirilmeye başlanmış açık kaynak kodlu, nesneye yönelik, platform bağımsız, yüksek verimli, çok işlevli, yüksek seviye, hem yorumlanan hem de derlenen bir dildir.",
            'imageUrl': "3.jpeg",
            'slug': 'java-kursu',
            'date': date(2021, 7, 21),
            'isActive': True,
            'isUpdated': True
        },
        {
            'title': 'PHP Kursu',
            'description': "PHP, açılımıyla Hypertext Preprocessor (çev. 'Üstünyazı Önişlemcisi') ya da eski açılımıyla Personal Home Page (çev. 'Kişisel Ana Sayfa'), internet için üretilmiş, sunucu taraflı, çok geniş kullanımlı, genel amaçlı, içerisine HTML gömülebilen betik ve programlama dilidir.",
            'imageUrl': "4.jpeg",
            'slug': 'php-kursu',
            'date': date(2023, 1, 10),
            'isActive': True,
            'isUpdated': False
        },
        {
            'title': 'Perl Kursu',
            'description': "Perl, bir dilbilimci olup NASA'da sistem yöneticisi olarak çalışan Larry Wall tarafından geliştirilmiş bir programlama dilidir. Yoğun şekilde metin işleme ve görüntü tanıma söz konusu olduğunda kullanılabilecek en güçlü ve pratik programlama dilidir.",
            'imageUrl': "5.jpeg",
            'slug': 'perl-kursu',
            'date': date(2024, 12, 12),
            'isActive': True,
            'isUpdated': True
        },
        {
            'title': 'ASP.NET Kursu',
            'description': "ASP.NET, Microsoft tarafından geliştirilmiş olan bir açık kaynak Web uygulama gelişimi teknolojisidir. Dinamik Web sayfaları, Web uygulamaları ve XML tabanlı Web hizmetleri geliştirilmesine olanak sağlar. Aynı işletme tarafından geliştirilen .NET çatısı'nın yazılım iskeleti parçası ve artık işletmece desteklenmeyen ASP teknolojisinin devamını teşkil etmiştir.",
            'imageUrl': "6.jpeg",
            'slug': 'aspnet-kursu',
            'date': date(2021, 1, 21),
            'isActive': True,
            'isUpdated': True
        },
        {
            'title': 'Django Kursu',
            'description': "Django, Python Programlama Dili için hazırlanmış ve BSD lisansı ile lisanslanmış yüksek seviyeli bir web çatısıdır. Basit kurulumu ve kullanımı, detaylı hata raporu sayfaları ve sunduğu yeni arayüz kodlama yöntemleriyle diğer sunucu yazılımı ve çatılardan kendini ayırmaktadır. İsmi, caz gitaristi Django Reinhardt'tan gelmektedir",
            'imageUrl': "7.jpeg",
            'slug': 'django-kursu',
            'date': date(2025, 2, 2),
            'isActive': True,
            'isUpdated': False
        },
        {
            'title': 'Node.js Kursu',
            'description': "Node.js, açık kaynaklı, genelde sunucu tarafında çalışan ve ağ bağlantılı uygulamalar için geliştirilmiş bir çalıştırma ortamıdır",
            'imageUrl': "8.jpeg",
            'slug': 'nodejs-kursu',
            'date': date(2023, 5, 18),
            'isActive': True,
            'isUpdated': True
        },
        {
            'title': 'Html Kursu',
            'description': "Hiper Metin İşaretleme Dili web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir. Dilin son sürümü HTML5'tir. HTML, bir programlama dili olarak tanımlanamaz. Çünkü HTML kodlarıyla kendi başına çalışan bir program yazılamaz.",
            'imageUrl': "9.jpeg",
            'slug': 'html-kursu',
            'date': date(2020, 7, 21),
            'isActive': True,
            'isUpdated': True
        },
        {
            'title': 'Css Kursu',
            'description': "Cascading Style Sheets, HTML'e ek olarak metin ve format biçimlendirme alanında fazladan olanaklar sunan bir işaretleme dilidir.",
            'imageUrl': "10.jpeg",
            'slug': 'css-kursu',
            'date': date(2025, 3, 4),
            'isActive': True,
            'isUpdated': True
        }
    ],
    'categories': [
        {
            'id': 1,
            'name': 'programlama',
            'slug': 'programlama'
        },
        {
            'id': 2,
            'name': 'web geliştirme',
            'slug': 'web-gelistirme'
        },
        {
            'id': 3,
            'name': 'mobil uygulama',
            'slug': 'mobil-uygulama'
        },
        {
            'id': 4,
            'name': 'veri bilimi',
            'slug': 'veri-bilimi'
        },
    ]
}

def index(request):
    courses = Course.objects.all()
    # courses = Course.objects.filter(isActive=1)     # template üserinde sorgu yazıyorum zaten
    categories = db['categories']     

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses
    })

def details(request, course_name):
    return HttpResponse(f'{course_name.capitalize()} Detay Sayfası')

def get_courses_by_category_name(request, category_name):
    try: 
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category': category_name,
            'category_text': category_text,
        })
    except:
        return HttpResponseNotFound('<h1>Yanlış Kategori Seçimi</h1>')

def get_courses_by_category_id(request, category_id):
    category_key_list = list(data.keys())
    if category_id > len(category_key_list):
        return HttpResponseNotFound('<h1>Yanlış Kategori Seçimi</h1>')
    category_name = category_key_list[category_id - 1]

    redirect_url = reverse('courses_by_category_name', args=[category_name])

    return redirect(redirect_url)