TSINADADEBA = "მე მქვია ჭიყა ნკონია"
SITYVA = 'ყაბაყი'
ASO = 'ა'
INDEQSI = 4
SITYVA_1 = ' ქვაბში ტივტივებს'



"""
0.
დაწერეთ ფუნქცია, რომელიც არგუემენტად მიწდოებულ სტრიქონს ' ' სიმბოლოზე
გახლეჩს და დაგიბრუნებს სიას, რომელიც წინადადების თითო სიტყვას მოიცავს:
- გამოიყენეთ სტრიქონის მონაცემთა ტიპზე ჩაშენებული "გახლეჩვის" ფუნქცია
- დააბრუნე შედეგად მიღებული სია

:param tsinadadeba: str სტრიქონი, რომელიც წარმოადგენს წინადადებას,
მაგლითად:
"მე ვარ ჭიკა ნყონია"
:return: list, სია; სია, გახლეჩილი ' ' space სიმბოლოზე. წინა მაგალითის
შემთხვევაში მიიღებდით:
['მე', 'ვარ', 'ჭიკა', 'ნყონია']
"""



"""
1.
დაწერეთ ფუნქცია, რომელიც არგუმენტად მიწოდებულ სტრიქონს აქცევს სიად,
რომლის თითო ელემენტი სტრიქონის შემადგენელი ასო იქნება:
- შედეგამდე მისასვლელად გამოიყენეთ სიის კონსტრუქტორი ფუნქცია,
არგუმენტად კი მიაწოდეთ striqoni

:param striqoni: str სტრიქონი, მაგალითად: ''
:return: list სია, რომლის თითო ელემენტი იქნება არგუმენტად მიწოდებული
სტრიქონის ასოები, მაგალითად,
['ხ', 'უ', 'ჭ', 'უ', 'ჭ', 'ა']
"""



"""
2.
დაწერეთ ფუნქცია, რომელიც არგუმენტად მიწოდებულ სტრიქონში, მეორე არგუმენტად
მიწდოებული ასოს პირველ შემთხვევას (იგივე ადგილმდებარეობას, იგივე ინდექსს) იპოვის:
- გამოიძახეთ სტრიქონზე გამართული ჩაშენებული ფუნქცია, რომელიც არგუმენტად მიწოდებულ
ასოს "პოულობს"
- ფუნქციიდან შედეგად მიღებული ინდექსი დააბრუნე

:param striqoni: str, სტრიქონი, რომელიც წარმოადგენს რამე სიტყვას.
მაგალითად, 'ბაყაყი'
:param aso: str, სტრიქონი რომელიც წარმოადგენს რაიმე ასოს, მაგალითად,
'ა'-ს
:return: int მთელრიცხვა მონაცემთა ტიპს, რომელიც წარმოადგენს არგუმენტ aso-ს
პირველ შემთხვევას (ინდექსს) სიტყვაში. მაგალითად თუ striqoni არის 'ბაყაყი' და
aso არის 'ა', შედეგად მივიღებთ 1-ს. თუ aso არის 'y', შედეგად მივიღებთ 2-ს
"""



"""
3.
დაწერეთ ფუნქცია, რომელიც არგუმენტად მიწოდებულ სტრიქონში, მეორე არგუმენტად
მიწოდებულ ინდექსზე მყოფ სიმბოლოს დააბრუნებს:
- გამოიყენეთ ინდექსაციის ოპერატორი, გაიხსენეთ, ეს არის კონკრეტული
სახის ფრჩხილები, რათა ინდექსზე მყოფ სიმბოლოს მიაკითხოთ
- შედეგად მოპოვებული სიმბოლო დააბრუნეთ
- ივარაუდეთ, რომ indeqsi სტრიქონში არსებობს, ანუ მის სიგრძის გარეთ არ არის

:param striqoni: str სტრიქონი. მაგალითად, 'ნაყინი'
:param indeqsi: int მთელრიცხვა მონაცემთა ტიპი. მაგალითად, 2
:return: str, სტრიქონი; striqoni-ში, არგუმენტად მიწოდებულ indeqsi-ის
ინდექსზე მყოფ სიმბოლოს დააბრუნებს. მაგალითად, თუ stirqoni არის 'ნაყინი' და
indeqsi არის 2, შედეგად მიიღებთ, 'ყ'-ს
"""



"""
4.
დაწერეთ ფუნქცია, რომლის მეშვებოით, პირველი არგუმენტით მიწოდებულ სტირქონს,
მეორე არგუმენტით მიწოდებულ სტრიქონს მიუმატებთ, და შედეგად წარმოებულ
სტრიქონს დააბრუნებთ:
- ამ ოპერაციის განსახორციებლად არსებობს ერთი ოპერატორი; ერთი სტრიქონი
მეორეს გვინდა რომ "მივუმატოთ".

:param sityva_a: str, სტრიქონი. მაგალითად, "Hello, "
:param sityva_b: str, სტრიქონი. მაგალითად, "World!"
:return: str, სტრიქონი რომელიც არის sityva_a და sityva_b-ს მიმატება. მაგალითად,
თუ sityva_a არის "Hello, "  და sityva_b არის "World!", შედეგად უნდა მიიღოთ
"Hello, World!"
"""



