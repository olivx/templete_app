import django_filters
from django_filters import rest_framework as filters

from api.models import Feira


class FeiraFilterSet(filters.FilterSet):
    distrito = django_filters.CharFilter(
        field_name="distrito", lookup_expr="nome__iexact"
    )
    bairro = django_filters.CharFilter(field_name="bairro", lookup_expr="nome__iexact")
    regiao = django_filters.CharFilter(
        field_name="sub_regiao", lookup_expr="regiao__nome__iexact"
    )

    class Meta:
        model = Feira
        fields = ["nome", "distrito", "bairro", "regiao"]
