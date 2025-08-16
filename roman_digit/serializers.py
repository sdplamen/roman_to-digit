from rest_framework import serializers

class ToRomanSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=1, max_value=3999, help_text="An integer between 1 and 3999 to convert to Roman numerals.")

class ToDecimalSerializer(serializers.Serializer):
    roman_number = serializers.CharField(max_length=15, help_text="A valid Roman numeral (e.g., 'XII') to convert to an integer.")