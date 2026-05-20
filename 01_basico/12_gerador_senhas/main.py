import string 
import secrets
import math


def obter_tamanho_valido() -> int:
    while True:
        try:
            tamanho_senha = int(input("Digite o tamanho da senha desejada (mínimo 8): "))
            
            if tamanho_senha < 8:
                print("⚠️  Por segurança, o tamanho mínimo aceito é 8 caracteres.\n")
                continue

            return tamanho_senha
        
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite apenas números inteiros.\n")

def obter_conjunto_de_caracteres():
    print('''
🔐 Escolha quais tipos de caracteres quer na senha:
    [1] Letras (a-z, A-Z)
    [2] Números (0-9)
    [3] Caracteres especiais (!, @, #, etc.)
    [4] Finalizar seleção e gerar
    ''')

    conjunto_de_caracteres = "" 

    while True:
        try:
            escolha = int(input("Escolha uma opção (1-4): "))

        except ValueError:
            print("❌ Opção inválida! Digite um número entre 1 e 4.\n")
            continue
        
        match escolha:
            case 1:
                conjunto_de_caracteres += string.ascii_letters
                print("   ✅ Letras adicionadas.")

            case 2:
                conjunto_de_caracteres += string.digits
                print("   ✅ Números adicionados.")

            case 3:
                conjunto_de_caracteres += string.punctuation
                print("   ✅ Caracteres especiais adicionados.")
                
            case 4:
                if not conjunto_de_caracteres:
                    print("⚠️  Você precisa selecionar pelo menos um tipo de caractere!\n")
                    continue

                print("\n⏳ Gerando sua senha com algoritmo seguro...")
                print(conjunto_de_caracteres)
                break
            
            case _:
                print("❌ Opção inválida! Escolha entre 1 e 4.\n")
            
    return conjunto_de_caracteres

def main() -> None:
    print("="*45)
    print("  🛡️ GERADOR DE SENHAS SEGURAS (Edição 2026)")
    print("="*45)

    tamanho = obter_tamanho_valido()
    conjunto = obter_conjunto_de_caracteres()

    senha = "".join(secrets.choice(conjunto) for _ in range(tamanho))
    
    tamanho_conjunto = len(set(conjunto))

    entropy = tamanho * math.log2(tamanho_conjunto)

    print(f"\n✨ Sua senha segura é:\n\n👉  {senha}\n")

    print("📊 Análise de Segurança:")
    print(f"   • Tamanho: {tamanho} caracteres")
    print(f"   • Pool de caracteres: {tamanho_conjunto} opções únicas")
    print(f"   • Entropia: {entropy:.2f} bits ", end="")

    if entropy < 40:
        print("(🔴 Fraca)")
    elif entropy < 60:
        print("(🟡 Média)")
    elif entropy < 80:
        print("(🟢 Forte)")
    else:
        print("(💎 Inquebrável)")




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Operação cancelada pelo usuário. Até logo!")