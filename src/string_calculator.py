import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ",|\n"

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        custom_delimiter = parts[0][2:]
        delimiter = re.escape(custom_delimiter)
        numbers = parts[1]

    parts = re.split(delimiter, numbers)
    negatives = [n for n in parts if int(n) < 0]

    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(negatives)}")

    return sum(int(n) for n in parts)

