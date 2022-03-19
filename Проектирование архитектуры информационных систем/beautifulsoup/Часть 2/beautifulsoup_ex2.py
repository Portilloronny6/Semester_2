import os
import re

from bs4 import BeautifulSoup


def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")
    files = dict.fromkeys(os.listdir(path))
    link_list = [start]
    while link_list:
        for id, link in enumerate(link_list):
            with open("{}{}".format(path, link), encoding='utf-8') as data:
                file_links = link_re.findall(data.read())
                for lnk in [i for i in file_links if i in files.keys()]:
                    if files.get(lnk) is None:
                        files[lnk] = link
                        if lnk == end:
                            return files
                        link_list.append(lnk)
            link_list.pop(id)
    return files


def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    parent = end
    bridge = [parent]
    while parent != start:
        parent = files[parent]
        if parent is not None:
            bridge.append(parent)
        else:
            bridge.append(start)
            parent = start
    return bridge[::-1]


def parse(start, end, path):
    bridge = build_bridge(start, end, path)
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file), encoding='utf-8') as data:
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

        out[file] = [imgs, headers, linkslen, lists]

    return out


if __name__ == '__main__':
    correct = {
        'Stone_Age': [13, 10, 12, 40],
        'Brain': [19, 5, 25, 11],
        'Artificial_intelligence': [8, 19, 13, 198],
        'Python_(programming_language)': [2, 5, 17, 41],
    }
    start = 'Stone_Age'
    end = 'Python_(programming_language)'
    path = '../wiki/'

    print('parse result:', parse(start, end, path))
    print('correct result', correct)
