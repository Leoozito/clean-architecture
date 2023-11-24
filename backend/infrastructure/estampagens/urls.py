from django.urls import path
from .views import home, create_new # update, delete

urlpatterns = [
    # path('delete/<int:id>', delete),
    # path('update/<int:id>', update),
    path('criar-novo', create_new),
    path('', home),
]