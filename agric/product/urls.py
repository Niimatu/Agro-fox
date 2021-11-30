from django . urls import path
from . import views
from .views import farmers

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("farmers/", farmers.as_view(), name="farmers"),
    path("services/", views.services, name="services"),
    path("lands/", views.lands, name="lands")
]
