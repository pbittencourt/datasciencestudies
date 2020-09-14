#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def arithmetic_arranger(lst, show_answers):
    """Faz aquelas parada doida mano

    :lst: TODO
    :returns: TODO

    """
    pass


conta = "52-235"
oper = re.findall('\D', conta)
oper = oper[0]
x,y = conta.split(oper)

if len(x) > len(y):
    size = len(x) + 2
else:
    size = len(y) + 2

if oper == '+':
    result = int(x) + int(y)
elif oper == '-':
    result = int(x) - int(y)
else:
    result = None

print(x.rjust(size))
print(oper, end=' ')
print(y.rjust(size-2))
print('-' * size)
print(str(result).rjust(size))
