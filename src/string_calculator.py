def add(numbers: str) -> int:
    if not numbers:
        return 0

    parts = numbers.split(",")
    total = sum(int(part) for part in parts)
    return total

