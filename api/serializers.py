from rest_framework import serializers

from api.models import Distrito, SubPrefeitura, Regiao, SubRegiao, Bairro, Feira


class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairro
        fields = "__all__"


class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = "__all__"


class SubPrefeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPrefeitura
        fields = "__all__"


class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = "__all__"


class SubRegiaoSerializer(serializers.ModelSerializer):
    regiao = RegiaoSerializer()

    class Meta:
        model = SubRegiao
        fields = "__all__"


class FeiraSerializer(serializers.ModelSerializer):
    bairro = BairroSerializer()
    distrito = DistritoSerializer()
    sub_pref = SubPrefeituraSerializer()
    sub_regiao = SubRegiaoSerializer()

    class Meta:
        model = Feira
        fields = "__all__"
