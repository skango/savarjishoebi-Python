# სტანდარტული ბიბლიოთეკის, random და math მოდულები, შემოიტანე


# მუდმივები - ხელი არ ახლოთ
# სანტიმეტრებში
CHURCHKHELIS_RADIUSI = 1.5

SACHMELI = [
    'ჩურჩხელა'
]



def churchkelis_zoma(simaghle):
    """
    დაწერე ფუნქცია, რომელიც არგუმენტად მიწოდებული სიმაღლის მიხედვით გამოითვლის
    ჩურჩხელას მოცულობას:

    - ვვარაუდობთ, რომ ჩურჩხელა ცილინდრი არის (ბოლოში კონუსებს არ ვუმატებთ,
    მხოლოდ ცილინდრად აღვიქვამთ)
    - ცილინდრის მოცულობის ფორმულა:
    მოცულობა = pi * (radiusi ** 2) * simaghle
    - radiusi-ისათვის გამოიყენე ამ ფაილის გლობალურ ფარგლებში არსებული მუდმივა,
    CHURCHKHELIS_RADIUSI
    - საზომი ერთეულები სანიტმეტრებია

    0. ზემოთ მოყვანილ მოცულობის ფორმულის გამოთვლას ახორციელებს პითონის
    სინტაქსით
    1. შედეგად მიღებულ მოცულობას აბრუნებს

    :param simaghle: int მთელრიცხვა მონაცემთა ტიპი
    :return: float ნამდვილი რიცხვის მონაცემთა ტიპს, რომელიც ჩურჩხელის
    მოცულობას წარმოადგენს
    """
    pass


def random_churchkelis_zomebi(raodenoba=10):
    """
    ეს ფუნქცია ქმნის სიას, რომლის თითო ელემენტი არის შემთხვევით გამოყვანილი
    ჩურჩხელის მოცულობები:

    თითო ჩურჩხელის სიმაღლე  უნდა იყოს **შემთხვევითი** (random):
    - ან int ან float ტიპის, ორივეში თანაბარ ქულას დაგიწერ
    - ჩურცხელის სიმაღლე: იყოს 1-დან 15 სანტიმეტრის **ჩათვლით** დიაპაზონში


    0. ქმნის ცარიელ სიას
    1. raodenoba არგუმენტის ოდენობით ასრულებს:
        ა. ჩურჩხელის სიმაღლის შემთხვევით გამოთვლას; ინახავს ცვლადში
        ბ. ჩურცXელის მოცულობას გამოითვლის, ფუნქცია churchkehlis_zoma-ს
        გამოძახებით:
            - არგუმენტად აწვდის გამოთვლილ სიმაღლეს
        გ. წინა ნაბიჯის შედეგად მიღებულ მოცულობას მე-0 ნაბიჯში შექმნილ სიას
        ბოლოში უმატებს

    2. შედეგად წარმოებულ სიას აბრუნებს


    :param raodenoba: int მთელრიცხვა მონცაემთა ტიპი; რამდენი ჩურცხელის
    მოცულობის გამოთვლა გვსურს
    :return: list სია, რომელიც მოიცავს ჩურჩხელის მოცულობებს; raodenoba
    არგუმენტით მიწოდებული რაოდენობის ელემენტებს მოიცავს
    """
    pass
