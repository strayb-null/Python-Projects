import random # passo 1

def get_digitos(numero): # passo 2
    return [int(digito) for digito in str(numero)]

def sem_duplicacao(numero):
    lista_numeros = get_digitos(numero)
    return len(lista_numeros) == len(set(lista_numeros))

def gerar_numero():
    while True:
        numero = random.randint(1000, 9999)
        if sem_duplicacao(numero):
            return numero
        
def calcular_touros_vacas(numero_secreto, numero_chute):
    boi_vaca = [0,0]
    numero_secreto_li = get_digitos(numero_secreto)
    numero_chute_li = get_digitos(numero_chute)
    
    
    for i,j in zip(numero_secreto_li, numero_chute_li):
        if j in numero_secreto_li:
            if j == i:
                boi_vaca[0] += 1
            else:
                boi_vaca[1] += 1
    return boi_vaca

def main():
    numero_secreto = gerar_numero()
    print(numero_secreto) #teste
    tentativas = int(input("Digite quantas tentativas você quer fazer:\n> "))

    while tentativas > 0:
        palpite = int(input("Digite seu palpite:\n> "))

        if palpite < 1000 or palpite > 9999:
            print("Digite apenas numeros com 4 digitos, tente novamente")
            continue
        if not sem_duplicacao(palpite):
            print("O número não deve ter duplicação, tente novamente")
            continue
    
        boi_vaca = calcular_touros_vacas(numero_secreto, palpite)
        print(f"{boi_vaca[0]} Touro e {boi_vaca[1]} Vaca")
        tentativas -= 1

        if boi_vaca[0] == 4:
            print("Você ganhou o jogo")  
    else:
        print("Você perdeu, acabou suas tentativas")



if __name__ == "__main__":
    main()