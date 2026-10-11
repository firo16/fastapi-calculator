def obliczanie(liczba1,dzialanie,liczba2):
        if dzialanie == '+':
            return liczba1 + liczba2

        elif dzialanie == '-':
            return liczba1 - liczba2

        elif dzialanie == '*':
            return liczba1 * liczba2

        elif dzialanie == '/':
            return liczba1 / liczba2

        elif dzialanie == '//':
            return liczba1 // liczba2

        elif dzialanie == '^':
            return liczba1 ** liczba2

        elif dzialanie == '%':
            return liczba1 % liczba2

        else:
            raise ValueError('nie ma takiegop dzialania')






'''while True:
    try:
        liczba1 = float(input('podaj liczbe:'))
        dzialanie = input(f'podaj dzialanie\n'
                          f'/  +  /  -  /  *  /  //  /  ^  / _/_ /\n'
                          f'>')
        liczba2 = float(input('podaj liczbe:'))
        print(f'wynik -- {obliczanie(liczba1, dzialanie, liczba2)}')

    except ValueError:
        print('chlopie, tam powinna byc liczba...')'''



