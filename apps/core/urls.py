from django.urls import path
from .views import home, session_expired

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("session_expired/", session_expired, name="session_expired") 
]
