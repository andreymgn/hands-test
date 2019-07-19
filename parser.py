import re


class PhoneParser:
    """PhoneParser is a helper class for phone number extraction

    Attributes:
        regex is a regular expression which defines how data looks in general
        format is a format() function parameter and it defined how digits will be turned to 8KKKNNNNNNN format
        extract is a function which defines how to extract numbers for format from regex match
    """

    def __init__(self, regex, f, extract):
        self.regex = re.compile(regex)
        self.format = f
        self.extract = extract

    def parse(self, text):
        result = set()
        for match in self.regex.finditer(text):
            match = match.group()
            extracted = self.extract(match)
            formatted = self.format.format(extracted)
            if len(formatted) == 11:
                result.add(formatted)
        return result


with_city_code_8 = PhoneParser(
    r"\D(8\s?[-(]?\s?\d{3}s?[-)]?\s?\d{3}\s?[-()]?\s?\d{2}\s?[-()]?\s?\d{2})\D",
    "{}",
    lambda text: re.sub(r"\D", "", str(text)),
)

with_city_code_7 = PhoneParser(
    r"\D(\+7\s?[-(]?\s?\d{3}\s?[-)]?\s?\d{3}\s?[-()]?\s?\d{2}\s?[-()]?\s?\d{2})\D",
    "8{}",
    lambda text: re.sub(r"\D", "", str(text))[1:],
)

# https://ru.wikipedia.org/wiki/Телефонный_номер#История_формата_телефонных_номеров_в_России
# assuming 7-digit phone numbers from 2008
# expect three non-numeric characters before this to prevent matching numbers like 8 (123) 456-78-90
without_city_code = PhoneParser(
    r"\D{3}(\d{3}\s?-\s?\d{2}\s?-\s?\d{2})\D",
    "8495{}",
    lambda text: re.sub(r"\D", "", str(text)),
)
