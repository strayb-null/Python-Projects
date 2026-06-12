import csv
import pandas as pd
from datetime import datetime
from data_entry import get_data, get_valor, get_categoria, get_descricao

class CSV:
    ARQUIVO_CSV = "dados_financeiro.csv"
    COLUMNS = ["data", "valor", "categoria", "descricao"]
    FORMATO = "%d-%m-%Y"

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

    @classmethod
    def get_lancamentos(cls, data_inicial, data_final):
        df = pd.read_csv(cls.ARQUIVO_CSV)
        df["data"] = pd.to_datetime(df["data"], format=CSV.FORMATO )
        data_inicial = datetime.strptime(data_inicial, CSV.FORMATO)
        data_final = datetime.strptime(data_final, CSV.FORMATO)

        mask = (df["data"] >= data_inicial) & (df["data"] <= data_final)
        df_filtrado = df.loc[mask]

        if df_filtrado.empty:
            print("Nenhum lançamento encontrado nesse período")
        else:
            print(f"Lançamentos de {data_inicial.strftime(CSV.FORMATO)} até {data_final.strftime(CSV.FORMATO)}")
            
            print(df_filtrado.to_string(
                index=False, formatters={"data": lambda x: x.strftime(CSV.FORMATO)}
            ))

        ganhos_total = df_filtrado[df_filtrado["categoria"] == "Ganhos"]["valor"].sum()
        despesas_total = df_filtrado[df_filtrado["categoria"] == "Despesas"]["valor"].sum()
        print("\nResumo Financeiro")
        print(f"Total de ganhos: R${ganhos_total:.2f}")
        print(f"Total de despesas: R${despesas_total:.2f}")
        print(f"Saldo: R${(ganhos_total - despesas_total):.2f}")

        return df_filtrado


def add():
    CSV.inciar_csv()
    data = get_data(
        "Digite a data do lançamento (mm-dd-yyy) ou deixe em branco e aperte enter para inserir a data de hoje: ",
        permitir_default = True
    )

    valor = get_valor()
    categoria = get_categoria()
    descricao = get_descricao()
    CSV.add_entrada(data, valor, categoria, descricao)


def main():
    while True:
        print("\n1. Adicionar nova transação")
        print("2. Ver transações e resumo dentro de um período")
        print("3. Sair")

        escolha = input("Escolha uma opção (1-3): ")

        if escolha == "1":
            add()
        elif escolha == "2":
            data_inicial = get_data("Digite a data inicial (dd-mm-yyyy): ")
            data_final = get_data("Digite a data final (dd-mm-yyyy): ")
            df = CSV.get_lancamentos(data_inicial, data_final)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()

        
            
