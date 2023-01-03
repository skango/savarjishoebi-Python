from menu import shekvetis_migheba as shekveta


def main():
    """
    მეგობრებთან ერთად ხარ რესტორანში. შთაგონებული ხარ და გადაწყვიტე რესტორნის
    შეკვეთის სისტემის ავტომატიზაცია.

    დაამთავრე ამ მოდულის და დამხმარე მოდულის კოდი, რათა ქვემოთ მოცემული
    შეკვეთბი გამოითვალო
    """
    kerdzi = 'შაურმა'
    fasi = shekveta(kerdzi)
    print(f'{kerdzi}ს ფასი: {fasi}')

    print('-------------------------------------------------------------')
    kerdzi = 'შაურმა'
    fasi = shekveta(kerdzi, ingredientebi={
            'კეტჩუპი': 'ნაკლები',
            'მაიონეზი': 'მეტი'
        }
    )
    print(f'{kerdzi}ს ფასი: {fasi}')

    print('-------------------------------------------------------------')
    kerdzi = 'პიცა'
    fasi = shekveta(kerdzi, ingredientebi={
            'სოუსი': 'მეტი',
            'სოკო': 'ნაკლები'
        }
    )
    print(f'{kerdzi}ს ფასი: {fasi}')

    print('-------------------------------------------------------------')
    kerdzi = 'ბურგერი'
    fasi = shekveta(kerdzi, ingredientebi={
            'ხახვი': 'მეტი',
            'სოუსი': 'ნაკლები'
        }
    )
    print(f'{kerdzi}ს ფასი: {fasi}')


main()
