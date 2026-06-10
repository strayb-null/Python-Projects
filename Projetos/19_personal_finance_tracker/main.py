import csv
import pandas as pd
from datetime import datetime

class CSV:
    ARQUIVO_CSV = "dados_financeiro.csv"
    COLUMNS = ["data", "valor", "categoria", "descricao"]

    @classmethod
    def inciar_csv(cls):
        try:
            pd.read_csv(cls.ARQUIVO_CSV)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.ARQUIVO_CSV, index=False)

    @classmethod
    def add_entrada(cls, data, valor, categoria, descricao):
        nova_entrada = {
            "data": data,
            "valor": valor,
            "categoria": categoria,
            "descricao" : descricao            
        }
        with open(cls.ARQUIVO_CSV, "a", newline="") as arquivocsv:
            writer = csv.DictWriter(arquivocsv, fieldnames=cls.COLUMNS)
            writer.writerow(nova_entrada)
        print("Entrada adicionada com sucesso!")

CSV.inciar_csv()
CSV.add_entrada("Teste", 100, "Teste", "Teste")