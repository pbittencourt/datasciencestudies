#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def arithmetic_arranger(problems: list, show_answers: bool = False) -> str:
    """
    Receives a list of strings that are arithmetic problems 
    and returns the problems arranged vertically and side-by-side.
    When `show_answers` is set to True, the answers are displayed.
    The limit of problems to display is five, and the functions
    only accepts additions and subtractions.
    
    :problems: list of strings that are arithmetic problems -> list
    :show_answers: if the answers should be displayed -> bool
    :returns: the problems arranged vertically and side-by-side -> str
    """

    first = []
    second = []
    line = []
    answer = []
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        try:
            oper = re.findall('[-+]', problem)[0]
        except:
            return "Error: Operator must be '+' or '-'."

        x, y = problem.split(oper)
        x = x.strip()
        y = y.strip()

        if len(x) > 4 or len(y) > 4:
            return "Error: Numbers cannot be more than four digits."

        if len(x) > len(y):
            width = len(x) + 2
        else:
            width = len(y) + 2

        if oper == '+':
            try:
                result = int(x) + int(y)
            except:
                return "Error: Numbers must only contain digits."
        elif oper == '-':
            try:
                result = int(x) - int(y)
            except:
                return "Error: Numbers must only contain digits."

        first.append(x.rjust(width))
        second.append(oper + ' ' + y.rjust(width - 2))
        line.append('-' * width)
        answer.append(str(result).rjust(width))

    gap = '    '
    arranged_problems = gap.join(first)
    arranged_problems += '\n' + gap.join(second)
    arranged_problems += '\n' + gap.join(line)
    if show_answers:
        arranged_problems += '\n' + gap.join(answer)
    return arranged_problems

if __name__ == '__main__':
    print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
