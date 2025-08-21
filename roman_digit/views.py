from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from roman_digit.serializers import ToRomanSerializer, ToDecimalSerializer
from roman_digit.logic import roman_to_dec, dec_to_roman

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
    def post(self, request):
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
    def post(self, request):
        serializer = ToDecimalSerializer(data=request.data)
        if serializer.is_valid():
            roman_num = serializer.validated_data['roman_number'].upper()
            try:
                result = roman_to_dec(roman_num)
                return Response({'result': result}, status=status.HTTP_200_OK)
            except KeyError:
                return Response({'error': 'Invalid Roman numeral entered.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)