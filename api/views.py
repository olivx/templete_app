from rest_framework import viewsets

from api.exceptions import CannotPatchApiException
from api.filters import FeiraFilterSet
from api.models import Bairro, Distrito, Feira, Regiao, SubPrefeitura, SubRegiao
from api.serializers import (
    BairroSerializer,
    DistritoSerializer,
    FeiraSerializer,
    RegiaoSerializer,
    SubPrefeituraSerializer,
    SubRegiaoSerializer,
)


class DistritoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer
    name = "distrito"


class SubPrefeituraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubPrefeitura.objects.all()
    serializer_class = SubPrefeituraSerializer
    name = "subprefeitura"


class RegiaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
    name = "regiao"


class SubRegiaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubRegiao.objects.all()
    serializer_class = SubRegiaoSerializer
    name = "subregiao"


class BairroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    name = "bairro"


class FeiraView(viewsets.ModelViewSet):
    queryset = Feira.objects.select_related(
        "bairro", "distrito", "sub_regiao", "sub_regiao__regiao", "sub_pref"
    ).all()
    serializer_class = FeiraSerializer
    name = "feira"
    http_method_names = ["get", "post", "head", "options", "patch", "delete"]
    filterset_fields = ("nome", "distrito", "bairro", "sub_regiao")
    filterset_class = FeiraFilterSet

    def partial_update(self, request, pk=None):
        if request.data.get("registro"):
            raise CannotPatchApiException("Cannot patch [registro] field")

        return super().partial_update(request, pk)
