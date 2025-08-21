from rest_framework import serializers

class ToRomanSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=1, max_value=3999)

class ToDecimalSerializer(serializers.Serializer):
    roman_number = serializers.CharField(max_length=50)
