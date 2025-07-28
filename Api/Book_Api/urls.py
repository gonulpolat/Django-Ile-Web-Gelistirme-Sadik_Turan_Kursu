from django.urls import path
from .  import views

urlpatterns = [
    # path('create/', views.book_create),
    # path('list/', views.book_list),
    path('', views.books),
    # path('<int:id>', views.book_get),
    # path('update/<int:id>', views.book_update),
    # path('delete/<int:id>', views.book_delete),
    path('<int:id>', views.book),
]

# localhost/books        => GET, POST
# localhost/books/<int>  => GET, PUT, DELETE