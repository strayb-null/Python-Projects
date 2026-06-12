from datetime import datetime 

data_formatada = "%d-%m-%Y"
CATEGORIAS = {"G": "Ganhos", "D": "Despesas"}

def get_data(prompt, permitir_default=False):
    data_str = input(prompt)
    if permitir_default and not data_str:
        return datetime.today().strftime(data_formatada)
    try:
        data_valida = datetime.strptime(data_str, data_formatada)
        return data_valida.strftime(data_formatada)
    except ValueError:
        print("Data inválida, por favor digite uma data válida no formato dd-mm-yyyy")
        return get_data(prompt, permitir_default)


def get_valor():
    try:
        valor = float(input("Insira o valor: "))
        if valor <= 0:
            raise ValueError("O valor não pode ser zero ou um valor negativo!")
        return valor
    except ValueError as e:
        print(e)
        return get_valor()


def get_categoria():
    categoria = input("Digite a categoria ('G' para ganhos ou 'D' para despesas): ").upper()
    if categoria in CATEGORIAS:
        return CATEGORIAS[categoria]
    
    print("Categoria inválida. Por favor digite, 'G' para ganhos ou 'D' para despesas")
    return get_categoria()


def get_descricao():
    return input("Digite uma descrição (opcional): ")