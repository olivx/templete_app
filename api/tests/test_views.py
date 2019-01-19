import pytest
from django.urls import reverse
from model_mommy import mommy

from api.models import (Bairro, Distrito, Feira, Regiao, SubPrefeitura,
                        SubRegiao)


@pytest.mark.django_db
def test_list_distritos(api_client):
    mommy.make(Distrito, _quantity=10)
    resp = api_client.get(reverse("distrito-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_distrito_by_id(api_client, django_request):
    distrito = mommy.make(Distrito)
    resp = api_client.get(reverse("distrito-detail", args=([distrito.id])))

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(
            reverse("distrito-detail", args=([distrito.id]))
        )
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_list_sub_prefeituras(api_client):
    mommy.make(SubPrefeitura, _quantity=10)
    resp = api_client.get(reverse("subprefeitura-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_sub_prefeitura_by_id(api_client, django_request):
    sub_prefeitura = mommy.make(SubPrefeitura)
    resp = api_client.get(reverse("subprefeitura-detail", args=([sub_prefeitura.id])))

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(
            reverse("subprefeitura-detail", args=([sub_prefeitura.id]))
        )
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_list_regioes(api_client):
    mommy.make(Regiao, _quantity=10)
    resp = api_client.get(reverse("regiao-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_regiao_by_id(api_client, django_request):
    regiao = mommy.make(Regiao)
    resp = api_client.get(reverse("regiao-detail", args=([regiao.id])))

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(reverse("regiao-detail", args=([regiao.id])))
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_list_sub_regioes(api_client):
    mommy.make(SubRegiao, _quantity=10)
    resp = api_client.get(reverse("subregiao-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_sub_regiao_by_id(api_client, django_request):
    sub_regiao = mommy.make(SubRegiao)
    resp = api_client.get(reverse("subregiao-detail", args=([sub_regiao.id])))

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(
            reverse("subregiao-detail", args=([sub_regiao.id]))
        )
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_list_bairros(api_client):
    mommy.make(Bairro, _quantity=10)
    resp = api_client.get(reverse("bairro-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_bairro_by_id(api_client, django_request):
    bairro = mommy.make(Bairro)
    resp = api_client.get(reverse("bairro-detail", args=([bairro.id])))

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(reverse("bairro-detail", args=([bairro.id])))
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_list_feiras(api_client):
    mommy.make(Feira, _quantity=10)
    resp = api_client.get(reverse("feira-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_feira_by_id(api_client, django_request):
    feira = mommy.make(Feira)
    resp = api_client.get(reverse("feira-detail", args=([feira.id])))

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(reverse("feira-detail", args=([feira.id])))
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_create_feira(api_client):
    feira = mommy.prepare(Feira, registro="4041-0", _save_related=True)
    data = dict(
        nome=feira.nome,
        lat=feira.lat,
        long=feira.long,
        registro=feira.registro,
        areap=feira.areap,
        setcens=feira.setcens,
        logradouro=feira.logradouro,
        numero=feira.numero,
        referencia=feira.referencia,
        distrito_id=feira.distrito_id,
        sub_pref_id=feira.sub_pref_id,
        sub_regiao_id=feira.sub_regiao_id,
        bairro_id=feira.bairro_id,
    )
    resp = api_client.post(reverse("feira-list"), data=data, format="json")

    assert resp.status_code == 201
    assert Feira.objects.get(registro=data["registro"])


@pytest.mark.django_db
def test_create_feira_required_fields(api_client):
    data = {}
    resp = api_client.post(reverse("feira-list"), data=data, format="json")

    assert resp.status_code == 400
    assert resp.json() == {
        "bairro_id": ["This field is required."],
        "distrito_id": ["This field is required."],
        "sub_pref_id": ["This field is required."],
        "sub_regiao_id": ["This field is required."],
        "nome": ["This field is required."],
        "registro": ["This field is required."],
        "long": ["This field is required."],
        "lat": ["This field is required."],
        "setcens": ["This field is required."],
        "areap": ["This field is required."],
        "logradouro": ["This field is required."],
        "referencia": ["This field is required."],
    }


@pytest.mark.django_db
def test_query_feira_by_nome(api_client):
    feira = mommy.make(Feira)

    resp = api_client.get("%s?nome=%s" % (reverse("feira-list"), feira.nome))

    assert resp.status_code == 200
    assert resp.json()["results"][0]["nome"] == feira.nome


@pytest.mark.django_db
def test_query_feira_by_distrito(api_client):
    feira = mommy.make(Feira)

    resp = api_client.get(
        "%s?distrito=%s" % (reverse("feira-list"), feira.distrito.nome)
    )

    assert resp.status_code == 200
    assert resp.json()["results"][0]["nome"] == feira.nome


@pytest.mark.django_db
def test_query_feira_by_bairro(api_client):
    feira = mommy.make(Feira)

    resp = api_client.get("%s?bairro=%s" % (reverse("feira-list"), feira.bairro.nome))

    assert resp.status_code == 200
    assert resp.json()["results"][0]["nome"] == feira.nome


@pytest.mark.django_db
def test_query_feira_by_regiao(api_client):
    feira = mommy.make(Feira)

    resp = api_client.get(
        "%s?regiao=%s" % (reverse("feira-list"), feira.sub_regiao.regiao.nome)
    )

    assert resp.status_code == 200
    assert resp.json()["results"][0]["nome"] == feira.nome


@pytest.mark.django_db
def test_delete_feira(api_client):
    feira = mommy.make(Feira)
    assert len(Feira.objects.all()) == 1

    resp = api_client.delete(reverse("feira-detail", args=([feira.id])))

    assert resp.status_code == 204
    assert len(Feira.objects.all()) == 0


@pytest.mark.django_db
def test_patch_feira(api_client):
    feira = mommy.make(Feira)
    data = {"nome": "Feira do Carlos Blanka"}
    resp = api_client.patch(reverse("feira-detail", args=([feira.id])), data=data)

    assert resp.status_code == 200
    assert resp.json()["nome"] == data["nome"].upper()


@pytest.mark.django_db
def test_cannot_patch_feira_registro(api_client):
    feira = mommy.make(Feira)
    data = {"nome": "Feira do Carlos Blanka", "registro": "8979"}
    resp = api_client.patch(reverse("feira-detail", args=([feira.id])), data=data)

    assert resp.status_code == 400
    assert resp.json() == {"detail": "Cannot patch [registro] field"}


@pytest.mark.django_db
def test_cannot_put_feira(api_client):
    feira = mommy.make(Feira)
    data = {"nome": "Feira do Carlos Blanka", "registro": "8979"}
    resp = api_client.put(reverse("feira-detail", args=([feira.id])), data=data)

    assert resp.status_code == 405
    assert resp.json() == {"detail": 'Method "PUT" not allowed.'}
