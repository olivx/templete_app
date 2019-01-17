from django.urls import path
from api import views
from api.router import CustomRouter

# feiras_router = DefaultRouter()
feiras_router = CustomRouter(api_root=views.ApiRoot)
feiras_router.register(r"feiras", views.FeiraView, basename=views.FeiraView.name)

urlpatterns = [
    # path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path(
        "distritos/<int:pk>",
        views.DistritoRetrieveView.as_view(),
        name=views.DistritoRetrieveView.name,
    ),
    path(
        "distritos", views.DistritoListView.as_view(), name=views.DistritoListView.name
    ),
    path(
        "sub-prefeituras",
        views.SubPrefeituraListView.as_view(),
        name=views.SubPrefeituraListView.name,
    ),
    path(
        "sub-prefeituras/<int:pk>",
        views.SubPrefeituraRetrieveView.as_view(),
        name=views.SubPrefeituraRetrieveView.name,
    ),
    path(
        "regioes/<int:pk>",
        views.RegiaoRetrieveView.as_view(),
        name=views.RegiaoRetrieveView.name,
    ),
    path("regioes", views.RegiaoListView.as_view(), name=views.RegiaoListView.name),
    path(
        "sub-regioes/<int:pk>",
        views.SubRegiaoRetrieveView.as_view(),
        name=views.SubRegiaoRetrieveView.name,
    ),
    path(
        "sub-regioes",
        views.SubRegiaoListView.as_view(),
        name=views.SubRegiaoListView.name,
    ),
    path(
        "bairros/<int:pk>",
        views.BairroRetrieveView.as_view(),
        name=views.BairroRetrieveView.name,
    ),
    path("bairros", views.BairroListView.as_view(), name=views.BairroListView.name),
] + feiras_router.urls
