import random

# Lista de palavras para o jogo
palavras = ['python', 'programacao', 'computador', 'jogador', 'forca', 'janela']

def escolher_palavra():
    # Escolhe uma palavra aleatória da lista
    return random.choice(palavras)

def jogar_forca(palavra):
    # Inicialização das variáveis
    palavra_secreta = list(palavra)
    palavra_revelada = ['_'] * len(palavra)
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    
    while True:
        # Mostra o estado atual da palavra
        print("Palavra: " + " ".join(palavra_revelada))
        print("Letras erradas: " + ", ".join(letras_erradas))
        print("Tentativas restantes: " + str(tentativas))
        
        if "_" not in palavra_revelada:
            print("Parabéns! Você adivinhou a palavra corretamente: " + palavra)
            break

        if tentativas == 0:
            print("Você perdeu! A palavra era: " + palavra)
            break

        # Recebe a próxima tentativa do jogador
        tentativa = input("Tente uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Entrada inválida. Por favor, insira uma única letra.")
            continue

        if tentativa in palavra:
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    palavra_revelada[i] = tentativa
        else:
            letras_erradas.append(tentativa)
            tentativas -= 1

# Início do jogo
if __name__ == "__main__":
    palavra = escolher_palavra()
    jogar_forca(palavra)
