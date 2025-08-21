from roman_digit.logic import dec_to_roman, roman_to_dec

def print_menu():
    menu = '''
    Task Manager Menu:
    1. Convert numerals to Roman.
    2. Convert Roman to numerals.
    3. Exit.
    '''
    print(menu)

def main():
    while True:
        print_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            try:
                num = int(input('Enter a number to convert to Roman symbol: '))
                result = dec_to_roman(num)
                print(f'The Roman numeral representation is: {result}')
            except ValueError as e:
                print(e)
        elif choice == '2':
            num = input('Enter Roman Number to convert to numeral: ').upper()
            try:
                result = roman_to_dec(num)
                print(f'The numeral value of this Roman numeral is: {result}')
            except KeyError:
                print('Invalid Roman numeral entered.')
        elif choice == '3':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
