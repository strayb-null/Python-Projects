import random

secret = random.randint(1,100)

while True:

    try:
        guess = int(input("Digite um número: "))
    except ValueError:
        print("\nOpção inválida\n") 
        continue
      
    if guess == secret:
        print(f"\nParabéns, você acertou o número secreto: {guess}")
        break
    elif guess > secret:
        print("O número secreto é MENOR!")
    elif guess < secret:
        print("O número secreto é MAIOR!")
   