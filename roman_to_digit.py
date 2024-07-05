def roman_to_dec(roman_num):
    i = 0
    num = 0
    while i < len(roman_num):
        if i + 1 < len(roman_num) and roman_num[i: i + 2] in roman:
            num += roman[roman_num[i: i + 2]]
            i += 2
        else:
            num += roman[roman_num[i]]
            i += 1
    return num
    # while num > 0:
    # for _ in range(num // symbols[int_value]):
    # roman_num += symbols.values(int_value)
    # num -= symbols[int_value]
    # int_value += 1'''


# Roman numbers to numerals
def dec_to_roman(num):
    if num > 3999:
        raise ValueError('Cannot translate number greater than 3999 !')
    roman_num = ''
    for value in sorted(symbols.keys(), reverse=True):
        while num >= value:
            roman_num += symbols[value]
            num -= value
    return roman_num


def print_menu():
    menu = '''
    Task Manager Menu:
    1. Convert numerals to Roman.
    2. Convert Roman to numerals.
    3. Exiting...
    '''
    print(menu)


def main():
    while True:
        print_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            num = int(input('Enter a number to convert to Roman symbol: '))
            result = dec_to_roman(num)
            print(f'The Roman numeral representation is: {result}')
        elif choice == '2':
            num = input('Enter Roman Number to convert to numeral: ').upper()
            result = roman_to_dec(num)
            print(f'The numeral value of this Roman numeral is: {result}')
        elif choice == '3':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')


symbols = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

roman = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

if __name__ == '__main__':
    main()