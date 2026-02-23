import unittest

from guess_number import guess_number


class TestGuessNumber(unittest.TestCase):
    def test_linear_finds_first(self) -> None:
        """Линейный поиск находит число в начале списка."""
        numbers = [5, 1, 3, 2, 4]
        result = guess_number(5, numbers, "linear")
        self.assertEqual(result, (5, 1))

    def test_linear_finds_last(self) -> None:
        """Линейный поиск находит число в конце списка."""
        numbers = [1, 2, 3, 4, 5]
        result = guess_number(5, numbers, "linear")
        self.assertEqual(result, (5, 5))

    def test_binary_sorted(self) -> None:
        """Бинарный поиск на отсортированном списке."""
        numbers = list(range(1, 11))
        result = guess_number(7, numbers, "binary")
        self.assertEqual(result[0], 7)
        self.assertLessEqual(result[1], 4)

    def test_binary_unsorted(self) -> None:
        """Бинарный поиск работает на неотсортированном списке."""
        numbers = [10, 3, 7, 1, 5, 9, 2, 8, 4, 6]
        result = guess_number(7, numbers, "binary")
        self.assertEqual(result[0], 7)
        self.assertLessEqual(result[1], 5)

    def test_binary_fewer_guesses(self) -> None:
        """Бинарный поиск даёт меньше сравнений на большом диапазоне."""
        numbers = list(range(1, 1001))
        _, linear_count = guess_number(500, numbers, "linear")
        _, binary_count = guess_number(500, numbers, "binary")
        self.assertLess(binary_count, linear_count)

    def test_target_not_in_list(self) -> None:
        """ValueError если target отсутствует в списке."""
        numbers = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            guess_number(10, numbers, "linear")
        with self.assertRaises(ValueError):
            guess_number(10, numbers, "binary")

    def test_single_element(self) -> None:
        """Список из одного элемента."""
        numbers = [42]
        for method in ("linear", "binary"):
            result = guess_number(42, numbers, method)
            self.assertEqual(result, (42, 1))


if __name__ == "__main__":
    unittest.main()
