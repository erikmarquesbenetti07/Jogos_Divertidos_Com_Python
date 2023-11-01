import random

def acerte_o_numero():
    print("Bem-vindo ao Jogo Acerte o Número!")
    while True:
        numero_secreto = random.randint(0, 10)
        tentativas = 5
        pontuacao = 100
        
        print("Tente adivinhar o número entre 0 e 10. Você tem 5 tentativas.")
        
        for tentativa in range(1, tentativas + 1):
            try:
                palpite = int(input(f"Tentativa {tentativa}: "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            
            if palpite < 0 or palpite > 10:
                print("O número deve estar entre 0 e 10.")
                continue
            
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativa} tentativa(s). Sua pontuação é {pontuacao} pontos.")
                break
            elif tentativa < tentativas:
                pontuacao -= 20
                if palpite < numero_secreto:
                    print("Tente um número maior.")
                else:
                    print("Tente um número menor.")
        else:
            print(f"Você esgotou suas tentativas. O número era {numero_secreto}. Sua pontuação é 10 pontos.")
        
        novo_jogo = input("Deseja jogar novamente? (S/N): ").strip().lower()
        if novo_jogo != 's':
            break

if __name__ == "__main__":
    acerte_o_numero()
