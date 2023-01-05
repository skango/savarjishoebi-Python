# შემოიტანე gameengine მოდული
import gameengine as game


# ამ ფუნქციას გჩუქნით
def handle_character_gen(player):
    """
    ასრულებს მოთამაშეს პერსონაჟის შექმნას. მომხმარებლისგან შემოაქვს პერსონაჟის
    სახელი და gamengine მოდულის მე-3 ფუნქციას აწვდის არგუმენტად. აბრუნებს
    შედეგად შექმნილი პერსონაჟის ლექსიკონს.

    :param player: str - მოთამაშეს სახელი (ან 'Player 1' ან 'Player 2'
    :return: dict - შედეგად მიღებული პერსონაჟის ლექსიკონი
    """
    name = input(f'{player}, please enter your character\'s name: ')
    return game.make_player_character(name)


# ამ ფუნქციას გჩუქნით
def handle_enemy_gen():
    """
    ქმნის და აბრუნებს მოწინააღმდეგე პერსონაჟს, gamengine-ის მოდულის
    make_enemy ფუნქციის გამოძახებით.

    :return: dict - შედეგად მიღებული მოწინააღმედგე პერსონაჟის ამსახველი
    ლექსიკონი
    """
    return game.make_enemy()


def game_over(player1, player2):
    """
    0.

    ამოწმებს თამაშის დასრულების პირობას. თამაში იმ შემთხვევაში სრულდება
    თუ არგუმენტად მიწოდებული რომელიმე მომხმარებლს სიცოცხლე აღარ აქვს.
    ამას აწომწებს gamengine მოდულის მე-4 ფუნქციის გამოძახებით:
        ა. თითო მოთამაშეს სიცოცხლის მაჩვენებელს ინახავს ცვლადში.
        ბ. კონსოლში ბეჭდავს თითო მომხმარებლის სახელსა და სიცოცხლის
        რიცხვით მაჩვენებელს
        გ. თუ რომელიმე მოთამაშეს სიცოცხლის მაჩვენებელი ნაკლებია ან ტოლია
        ნულსა, ნიშნავს რომ ამ მოთამაშემ წააგო და მეორე მოთამაშემ მოიგო.
        მოგებული მომხმარებლის ლექსიკონიდან აბრუნებს სახელს.
        დ. სხვა შემთხვევაში None-ს

    :param player1: პირველი მოთამაშის ამსახველი ლექსიკონი
    :param player2: მეორე მოთამაშის ამსახველი ლექსიკონი
    :return: str - გამარჯვებული მოთამაშის სახელი. სხვა შემთხვევაში
    None
    """
    health1 = game.check_health(player1)
    health2 = game.check_health(player2)
    print(f"{player1['name']} health is {health1}")
    print(f"{player2['name']} health is {health2}")
    if health2 <= 0:
        return player1['name']
    elif health1 <= 0:
        return player2['name']
    else:
        return None


# ამ ფუნქციას გჩუქნით
def play_game(player1, player2):
    """
    თამაშის გასაშვები მთავარი ფუნქცია. მოთამაშეები ერთმანეთს არტყამნე,
    მანამ სანამ ერთ-ერთი მოთამაშე არ მოიგებს თამაშს.

    :param player1: პირველი მოთამაშეს პერსონაჟის ამსახველი ლექსიკონი
    :param player2: მეორე მოთამაშეს პერსონაჟის ამსახველი ლექსიკონი
    """
    winner = ""
    player_1_name = player1.get('name')
    player_2_name = player2.get('name')

    while True:
        winner = game_over(player1, player2)
        if winner:
            break

        damage = game.attack(player2)
        print(f'{player_1_name} attacks {player_2_name} for {damage} damage!')
        damage = game.attack(player1)
        print(f'{player_2_name} attacks {player_1_name} for {damage} damage!')

    print(f'Congratulations, {winner} won!')


# ამ ფუნქციას გჩუქნით
def main():
    """
    წლების განმავლობაში ვიდეო თამაშებში გატარებულმა დრომ შთაგაგონა და
    მოგანდომა ფინალურ გამოცდაში პატარა თამაშის შექმნა. კარგი დამთხვევაა.
    """
    while True:
        mode = input('pick game mode:\n1: {Player vs Player}\n2: {Player vs Computer}\n>>>')

        # pvp
        if mode == '1':
            player1 = handle_character_gen('Player 1')
            player2 = handle_character_gen('Player 2')
            play_game(player1, player2)
            break

        # pve
        if mode == '2':
            player1 = handle_character_gen('Player 1')
            player2 = handle_enemy_gen()
            play_game(player1, player2)
            break


main()
