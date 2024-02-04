# для роботи з регулярними виразами
import re
# для використання функції як параметру в іншій функції
from typing import Callable

# функція для пошуку чисел в тексті
# повертає знайдені числа як генератор
def generator_numbers(text: str):
    # перевіряємо чи текст не None і не пустий
    if text is not None and text != '':
        # розбиваємо текст на частини по пробілу і записуємо їх у список
        list_of_words_drom_text = text.split(" ")
        # створюємо шаблон для пошуку тільки чисел
        pattern = r"([0-9]+\.?[0-9]?)"
        # цикл для пошуку чисел
        for str_in_list in list_of_words_drom_text:
            # якщо рядок то число
            if re.search(pattern, str_in_list) is not None:
                # повертаємо число
                yield str_in_list

# функція для розрахунку суми чисел у тексті
def sum_profit(text: str, func: Callable) -> float:
    # створюмо змінну для суми чисел
    add_all_digits = 0
    # входимо у цикл щоб пройтись генератором по всім чслам
    for digit in func(text):
        # записуємо всі числа до змінної
        # попередньо її перетворивши у float
        add_all_digits += float(digit)
    # повертаємо суму чисел
    return add_all_digits
   
# наш текст для перевірки роботи логіки
our_text = "Загальний дохід працівника складається з декількох частин: \
    1000.01 як основний дохід, \
    доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# викликаємо нашу логіку і друкуємо результат
print(sum_profit(our_text, generator_numbers))
