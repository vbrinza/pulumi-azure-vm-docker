import requests
from bs4 import BeautifulSoup
from collections import Counter
import sys


def parse_page(target_url):
    words_list = []
    source_code = requests.get(target_url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.findAll('body'):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            words_list.append(each_word)
        clean_tags(words_list)


def clean_tags(words_list):
    cleaned_list = []
    for word in words_list:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            cleaned_list.append(word)
    output_words(cleaned_list)


def output_words(cleaned_list):
    word_count = {}

    for word in cleaned_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    c = Counter(word_count)
    top = c.most_common(1)
    print(top)


if __name__ == '__main__':
    url = (sys.stdin.read())
    parse_page(url.strip())
