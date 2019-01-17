from collections import OrderedDict

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import APIRootView

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

from django.urls import NoReverseMatch


# class ApiRoot(generics.GenericAPIView):
class ApiRoot(APIRootView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        urls = OrderedDict()
        urls = {
            "distritos": reverse(DistritoListView.name, request=request),
            "sub-prefeituras": reverse(SubPrefeituraListView.name, request=request),
            "regioes": reverse(RegiaoListView.name, request=request),
            "sub-regioes": reverse(SubRegiaoListView.name, request=request),
            "bairros": reverse(BairroListView.name, request=request),
        }
        namespace = request.resolver_match.namespace
        for key, url_name in self.api_root_dict.items():
            if namespace:
                url_name = namespace + ":" + url_name
            try:
                urls[key] = reverse(
                    url_name,
                    args=args,
                    kwargs=kwargs,
                    request=request,
                    format=kwargs.get("format", None),
                )
            except NoReverseMatch:
                # Don't bail out if eg. no list routes exist, only detail routes.
                continue

        return Response(urls)


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
    http_method_names = ["get", "post", "head", "options", "patch", "delete"]
    filterset_fields = ("nome", "distrito", "bairro", "sub_regiao")
    filterset_class = FeiraFilterSet

    def partial_update(self, request, pk=None):
        if request.data.get("registro"):
            raise CannotPatchApiException("Cannot patch [registro] field")

        return super().partial_update(request, pk)


FeiraListView = FeiraView.as_view({"get": "list"})
