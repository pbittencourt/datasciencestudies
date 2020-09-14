#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

document = 'example.xml'
with open(document) as handle:
    lines = handle.readlines()
    line2 = lines[1]
    keys = re.findall('xmlns:\S*=', line2)
    values = re.findall('="(.+?)"', line2)
    for key in keys:
        print(key)
    for value in values:
        print(value)

