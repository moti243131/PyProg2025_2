from typing import Literal


def guess_number(
    target: int,
    numbers_list: list[int],
    method: Literal["linear", "binary"],
) -> tuple[int, int]:
    """Находит число в списке и возвращает его вместе с количеством сравнений.

    Использует либо медленный перебор (linear), либо алгоритм бинарного
    поиска (binary). Список может быть не отсортирован — для binary
    создаётся отсортированная копия.

    Args:
        target: Искомое число.
        numbers_list: Список чисел без дубликатов (может быть не отсортирован).
        method: "linear" — перебор слева направо, "binary" — бинарный поиск.

    Returns:
        Кортеж (угаданное число, количество сравнений/угадываний).

    Raises:
        ValueError: Если target отсутствует в numbers_list.
    """
    if target not in numbers_list:
        raise ValueError(f"Число {target} отсутствует в списке")

    if method == "linear":
        return _linear_search(target, numbers_list)
    return _binary_search(target, numbers_list)


def _linear_search(target: int, numbers_list: list[int]) -> tuple[int, int]:
    """Линейный поиск: перебор элементов слева направо."""
    guesses = 0
    for num in numbers_list:
        guesses += 1
        if num == target:
            return target, guesses
    raise ValueError(f"Число {target} отсутствует в списке")


def _binary_search(target: int, numbers_list: list[int]) -> tuple[int, int]:
    """Бинарный поиск на отсортированной копии списка."""
    sorted_list = sorted(numbers_list)
    left, right = 0, len(sorted_list) - 1
    guesses = 0

    while left <= right:
        mid = (left + right) // 2
        mid_val = sorted_list[mid]
        guesses += 1

        if mid_val == target:
            return target, guesses
        if mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError(f"Число {target} отсутствует в списке")


def input_range_from_keyboard() -> tuple[int, int]:
    """Запрашивает начало и конец диапазона с клавиатуры.

    Валидирует ввод: начало должно быть не больше конца.
    Повторяет запрос при некорректном вводе.

    Returns:
        Кортеж (начало_диапазона, конец_диапазона).

    Raises:
        ValueError: При нечисловом вводе или если start > end.
    """
    while True:
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
            if start > end:
                print("Ошибка: начало должно быть <= конца. Повторите ввод.")
                continue
            return start, end
        except ValueError:
            print("Ошибка: введите целые числа. Повторите ввод.")


def main() -> None:
    """Демонстрация работы guess_number."""
    numbers = list(range(1, 101))

    result_linear = guess_number(42, numbers, "linear")
    print(f"Linear: число {result_linear[0]}, угадываний: {result_linear[1]}")

    result_binary = guess_number(42, numbers, "binary")
    print(f"Binary: число {result_binary[0]}, угадываний: {result_binary[1]}")


if __name__ == "__main__":
    main()
