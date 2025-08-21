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

def roman_to_dec(roman_num):
    i = 0
    num = 0
    while i < len(roman_num) :
        if i + 1 < len(roman_num) and roman_num[i : i + 2] in roman :
            num += roman[roman_num[i : i + 2]]
            i += 2
        else :
            num += roman[roman_num[i]]
            i += 1
    return num

def dec_to_roman(num):
    if num > 3999 :
        raise ValueError('Cannot translate number greater than 3999!')
    roman_num = ''
    for value in sorted(symbols.keys(), reverse=True) :
        while num >= value :
            roman_num += symbols[value]
            num -= value
    return roman_num