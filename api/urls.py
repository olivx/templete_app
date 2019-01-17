from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter(trailing_slash=False)
router.register(r"feiras", views.FeiraView, basename=views.FeiraView.name)
router.register(r"bairros", views.BairroViewSet, basename=views.BairroViewSet.name)
router.register(
    r"distritos", views.DistritoViewSet, basename=views.DistritoViewSet.name
)
router.register(
    r"sub-prefeituras",
    views.SubPrefeituraViewSet,
    basename=views.SubPrefeituraViewSet.name,
)
router.register(r"regioes", views.RegiaoViewSet, basename=views.RegiaoViewSet.name)
router.register(
    r"sub-regioes", views.SubRegiaoViewSet, basename=views.SubRegiaoViewSet.name
)

urlpatterns = router.urls
