# აქ შემოიტანეთ საჭირო მოდულები
import random as r

MAX_HEALTH = 100
LOWEST_DAMAGE = 0
HIGHEST_DAMAGE = 25

ENEMY_NAMES = [
    'BIG GUY',
    'CHICK NKONIA',
    'SUE SIDE',
    'BAMES JOND',
    'HUGH JAZZ',
    'ADAM YANNY',
    'JOSEPH STALIN'
]

CHARACTER_TYPES = {
    'ENEMY': 'enemy',
    'PLAYER': 'player'
}


def calculate_damage(lowest_damage=LOWEST_DAMAGE, highest_damage=HIGHEST_DAMAGE):
    """
    0.

    გამოითვლის შეტევის სიძლიერეს. შემთხვევითობის მოდულიდან გამოიძახებს
    შემთხვევითი მთელრიცხვა დიაპაზონის წარმოების ფუნქციას და ზღვარებად მიაწდოებს
    ფუნქციაში მიწოდებულ არგუმენტებს და შედეგად მიღებულ რიცხვს დააბრუნებს.


    :param lowest_damage: int - შეტევის სიძლიერის ქვედა დიაპაზონი; გაჩუმებით
    LOWEST_DAMAGE
    :param highest_damage: int - შეტევის სიძლიერის ზედა დიაპაზონი; გაჩუმებით
    HIGHEST_DAMAGE
    :return: int - შედეგად მიღებული შეტევის სიძლიერის რიცხვითი მაჩვენებელი
    """
    return r.randrange(lowest_damage, highest_damage)


def make_character():
    """
    1.

    ქმნის ახალი პერსონაჟის საბაზისო ლექსიკონს, რომელში იქნება
    მხოლოდ შემდეგი მონაცემი:

    {
        'health': MAX_HEALTH
    }

    სადაც MAX_HEALTH არის მოდულში არსებული მუდმივა

    :return: dict -  შედეგად შექმნილ ლექსიკონს
    """
    new_character = {"health": MAX_HEALTH}
    return new_character


def make_enemy():
    """
    2.

    ქმნის მოწინააღმდეგის პერსონაჟს. ჯერ იძახებს ზემოთ მოცემულ დამხმარე, მე-1 ფუნქციას,
    შემდეგ შედეგად შექმნილი პერსონაჟის ლექსიკონს უმატებს დამატებით, საჭირო წყვილებს.

    შედეგად მიღებულ მოწინააღმდეგეს
    ლექსიკონს უნდა ჰქონდეს შემდეგი სტრუქტურა:

    {
        'health': int,
        'type': str,
        'name': str
    }
    - სადაც type-ი უთითებს ამ მოდულში არსებული მუდმივი ლექსიკონიდან,
    CHARACTER_TYPES-იდან, ENEMY გასაღებით მითითებულ მონაცემს
    - სადაც name არის ამ მოდულში არსებული მუდმივი სიიდან, ENEMY_NAMES-დან
    შემთხვევით ამორჩეული სტრიქონი

    :return: dict - შედეგად მიღებული მეწინააღმდეგის ტიპის პერსონაჟს
    """
    enemy = {"health": MAX_HEALTH, "type": CHARACTER_TYPES["ENEMY"],
             "name": ENEMY_NAMES[r.randrange(0, len(ENEMY_NAMES))]}
    return enemy


def make_player_character(name):
    """
    3.

    ქმნის მოთამაშეს პერსონაჟს, არგუმენტად მიწოდებული სახელით.
    ჯერ ზემოთ მოცეცმული მე-1 დამხმარე ფუნქციას იძახებს, მერე კი
    შედეგად შექმნილ ლექსიკონს უმატებს საჭირო, დამატებით წყვილებს.

    შედეგად მიღებულ მოთამაშეს პერსონაჟის ლექსიკონს უნდა ჰქონდეს შემდეგი
    სტრუქტურა:

    {
        'health': int,
        'type': str,
        'name': str
    }
    - სადაც type-ი უთითებს ამ მოდულში არსებული მუდმივი ლექსიკონიდან,
    CHARACTER_TYPES-იდან, PLAYER გასაღებით მითითებულ მონაცემს
    - სადაც name არის ამ ფუნქციაში მოწოდებული პარამეტრი


    :param name: str - მოთამაშეს პერსონაჟის სასურველი სახელი
    :return: dict - შედეგად მიღებული მოთამაშის ტიპის პერსონაჟს
    """
    player = {"health": MAX_HEALTH, "type": CHARACTER_TYPES["PLAYER"],
              "name": name}
    return player


def check_health(character):
    """
    4.

    მიწოდებული პერსონაჟის ლექსიკონიადნ სიცოცხლის მაჩვენებელს აბრუნებს

    :param character: dict - პერსონაჟის ამსახველი ლექსიკონი
    :return: int - პერსონაჟის სიცოცხლის მაჩვენებელი რიცხვი
    """
    return character["health"]


def take_damage(character, damage):
    """
    5.

    არგუმენტად მიწოდებულ პერსონაჟს მეორე არგუმენტად მიწოდებული დარტყმის
    სიძლიერის ზიანს აყენებს. მე-4 ფუნქციის გამოძახებით ამოწმებს
    პერსონაჟის სიცოცხლის მაჩვენებელს და იმ შემთხვევაში თუ დარტყმის სიძლიერე
    მეტია 0-ზე, პერსონაჟის სიცოცხლის მაჩვენებელს აკლდება დარტყმის სიძლიერის
    რაოდენობა. სხვა შემთხვევაში კი კონსოლში ვბეჭდავთ, რომ პერსონაჟმა სიანი
    არ მიიღო.

    :param character: dict - დარტყმის მიმღები პერსონაჟის ამსახველი ლექსიკონი
    :param damage: int - დარტყმის სიძლიერის რიცხვითი მაჩვენებლი
    """

    character["health"] -= damage if damage > 0 else print("Character is not damaged!")


def attack(target):
    """
    6.

    მე-0 ფუნქციის გამოძახებით გამოითვლის დარტყმის სიძლიერეს და
    მე-5 ფუნქციას არგუმენტებად გადასცემს შედეგად მიღებულ მთელრიცხვა მონაცემსა
    და არგუმენტად მიღებული სამიზნე პერსონაჟის ლექსიკონს.

    :param target: dict - სამიზნე პერსონაჟის ამსახველი ლექსიკონი
    :return: int - მიღებული დარტყმის სიძლიერე
    """
    damage = calculate_damage()
    take_damage(target, damage)
    return damage
