from rest_framework import serializers

from api.models import Bairro, Distrito, Feira, Regiao, SubPrefeitura, SubRegiao


class BairroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bairro
        fields = "__all__"


class DistritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distrito
        fields = "__all__"


class SubPrefeituraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubPrefeitura
        fields = "__all__"


class RegiaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regiao
        fields = "__all__"


class SubRegiaoSerializer(serializers.HyperlinkedModelSerializer):
    regiao_id = serializers.IntegerField(write_only=True)
    regiao = RegiaoSerializer(read_only=True)

    class Meta:
        model = SubRegiao
        fields = "__all__"


class FeiraSerializer(serializers.HyperlinkedModelSerializer):
    bairro = BairroSerializer(read_only=True)
    distrito = DistritoSerializer(read_only=True)
    sub_pref = SubPrefeituraSerializer(read_only=True)
    sub_regiao = SubRegiaoSerializer(read_only=True)

    bairro_id = serializers.IntegerField(write_only=True)
    distrito_id = serializers.IntegerField(write_only=True)
    sub_pref_id = serializers.IntegerField(write_only=True)
    sub_regiao_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Feira
        fields = "__all__"
