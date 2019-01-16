import pytest

from api.models import (Bairro, Distrito, Feira, Regiao, SubPrefeitura,
                        SubRegiao)
from api.serializers import (BairroSerializer, DistritoSerializer,
                             FeiraSerializer, RegiaoSerializer,
                             SubPrefeituraSerializer, SubRegiaoSerializer)


@pytest.mark.django_db
def test_deserialize_distrito():
    model = Distrito.objects.create(nome="Vila Formosa")
    serializer = DistritoSerializer(model)

    for f in model._meta.fields:
        assert f.name in serializer.data.keys()


@pytest.mark.django_db
def test_deserialize_sub_prefeitura():
    model = SubPrefeitura.objects.create(nome="Vila Prudente")
    serializer = SubPrefeituraSerializer(model)

    for f in model._meta.fields:
        assert f.name in serializer.data.keys()


@pytest.mark.django_db
def test_deserialize_regiao():
    model = Regiao.objects.create(nome="Leste")
    serializer = RegiaoSerializer(model)

    for f in model._meta.fields:
        assert f.name in serializer.data.keys()


@pytest.mark.django_db
def test_deserialize_sub_regiao():
    regiao = Regiao.objects.create(nome="Oeste")
    model = SubRegiao.objects.create(nome="Oeste 1", regiao=regiao)
    serializer = SubRegiaoSerializer(model)

    for f in model._meta.fields:
        assert f.name in serializer.data.keys()


@pytest.mark.django_db
def test_deserialize_bairro():
    model = Bairro.objects.create(nome="Bras")
    serializer = BairroSerializer(model)

    for f in model._meta.fields:
        assert f.name in serializer.data.keys()


@pytest.mark.django_db
def test_deserialize_feira():
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
    serializer = FeiraSerializer(model)

    for f in model._meta.fields:
        assert f.name in serializer.data.keys()


@pytest.mark.django_db
def test_serialize_feira():
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
        nome="Vila Formosa",
        registro="4041-0",
        logradouro="RUA MARAGOJIPE",
        numero="755",
        referencia="TV Rua Pretoria",
        distrito_id=distrito.id,
        sub_pref_id=sub_pref.id,
        sub_regiao_id=sub_regiao.id,
        bairro_id=bairro.id,
    )
    serializer = FeiraSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    assert Feira.objects.get(registro="4041-0")
