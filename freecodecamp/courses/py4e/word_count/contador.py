#!/usr/bin/env python3
# -*- coding: utf-8 -*-

counter = dict()
with open('texto.txt') as fhandle:
    lines = fhandle.readlines()
    for line in lines:
        if line == '\n':
            continue
        words = line.split()
        for word in words:
            word = word.strip()
            if word.find('/') == -1:
                for letter in word:
                    if not letter.isalpha():
                        word = word.replace(letter, '')
            else:
                poem = word.split('/')
                for word in poem:
                    for letter in word:
                        if not letter.isalpha():
                            word = word.replace(letter, '')
            counter[word] = counter.get(word, 0) + 1

# show most popular words
counter_desc = sorted(counter.items(), key=lambda x: x[1], reverse=True)
for item in counter_desc[:20]:
    k, v = item
    print(f'A palavra "{k}" apareceu "{v}" vezes no texto.')

print(counter)
