from django.urls import path, include
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name="index"),
    path('view-up/<int:pk>/', views.views_up, name="views_up"),
    path('blog-detail/<int:pk>/', views.article_single, name="single"),
    path('blog/', views.article_view, name="blog-list"),

    path('api/', include('apps.articles.api.urls'))

]
