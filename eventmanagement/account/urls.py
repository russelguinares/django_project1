
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('account/', views.login_view, name='login'),
]