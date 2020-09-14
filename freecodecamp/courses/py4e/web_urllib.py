#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counter = dict()
for line in handle:
    line = line.decode().strip()
    print(line)
    words = line.split()
    for word in words:
        counter[word] = counter.get(word, 0) + 1

alist = sorted([(v, k) for k, v in counter.items()], reverse=True)
for item in alist:
    occ, word  = item
    if occ <= 1:
        break
    print(f'The word "{word}" has occurred {occ} times.')
