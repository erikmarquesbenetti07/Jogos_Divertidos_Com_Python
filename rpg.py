import random

# Classe do personagem
class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

# Classes de monstros
class Goblin(Character):
    def __init__(self):
        super().__init__("Goblin", 10, 3)

class Dragon(Character):
    def __init__(self):
        super().__init__("Dragon", 30, 5)

# Função para realizar um combate
def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f'{player.name} HP: {player.hp}')
        print(f'{enemy.name} HP: {enemy.hp}')
        print("\nOpções de ação:")
        print("1. Atacar")
        print("2. Fugir")
        choice = input("O que você deseja fazer? ")

        if choice == '1':
            player_damage = random.randint(0, player.attack)
            enemy_damage = random.randint(0, enemy.attack)

            print(f'Você ataca o {enemy.name} e causa {player_damage} de dano!')
            print(f'O {enemy.name} te ataca e causa {enemy_damage} de dano!\n')

            enemy.take_damage(player_damage)
            player.take_damage(enemy_damage)
        elif choice == '2':
            print("Você fugiu da batalha!")
            return False

    if player.is_alive():
        print(f'Você derrotou o {enemy.name}!\n')
        return True
    else:
        print(f'Você foi derrotado pelo {enemy.name}!\n')
        return False

# Função principal
def main():
    print("Bem-vindo ao Jogo de RPG!")

    player_name = input("Digite o nome do seu personagem: ")
    player = Character(player_name, 20, 4)

    while player.is_alive():
        enemy = random.choice([Goblin(), Dragon()])
        print(f'Um {enemy.name} apareceu!\n')
        result = battle(player, enemy)

        if not result:
            print("Fim de jogo. Deseja jogar novamente?")
            replay = input("Digite 'sim' para jogar novamente: ")
            if replay.lower() != 'sim':
                break

    print("Obrigado por jogar!")

if __name__ == "__main__":
    main()
