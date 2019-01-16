from django.db import models


class Distrito(models.Model):
    nome = models.CharField(max_length=18)
    cod_dist = models.CharField(max_length=9, unique=True)


class SubPrefeitura(models.Model):
    nome = models.CharField(max_length=25)
    cod_sub_pref = models.CharField(max_length=2, unique=True)


class Regiao(models.Model):
    nome = models.CharField(max_length=6, unique=True)


class SubRegiao(models.Model):
    nome = models.CharField(max_length=7)
    regiao = models.ForeignKey(
        Regiao, related_name="sub_regioes", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("nome", "regiao")


class Bairro(models.Model):
    nome = models.CharField(max_length=20, unique=True)


class Feira(models.Model):
    nome = models.CharField(max_length=30)
    registro = models.CharField(max_length=6, unique=True)
    long = models.CharField(max_length=10)
    lat = models.CharField(max_length=10)
    setcens = models.CharField(max_length=15)
    areap = models.CharField(max_length=13)
    logradouro = models.CharField(max_length=34)
    numero = models.CharField(max_length=5)
    referencia = models.CharField(max_length=24)

    distrito = models.ForeignKey(
        Distrito, related_name="feiras", on_delete=models.CASCADE
    )
    sub_pref = models.ForeignKey(
        SubPrefeitura, related_name="feiras", on_delete=models.CASCADE
    )
    sub_regiao = models.ForeignKey(
        SubRegiao, related_name="feiras", on_delete=models.CASCADE
    )
    bairro = models.ForeignKey(Bairro, related_name="bairro", on_delete=models.CASCADE)
