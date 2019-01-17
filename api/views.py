from rest_framework import generics, viewsets
from api.models import Distrito, SubPrefeitura, SubRegiao, Regiao, Feira, Bairro
from api.exceptions import CannotPatchApiException
from api.serializers import (
    DistritoSerializer,
    SubPrefeituraSerializer,
    RegiaoSerializer,
    FeiraSerializer,
    BairroSerializer,
    SubRegiaoSerializer,
)


class DistritoListView(generics.ListAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer
    name = "distrito-list"


class DistritoRetrieveView(generics.RetrieveAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer
    name = "distrito-detail"


class SubPrefeituraListView(generics.ListAPIView):
    queryset = SubPrefeitura.objects.all()
    serializer_class = SubPrefeituraSerializer
    name = "sub-prefeitura-list"


class SubPrefeituraRetrieveView(generics.RetrieveAPIView):
    queryset = SubPrefeitura.objects.all()
    serializer_class = SubPrefeituraSerializer
    name = "sub-prefeitura-detail"


class RegiaoListView(generics.ListAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
    name = "regiao-list"


class RegiaoRetrieveView(generics.RetrieveAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
    name = "regiao-detail"


class SubRegiaoListView(generics.ListAPIView):
    queryset = SubRegiao.objects.all()
    serializer_class = SubRegiaoSerializer
    name = "sub-regiao-list"


class SubRegiaoRetrieveView(generics.RetrieveAPIView):
    queryset = SubRegiao.objects.all()
    serializer_class = SubRegiaoSerializer
    name = "sub-regiao-detail"


class BairroListView(generics.ListAPIView):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    name = "bairro-list"


class BairroRetrieveView(generics.RetrieveAPIView):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    name = "bairro-detail"


class FeiraView(viewsets.ModelViewSet):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer
    name = "feira"
    http_method_names = ["get", "post", "head", "options", "patch"]

    def partial_update(self, request, pk=None):
        if request.data.get("registro"):
            raise CannotPatchApiException("Cannot patch registro field")
        super().partial_update()
