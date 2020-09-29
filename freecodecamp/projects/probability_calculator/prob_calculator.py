#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random

class Hat():

    def __init__(self: object, **balls: dict) -> None:
        """
        Receives a number of `balls`, with color and quantity, and
        stores in `contents` attribute.

        :**balls: dictionary with color as key and number as value
        :returns: None
        """
        self.contents = list()
        for ball, count in balls.items():
            for i in range(0, count):
                self.contents.append(ball)

    def draw(self: object, number: int) -> list:
        """
        Withdraw `number` elements from object.
        Return list of drawn elements, as strings.

        :number: number of elements to withdraw from object -> int
        :returns: list of drawn elements -> list
        """
        contents = self.contents
        withdraw = list()
        if number > len(contents):
            number = len(contents)
        for i in range(0, number):
            element = random.choice(contents)
            contents.remove(element)
            withdraw.append(element)
        return withdraw


def experiment(hat: object, expected_balls: list, num_balls_drawn: int, num_experiments: int) -> float:
    """
    Withdraw `num_balls_drawn` from `hat` object and check if
    `expected_balls` is a subgroup of its elements. Repeat the
    proccess `num_experiments` times and return the ratio
    between the successful events and the total.
    """

    match = 0
    total = num_experiments
    while num_experiments > 0:

        expected = list()
        for ball, count in expected_balls.items():
            for i in range(0, count):
                expected.append(ball)

        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        diff = copy.deepcopy(drawn)
        for item in expected:
            if item in diff:
                diff.remove(item)

        if len(diff) == len(drawn) - len(expected):
            match += 1

        num_experiments -= 1

    return match/total


if __name__ == "__main__":
    print('-'*50)
    hat = Hat(yellow=3, green=2, blue=4)
    probability = experiment(
        hat=hat,
        expected_balls={'yellow': 1, 'blue': 2},
        num_balls_drawn=5,
        num_experiments=10
    )
    print(probability)
    hat = Hat(blue=3,red=2,green=6)
    probability = experiment(
        hat=hat,
        expected_balls={"blue":2,"green":1},
        num_balls_drawn=4,
        num_experiments=1000
    )
    print(probability)
    hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
    probability = experiment(
        hat=hat,
        expected_balls={"yellow":2,"blue":3,"test":1},
        num_balls_drawn=20,
        num_experiments=100
    )
    print(probability)
