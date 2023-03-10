TSINADADEBA = "მე მქვია ჭიკა ნყონია"
SITYVA = 'ბაყაყი'
ASO = 'ყ'
INDEQSI = 3
SITYVA_1 = ' წყალში ყიყინებს'



"""
0.
დაწერეთ ფუნქცია, რომელიც არგუემენტად მიწდოებულ სტრიქონს ' ' სიმბოლოზე
გახლეჩს და დაგიბრუნებს სიას, რომელიც წინადადების თითო სიტყვას მოიცავს:
- გამოიყენეთ სტრიქონის მონაცემთა ტიპზე ჩაშენებული "გახლეჩვის" ფუნქცია
- დააბრუნე შედეგად მიღებული სია

:param tsinadadeba: str სტრიქონი, რომელიც წარმოადგენს წინადადებას,
მაგლითად:
"მე მქვია ნიკა"
:return: list, სია; სია, გახლეჩილი ' ' space სიმბოლოზე. წინა მაგალითის
შემთხვევაში მიიღებდით:
['მე', 'მქვია', 'ნიკა']
"""
def seperateSentence(tsinadadeba):
    data = []
    j = 0
    a = 0
    for i in tsinadadeba:
        j += 1
        if i == " ":
            data.append(tsinadadeba[a:j])
            a = j
        if j == len(tsinadadeba) - 1:
            data.append(tsinadadeba[a:j+1])
            a = j
    return data


"""
1.
დაწერეთ ფუნქცია, რომელიც არგუმენტად მიწოდებულ სტრიქონს აქცევს სიად,
რომლის თითო ელემენტი სტრიქონის შემადგენელი ასო იქნება:
- შედეგამდე მისასვლელად გამოიყენეთ სიის კონსტრუქტორი ფუნქცია,
არგუმენტად კი მიაწოდეთ striqoni

:param striqoni: str სტრიქონი, მაგალითად: 'ხუჭუჭა'
:return: list სია, რომლის თითო ელემენტი იქნება არგუმენტად მიწოდებული
სტრიქონის ასოები, მაგალითად,
['ხ', 'უ', 'ჭ', 'უ', 'ჭ', 'ა']
"""

def alphabetSeperator(striqoni):
    list = []
    for i in striqoni:
        list.append(i)
    return list

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

def findIndex(striqoni,aso):
    return striqoni.index(aso)

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
def getbyID(striqoni,indexi):
    return striqoni[indexi]


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

def merge(striqoni_a, striqoni_b):
    return striqoni_a + striqoni_b


def main():
    """
    მთავარი ფუნქცია, სადაც უნდა მოათავსოთ ზემოთ გაწერილი დამხმარე ფუნქციების
    გამოძახება. დეტალურად წაიკითხეთ ფუნქციის ტანში, კომენტარების სახით
    მოცემული ინსტრუქციები.


    ბოლოს მოსალოდნელი შედეგი:

    წინადადება: მე მქვია ჭიკა ნყონია
    წინადადების სიტყვები: ['მე', 'მქვია', 'ჭიკა', 'ნყონია']
    ['მ', 'ე']
    ['მ', 'ქ', 'ვ', 'ი', 'ა']
    ['ჭ', 'ი', 'კ', 'ა']
    ['ნ', 'ყ', 'ო', 'ნ', 'ი', 'ა']
    სიტყვა, ბაყაყი-ში ვეზებთ ასო ყ-ს პირველ შემთხვევას
    პირველი შემთხვევა: 2
    სიტყვა, ბაყაყი-ში ვეზებთ ინდექს 3-ზე მყოფ სიმბოლოს
    სიმბოლო: ა
    ბაყაყი-ს ვუმატებთ  წყალში ყიყინებს-ს
    შედეგად მივიღეთ: ბაყაყი წყალში ყიყინებს
    """
    # 0. ცვლადს მიანიჭეთ, ამ ფაილში არსებული მუდმივას, TSINADADEBA-ს,
    # მნიშვნელობა
    sentence = TSINADADEBA

    # 1. მე-0 ნაბიჯში ცვლადი მიაწოდე მე-0 ფუნქციას არგუმენტად,
    # რათა მივიღოთ წინადადება, სიის სახით;
    # შედეგი, გასაგებად, დაბეჭდე კონსოლში
    listofsentence = seperateSentence(sentence)
    print(listofsentence)
    # 2. წინა, მე-1 ნაბიჯზე მიღებულ სიის თითო ელემენტზე
    # აწარმოე იტერაცია:
    # - სიის თითო ელემენტი არგუემნტად მიაწოდე მე-1 ფუნქციას, რათა
    # მივიღოთ სტრიქონის ყველა ასო, სიად
    # - შედეგად მიღებული სია დაბეჭდე
    for i in listofsentence:
        print(alphabetSeperator(i))


    # 3. მე-2 ფუნქციას არგუმენტად მიაწოდე ამ ფაილში გაწერილი მუდმივები,
    # SITYVA და ASO. შედეგი შეინახე ცვლადში;
    # - გასაგებად დაბეჭდე შედეგად მიღებული ცვლადი,
    ind = findIndex(SITYVA,ASO)
    print(ind)
    # 4. მე-3 ფუნქციას არგუმენტად მიაწოდე ამ ფაილში გაწერილი მუდმივები,
    # SITYVA და INDEQSI;
    # - შედეგად მიღებული პასუხი კონსოლში გასაგებად დაბეჭდე
    aso = getbyID(SITYVA,INDEQSI)
    print(aso)
    # 5. მე-4 ფუნქციას არგუმენტებად მიაწოდე ამ ფაილში გაწერილი მუდმივები,
    # SITYVA და SITYVA_1;
    # - შედეგად მიღებული სტრიქონი კონსოლში გასაგებად დაბეჭდე
    print(merge(SITYVA,SITYVA_1))
#print(seperateSentence("au magrad mshia ra es dedamotynuli to"))
#print(alphabetSeperator("magrad mshia"))
#print(findIndex("chyonias magrad shia","y"))
#print(getbyID("datvs shia",4))
#print(merge("shreki"," magaria"))
main()
