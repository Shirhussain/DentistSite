from django.urls import path
from .views import home, contact

app_name = "dental"
urlpatterns = [
    path('', home, name = "home"),
    path('contact/', contact, name = "contact"),
]

