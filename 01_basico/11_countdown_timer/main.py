import time

def timer():
    while True:
        try:
            t = int(input("Digite o tempo sem segundos: "))

            if t < 0:
                print("Por favor, insira um número positivo")
                continue

            break

        except ValueError:
            print("Opção inválida. Digite um número válido")
        
        
    while t:
        mins, secs = divmod(t, 60)
        
        time_string = '{:02d}:{:02d}'.format(mins, secs)
        
        print(time_string, end='\r')
        time.sleep(1)
        
        t -= 1

    print("Bazinga")
    



if __name__ == "__main__":
    timer()