"""
5. 
დაწერე ფუნქცია, რომელიც striqoni არგუმენტის სტრიქონს გაჭრის, start
და stop არგუმენტის მთელრიცხვა ინდექსებზე:

0. გამოიყენეთ Python-ზე გამართული ინდექსაციის სინტაქსი (გაიხსენეთ,
რომელი სახის ფრჩხილებით ხდება ეს), რათა სტრიქონი გაჭრა start ინდექსიდან
stop **ინდექსამდე**

1. შედეგად მიღებული სტრიქონი დააბრუნე

მაგალითად, თუ striqoni არის 'კაკალი', start არის 1, stop არის 4,
შედეგად დავაბრუნებთ სტრიქონ, 'აკა'-ს.

თუ start არის 2, stop არის -1, მივიღებთ სტრიქონ, 'კალ'-ს

:param striqoni: str სტრიქონი, რომლის გაჭრაც გვსურს
:param start: int მთელრიცხვა მონცაემთა ტიპი, რომელიც არის სტრიქონის გაჭრის
საწყისი ინდექსი
:param stop: int მთელრიცხვა მონცაემთა ტიპი, რომელიც არის სტრიქონის გაჭრის
სასრული ინდექსი
:return: str სტრიქონი, რომელიც არის ინდექსზებზე გაჭრილი
"""



def main():
    """
    მთავარი ფუნქცია, სადაც უნდა მოათავსოთ ზემოთ გაწერილი დამხმარე ფუნქციების
    გამოძახება. დეტალურად წაიკითხეთ ფუნქციის ტანში, კომენტარების სახით
    მოცემული ინსტრუქციები.


    ბოლოს მოსალოდნელი შედეგი:

    წინადადება: მე მქვია ჭიკა ნყონია
    წინადადების სიტყვები: ['მე', 'მქვია', 'ჭიყა', 'ნკონია']
    ['მ', 'ე']
    ['მ', 'ქ', 'ვ', 'ი', 'ა']
    ['ჭ', 'ი', 'ყ', 'ა']
    ['ნ', 'კ', 'ო', 'ნ', 'ი', 'ა']
    სიტყვა, ყაბაყი-ში ვეძებთ ასო ა-ს პირველ შემთხვევას
    პირველი შემთხვევა: 1
    სიტყვა, ყაბაყი-ში ვეძებთ ინდექს 4-ზე მყოფ სიმბოლოს
    სიმბოლო: ყ
    ყაბაყი-ს ვუმატებთ  ქვაბში ტივტივებს-ს
    შედეგად მივიღეთ: ყაბაყი ქვაბში ტივტივებს
    სტირქონ, ყაბაყი ქვაბში ტივტივებს, ვჭრით ინდექს 2-დან, 8-დე
    შედეგად მივიღეთ: ბაყი ქ
    """
    # 0. ცვლადს მიანიჭეთ, ამ ფაილში არსებული მუდმივას, TSINADADEBA-ს,
    # მნიშვნელობა


    # 1. მე-0 ნაბიჯში ცვლადი მიაწოდე მე-0 ფუნქციას არგუმენტად,
    # რათა მივიღოთ წინადადება, სიის სახით;
    # შედეგი, გასაგებად, დაბეჭდე კონსოლში


    # 2. წინა, მე-1 ნაბიჯზე მიღებულ სიის თითო ელემენტზე
    # აწარმოე იტერაცია:
    # - სიის თითო ელემენტი არგუემნტად მიაწოდე მე-1 ფუნქციას, რათა
    # მივიღოთ სტრიქონის ყველა ასო, სიად
    # - შედეგად მიღებული სია დაბეჭდე


    # 3. მე-2 ფუნქციას არგუმენტად მიაწოდე ამ ფაილში გაწერილი მუდმივები,
    # SITYVA და ASO. შედეგი შეინახე ცვლადში;
    # - გასაგებად დაბეჭდე შედეგად მიღებული ცვლადი,


    # 4. მე-3 ფუნქციას არგუმენტად მიაწოდე ამ ფაილში გაწერილი მუდმივები,
    # SITYVA და INDEQSI;
    # - შედეგად მიღებული პასუხი კონსოლში გასაგებად დაბეჭდე


    # 5. მე-4 ფუნქციას არგუმენტებად მიაწოდე ამ ფაილში გაწერილი მუდმივები,
    # SITYVA და SITYVA_1;
    # - შედეგეად მიღებული სტრიქონი შეინახე ცვლადში
    # - შედეგად მიღებული სტრიქონი კონსოლში გასაგებად დაბეჭდე

    # 6. მე-5 ფუნქციას არგუემნტებად მიაწოდე წინა, მე-5 ნაბიჯის შედეგად მიღებული
    # ცვლადი, საწყისი ინდექსი 2, დასასრული ინდექსი, 8:
    # - შედეგად მიღებული სტრიქონი ცვალდში შეინახე
    # - შედეგად მიღეუბლი სტრიქონი გამოიტანე კონსოლში


main()