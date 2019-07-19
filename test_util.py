from util import find_phone_numbers, get_page_contents
import unittest


class UtilTest(unittest.TestCase):
    def test_find_phone_numbers(self):
        test_cases = {
            "https://hands.ru/company/about/": set(["84951370720"]),
            "https://repetitors.info/": set(
                ["84955405676", "88005555676", "88005057283", "88005057284"]
            ),
            "https://hh.ru/article/28": set(
                [
                    "88612055557",
                    "84952308739",
                    "84959746427",
                    "88124584545",
                    "88432121250",
                    "87272505084",
                    "84232023328",
                    "83432169773",
                    "88622965931",
                    "84732065065",
                    "84953360302",
                    "83832079464",
                    "84852670838",
                    "88314226600",
                    "88001006427",
                ]
            ),
            "https://yandex.com/company/contacts/moscow/": set(
                [
                    "84959743581",
                    "84957392211",
                    "84957397000",
                    "84957397070",
                    "84957392332",
                    "84959743586",
                    "84957392325",
                    "84957393777",
                ]
            ),
        }
        for url, numbers in test_cases.items():
            result = find_phone_numbers(get_page_contents(url))
            self.assertEqual(numbers, result)
