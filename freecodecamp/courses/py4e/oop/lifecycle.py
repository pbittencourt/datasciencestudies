#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Roboto:

    """Docstring for Roboto. """

    name = ''
    hails = 0

    def __init__(self, name):
        self.name = name
        print(f'Roboto {name} created. Praise the Lord!')

    def hail(self):
        self.hails += 1
        print(f'Roboto {self.name} is hailing at you {self.hails} times.')

    def __del__(self):
        print(f'You have DESTROYED {self.name}! You\'re going to pay! {self.name.upper()} will HAUNT you till DEATH! PRAISE THE LORD!!!111!11!')


baphomet = Roboto('Baphomet')
baphomet.hail()
baphomet.hail()
baphomet.hail()
baphomet.hail()
baphomet.hail()
baphomet.hail()
baphomet.hail()

baphomet = 'cute panda'
print(baphomet)
