from urllib.request import urlopen

from parser import with_city_code_7, with_city_code_8, without_city_code


def get_page_contents(url):
    resource = urlopen(url)
    return resource.read().decode(resource.headers.get_content_charset())


def find_phone_numbers(text):
    return (
        with_city_code_7.parse(text)
        | with_city_code_8.parse(text)
        | without_city_code.parse(text)
    )


def process_file(filename):
    result = {}
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            result[line] = find_phone_numbers(get_page_contents(line))

    return result
