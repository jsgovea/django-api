from django.urls import path

from . import views

urlpatterns = [
    path("planets/", views.planet_list, name="planets"),
    path("get-query/", views.get_query, name="get-query"),
    path("planet/<int:pk>/", views.planet_detail, name="planet-detail"),
    path("planet/delete/<int:pk>/", views.delete_planet, name="delete-planet"),
]
