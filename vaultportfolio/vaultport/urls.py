from django.urls import path
from . import views

app_name = "vaultport"

urlpatterns = [
    path('', views.intern, name='internship_portfolio'),
]