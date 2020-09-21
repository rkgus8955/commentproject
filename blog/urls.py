from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('write/', views.write, name='write'),
]