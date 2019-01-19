import pytest

from api.models import (Bairro, Distrito, Feira, Regiao, SubPrefeitura,
                        SubRegiao)
from api.serializers import (BairroSerializer, DistritoSerializer,
                             FeiraSerializer, RegiaoSerializer,
                             SubPrefeituraSerializer, SubRegiaoSerializer)


@pytest.mark.django_db
def test_deserialize_distrito(django_request):
    model = Distrito.objects.create(nome="Vila Formosa")
    serializer = DistritoSerializer(model, context={"request": django_request})

    for f in model._meta.fields:
        assert f.name in serializer.data.keys() if f.name != "id" else True


@pytest.mark.django_db
def test_deserialize_sub_prefeitura(django_request):
    model = SubPrefeitura.objects.create(nome="Vila Prudente")
    serializer = SubPrefeituraSerializer(model, context={"request": django_request})

    for f in model._meta.fields:
        assert f.name in serializer.data.keys() if f.name != "id" else True


@pytest.mark.django_db
def test_deserialize_regiao(django_request):
    model = Regiao.objects.create(nome="Leste")
    serializer = RegiaoSerializer(model, context={"request": django_request})

    for f in model._meta.fields:
        assert f.name in serializer.data.keys() if f.name != "id" else True


@pytest.mark.django_db
def test_deserialize_sub_regiao(django_request):
    regiao = Regiao.objects.create(nome="Oeste")
    model = SubRegiao.objects.create(nome="Oeste 1", regiao=regiao)
    serializer = SubRegiaoSerializer(model, context={"request": django_request})

    for f in model._meta.fields:
        assert f.name in serializer.data.keys() if f.name != "id" else True


@pytest.mark.django_db
def test_deserialize_bairro(django_request):
    model = Bairro.objects.create(nome="Bras")
    serializer = BairroSerializer(model, context={"request": django_request})

    for f in model._meta.fields:
        assert f.name in serializer.data.keys() if f.name != "id" else True


@pytest.mark.django_db
def test_deserialize_feira(django_request):
    distrito = Distrito.objects.create(nome="Vila Formosa")
    sub_pref = SubPrefeitura.objects.create(nome="Vila Prudente")
    regiao = Regiao.objects.create(nome="Oeste")
    sub_regiao = SubRegiao.objects.create(nome="Oeste 1", regiao=regiao)
    bairro = Bairro.objects.create(nome="Bras")
    model = Feira.objects.create(
        long="-46550164",
        lat="-23558733",
        setcens="355030885000091",
        areap="3550308005040",
        nome="Vila Formosa",
        registro="4041-0",
        logradouro="RUA MARAGOJIPE",
        numero="755",
        referencia="TV Rua Pretoria",
        distrito=distrito,
        sub_pref=sub_pref,
        sub_regiao=sub_regiao,
        bairro=bairro,
    )
    serializer = FeiraSerializer(model, context={"request": django_request})

    for f in model._meta.fields:
        assert f.name in serializer.data.keys() if f.name != "id" else True


@pytest.mark.django_db
def test_serialize_feira_uppercase(django_request):
    distrito = Distrito.objects.create(nome="Vila Formosa")
    sub_pref = SubPrefeitura.objects.create(nome="Vila Prudente")
    regiao = Regiao.objects.create(nome="Oeste")
    sub_regiao = SubRegiao.objects.create(nome="Oeste 1", regiao=regiao)
    bairro = Bairro.objects.create(nome="Bras")
    data = dict(
        long="-46550164",
        lat="-23558733",
        setcens="355030885000091",
        areap="3550308005040",
        nome="vila formosa",
        registro="4041-0",
        logradouro="rua maragojipe",
        numero="755",
        referencia="tv rua pretoria",
        distrito_id=distrito.id,
        sub_pref_id=sub_pref.id,
        sub_regiao_id=sub_regiao.id,
        bairro_id=bairro.id,
    )
    serializer = FeiraSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    feira = Feira.objects.get(registro="4041-0")
    assert feira.logradouro == "RUA MARAGOJIPE"
    assert feira.referencia == "TV RUA PRETORIA"
    assert feira.nome == "VILA FORMOSA"
