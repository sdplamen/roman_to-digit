# Roman Numeral Converter

This project is a Django application that provides a web interface and a REST API for converting between Roman numerals and decimal numbers.

## Features

*   **Web Interface:** A simple UI to convert numbers to Roman numerals and vice-versa.
*   **REST API:** Endpoints for programmatic conversion.
*   **API Documentation:** Includes Swagger and ReDoc for interactive API documentation.
*   **Command-line script:** A standalone script (`roman_to_digit.py`) for conversions in the terminal.

## API Endpoints

The following API endpoints are available:

*   `api/to-roman/`: Converts a decimal number to a Roman numeral.
    *   **Method:** `POST`
    *   **Body:** `{"number": <integer>}`
*   `api/to-decimal/`: Converts a Roman numeral to a decimal number.
    *   **Method:** `POST`
    *   **Body:** `{"roman_number": "<string>"}`

### API Documentation

*   **Swagger UI
*   **ReDoc