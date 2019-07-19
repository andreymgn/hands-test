import unittest

from parser import with_city_code_7, with_city_code_8, without_city_code


class ParserTest(unittest.TestCase):
    def test7(self):
        success_cases = [
            "+71234567890",
            "+7 123 456 78 90",
            "+7(123)456 78 90",
            "+7(123) 456 78 90",
            "+7(123)456-78-90",
            "+7(123) 456-78-90",
            "+7(123)456-7890",
        ]
        fail_cases = [
            "81234567890",  # wrong format
            "+7((1234567890",  # too many parenthesis
            "+7(123)-4567890",  # unexpected dash after parenthesis
            "+7123456789",  # not enough numbers
        ]
        # since regex expects non-numeric character before and after number, prepend and append 'a' to all test cases
        success_cases = ["a" + case + "a" for case in success_cases]
        fail_cases = ["a" + case + "a" for case in fail_cases]
        success_result = "81234567890"
        for case in success_cases:
            result = with_city_code_7.parse(case)
            self.assertEqual(len(result), 1)
            self.assertEqual(list(result)[0], success_result)
        for case in fail_cases:
            result = with_city_code_7.parse(case)
            self.assertEqual(len(result), 0)

    def test8(self):
        success_cases = [
            "81234567890",
            "8 123 456 78 90",
            "8(123)456 78 90",
            "8(123) 456 78 90",
            "8(123)456-78-90",
            "8(123) 456-78-90",
            "8(123)456-7890",
        ]
        fail_cases = [
            "+71234567890",  # wrong format
            "8((1234567890",  # too many parenthesis
            "8(123)-4567890",  # unexpected dash after parenthesis
            "8123456789",  # not enough numbers
        ]
        # since regex expects non-numeric character before and after number, prepend and append 'a' to all test cases
        success_cases = ["a" + case + "a" for case in success_cases]
        fail_cases = ["a" + case + "a" for case in fail_cases]
        success_result = "81234567890"
        for case in success_cases:
            result = with_city_code_8.parse(case)
            self.assertEqual(len(result), 1)
            self.assertEqual(list(result)[0], success_result)
        for case in fail_cases:
            result = with_city_code_8.parse(case)
            self.assertEqual(len(result), 0)

    def test_no_city(self):
        success_cases = ["123-45-67", "123 - 45 - 67"]
        fail_cases = [
            "+71234567890",
            "8((1234567890",
            "81234567890",
            "8(123)4567890",
            "8 (123) 456-78-90",
            "8123456789",
            "123 456 7",
        ]
        # since regex expects three non-numeric character before and after number, prepend and append 'a' to all test cases
        success_cases = ["aaa" + case + "a" for case in success_cases]
        fail_cases = ["aaa" + case + "a" for case in fail_cases]
        success_result = "84951234567"
        for case in success_cases:
            result = without_city_code.parse(case)
            self.assertEqual(len(result), 1)
            self.assertEqual(list(result)[0], success_result)
        for case in fail_cases:
            result = without_city_code.parse(case)
            self.assertEqual(len(result), 0)
