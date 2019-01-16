import pandas as pd
from django.core.management import BaseCommand

from api.models import (Bairro, Distrito, Feira, Regiao, SubPrefeitura,
                        SubRegiao)


class Command(BaseCommand):
    def handle(self, *args, **options):
        df = pd.read_csv(options["file"])

        self.create_distritos(df[["CODDIST", "DISTRITO"]])
        self.create_sub_prefeituras(df[["CODSUBPREF", "SUBPREFE"]])
        self.create_regioes(df[["REGIAO5"]])
        self.create_sub_regioes(df[["REGIAO5", "REGIAO8"]])
        self.create_bairros(df[["BAIRRO"]])
        self.create_feiras(
            df[
                [
                    "LONG",
                    "LAT",
                    "SETCENS",
                    "AREAP",
                    "CODDIST",
                    "CODSUBPREF",
                    "REGIAO8",
                    "NOME_FEIRA",
                    "REGISTRO",
                    "LOGRADOURO",
                    "NUMERO",
                    "BAIRRO",
                    "REFERENCIA",
                ]
            ]
        )

    def create_distritos(self, df):
        unique_distritos = df.drop_duplicates()
        unique_distritos.columns = ["cod_dist", "nome"]

        for _, row in unique_distritos.iterrows():
            row = self.to_upper(row)
            Distrito.objects.create(**row)

    def create_sub_prefeituras(self, df):
        unique_sub_prefs = df.drop_duplicates()
        unique_sub_prefs.columns = ["cod_sub_pref", "nome"]

        for _, row in unique_sub_prefs.iterrows():
            row = self.to_upper(row)
            SubPrefeitura.objects.create(**row)

    def create_regioes(self, df):
        unique_regioes = df.drop_duplicates()
        unique_regioes.columns = ["nome"]

        for _, row in unique_regioes.iterrows():
            row = self.to_upper(row)
            Regiao.objects.create(**row)

    def create_sub_regioes(self, df):
        unique_sub_regioes = df.drop_duplicates()
        unique_sub_regioes.columns = ["regiao", "nome"]

        for _, row in unique_sub_regioes.iterrows():
            row = self.to_upper(row)
            row["regiao"] = Regiao.objects.get(nome=row["regiao"])
            SubRegiao.objects.create(**row)

    def create_bairros(self, df):
        unique_bairros = df.drop_duplicates()
        unique_bairros.columns = ["nome"]

        for _, row in unique_bairros.iterrows():
            row = self.to_upper(row)
            Bairro.objects.create(**row)

    def create_feiras(self, df):
        unique_feiras = df.drop_duplicates(subset=("REGISTRO"))
        unique_feiras.columns = [
            "long",
            "lat",
            "setcens",
            "areap",
            "distrito",
            "sub_pref",
            "sub_regiao",
            "nome",
            "registro",
            "logradouro",
            "numero",
            "bairro",
            "referencia",
        ]

        for _, row in unique_feiras.iterrows():
            row = self.to_upper(row)
            row["numero"] = self.parse_number(row["numero"])
            row["distrito"] = Distrito.objects.get(cod_dist=row["distrito"])
            row["sub_pref"] = SubPrefeitura.objects.get(cod_sub_pref=row["sub_pref"])
            row["sub_regiao"] = SubRegiao.objects.get(nome=row["sub_regiao"])
            row["bairro"] = Bairro.objects.get(nome=row["bairro"])
            row["referencia"] = row["referencia"][
                : Feira._meta.get_field("referencia").max_length
            ]
            Feira.objects.create(**row)

    def to_upper(self, row):
        return {k: str(v).upper().strip() for k, v in row.items()}

    def parse_number(self, nb):
        try:
            return str(int(float(nb)))
        except ValueError:
            return str(nb)

    def add_arguments(self, parser):
        parser.add_argument("-f", action="store", dest="file", help="""File location""")
