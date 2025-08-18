from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from roman_digit.serializers import ToRomanSerializer, ToDecimalSerializer

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

def index(request):
    result = None
    error = None

    if request.method == 'GET' and 'action' in request.GET :
        action = request.GET.get('action')
        if action == 'to_roman' :
            try :
                num = int(request.GET.get('number', 0))
                result = dec_to_roman(num)
            except ValueError as e :
                error = str(e)
        elif action == 'to_decimal' :
            roman_num = request.GET.get('roman_number', '').upper()
            try :
                result = roman_to_dec(roman_num)
            except KeyError :
                error = 'Invalid Roman numeral entered.'

    return render(request, 'index.html', {'result' :result, 'error' :error})

class ToRomanView(APIView):
    serializer_class = ToRomanSerializer
    def get(self, request):
        serializer = ToRomanSerializer(data=request.data)
        if serializer.is_valid():
            try:
                result = dec_to_roman(serializer.validated_data['number'])
                return Response({'result': result}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDecimalView(APIView):
    serializer_class = ToDecimalSerializer
    def get(self, request):
        serializer = ToDecimalSerializer(data=request.data)
        if serializer.is_valid():
            roman_num = serializer.validated_data['roman_number'].upper()
            try:
                result = roman_to_dec(roman_num)
                return Response({'result': result}, status=status.HTTP_200_OK)
            except KeyError:
                return Response({'error': 'Invalid Roman numeral entered.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)