from django.urls import path
from .views import article_list, article_create, article_detail, article_update, article_delete


urlpatterns = [
    path('list/', article_list),
    path('create/', article_create),
    path('<int:pk>/', article_detail),
    path('edit/<int:pk>/', article_update),
    path('delete/<int:pk>/', article_delete),
]

