from django.test import TestCase
from roman_digit.logic import dec_to_roman, roman_to_dec

class RomanNumeralConversionTest(TestCase):

    def test_dec_to_roman(self):
        self.assertEqual(dec_to_roman(1), 'I')
        self.assertEqual(dec_to_roman(4), 'IV')
        self.assertEqual(dec_to_roman(5), 'V')
        self.assertEqual(dec_to_roman(9), 'IX')
        self.assertEqual(dec_to_roman(10), 'X')
        self.assertEqual(dec_to_roman(40), 'XL')
        self.assertEqual(dec_to_roman(50), 'L')
        self.assertEqual(dec_to_roman(90), 'XC')
        self.assertEqual(dec_to_roman(100), 'C')
        self.assertEqual(dec_to_roman(400), 'CD')
        self.assertEqual(dec_to_roman(500), 'D')
        self.assertEqual(dec_to_roman(900), 'CM')
        self.assertEqual(dec_to_roman(1000), 'M')
        self.assertEqual(dec_to_roman(3999), 'MMMCMXCIX')
        with self.assertRaises(ValueError):
            dec_to_roman(4000)

    def test_roman_to_dec(self):
        self.assertEqual(roman_to_dec('I'), 1)
        self.assertEqual(roman_to_dec('IV'), 4)
        self.assertEqual(roman_to_dec('V'), 5)
        self.assertEqual(roman_to_dec('IX'), 9)
        self.assertEqual(roman_to_dec('X'), 10)
        self.assertEqual(roman_to_dec('XL'), 40)
        self.assertEqual(roman_to_dec('L'), 50)
        self.assertEqual(roman_to_dec('XC'), 90)
        self.assertEqual(roman_to_dec('C'), 100)
        self.assertEqual(roman_to_dec('CD'), 400)
        self.assertEqual(roman_to_dec('D'), 500)
        self.assertEqual(roman_to_dec('CM'), 900)
        self.assertEqual(roman_to_dec('M'), 1000)
        self.assertEqual(roman_to_dec('MMMCMXCIX'), 3999)