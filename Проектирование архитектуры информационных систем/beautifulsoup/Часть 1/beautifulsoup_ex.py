import re
import unittest

from bs4 import BeautifulSoup


def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as data:
        soup = BeautifulSoup(data, "lxml")

    body = soup.find(id="bodyContent")

    imgs = len((body.find_all('img', width=lambda x: int(x or 0) > 199)))

    headers = len([i.text for i in body.find_all(name=re.compile(r'[hH1-6]{2}')) if i.text[0] in 'ETC'])

    linkslen = 0
    link_found = body.find_next('a')
    while link_found:
        local_linklen = 1
        for i in link_found.find_next_siblings():
            if i.name == 'a':
                local_linklen += 1
            else:
                break
        linkslen = max(linkslen, local_linklen)
        link_found = link_found.find_next('a')

    lists = 0
    html_lists = body.find_all(['ul', 'ol'])
    for html_list in html_lists:
        if not html_list.find_parents(['ul', 'ol']):
            lists += 1

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
        )

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
