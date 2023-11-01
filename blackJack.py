import random

# Criação do baralho
suits = ['Espadas', 'Copas', 'Ouros', 'Paus']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']

# Dicionário de valores das cartas
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Valete': 10, 'Dama': 10, 'Rei': 10, 'Ás': 11
}

# Criação do baralho
deck = [{'rank': rank, 'suit': suit, 'value': card_values[rank]} for rank in ranks for suit in suits]

# Função para calcular a pontuação de uma mão
def calculate_score(hand):
    score = sum(card['value'] for card in hand)
    # Tratar Ás como 1 se o valor total for maior que 21
    for card in hand:
        if card['rank'] == 'Ás' and score > 21:
            score -= 10
    return score

# Função para mostrar uma mão
def display_hand(hand):
    for card in hand:
        print(f'{card["rank"]} de {card["suit"]}')

# Inicialização das mãos do jogador e do computador
player_hand = [random.choice(deck) for _ in range(2)]
computer_hand = [random.choice(deck) for _ in range(2)]

# Loop do jogo
while True:
    print('\nMão do jogador:')
    display_hand(player_hand)
    player_score = calculate_score(player_hand)
    print(f'Pontuação do jogador: {player_score}')

    # Verifique se o jogador estourou
    if player_score > 21:
        print('Você estourou! Computador vence.')
        break

    # Pergunte ao jogador se deseja comprar outra carta
    choice = input('Deseja comprar outra carta? (sim/não): ')
    if choice.lower() == 'sim':
        player_hand.append(random.choice(deck))
    else:
        # Vez do computador
        while calculate_score(computer_hand) < 17:
            computer_hand.append(random.choice(deck))
        
        print('\nMão do computador:')
        display_hand(computer_hand)
        computer_score = calculate_score(computer_hand)
        print(f'Pontuação do computador: {computer_score}')

        # Determine o vencedor
        if computer_score > 21 or player_score > computer_score:
            print('Você venceu!')
        elif player_score < computer_score:
            print('Computador venceu!')
        else:
            print('Empate!')
        break
