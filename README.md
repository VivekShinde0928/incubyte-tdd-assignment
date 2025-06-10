# Incubyte TDD Assignment - String Calculator (Python)

This repository contains my solution to the **Incubyte TDD Kata Assignment** 

# What is Implemented

This project follows **Test-Driven Development (TDD)** and builds a simple **String Calculator** function

#Function Signature:
""""
def add(numbers: str) -> int
""""

#Features Implemented:
Returns 0 for an empty string

Returns the number itself for a single number string (e.g., "1" → 1)

Returns the sum of two comma-separated numbers (e.g., "1,2" → 3)

#How to Run the Tests:
**** Prerequisites ****
Python 3.8+
pytest

# Create and activate virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

#  Folder Structure:
incubyte-tdd-assignment/ 
|src/
|   ─ string_calculator.py        # Main logic
|── tests/
|   ─ test_string_calculator.py  # Unit tests using pytest
|── requirements.txt
|── README.md

