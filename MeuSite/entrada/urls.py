from django.urls import path
from entrada import views

app_name = "entrada"

urlpatterns = [
    path("", views.home, name='home'),
]