from django.urls import path
from . import views

app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>", views.detail, name="blog_detail"),
    path('signup/', views.signup, name='signup'),
]