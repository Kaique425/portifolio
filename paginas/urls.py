from django.urls import path
from . import views

app_name = "paginas"
urlpatterns = [
    path('', views.home, name='home'),
    path('projeto/<slug:slug>', views.projeto, name="projeto" )
]