from typing import Callable
import re


def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total = sum(numbers_generator)
    return total


text = "Загальний дохід  складається з декількох частин:1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
