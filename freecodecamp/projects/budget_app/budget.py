#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import ndiff

class Category:

    def __init__(self: object, category: str) -> None:
        self.category = category
        self.ledger = list()
        self.budget = 0

    def __str__(self: object) -> str:
        """
        Print budget of the category when called via `print()`

        :returns: printed budget -> str
        """
        msg = f'{self.category:*^30}'
        for item in self.ledger:
            msg += '\n'
            amount =item['amount']
            description = item['description']
            msg += f'{description:<23.23}{amount:>7.2f}'
        msg += f'\nTotal: {self.get_balance():.2f}'

        return msg

    def check_funds(self: object, amount: float) -> bool:
        """
        Check if `amount` exceed the budget of the category.

        :amount: value to be compared to the balance -> float
        :returns: False if the amount is less than the balance of the budget
        caregory, True otherwise
        """
        return False if amount > self.budget else True

    def deposit(self: object, amount: float, description:str = '') -> None:
        """
        Method to deposit items in budget. Accept an amount and description.
        If no description is given, it defaults to an empty string.

        :amount: value to deposit -> float
        :description: what are we depositing? -> str
        :returns: None
        """
        item = {'amount': amount, 'description': description}
        self.budget += amount
        self.ledger.append(item)

    def withdraw(self: object, amount: float, description:str = '') -> bool:
        """
        Method to withdraw items in budget. Accept an amount and description.
        If no description is given, it defaults to an empty string.
        The amount is stored in the ledger as a negative number.
        If there are no enough budget, nothing should be added to the ledger.

        :amount: value to withdraw -> float
        :description: what are we wtihdrawing? -> str
        :returns: True if the widhdraw too place and False otherwise
        """
        if self.check_funds(amount):
            amount = -amount
            item = {'amount': amount, 'description': description}
            self.budget += amount
            self.ledger.append(item)
            return True
        else:
            return False

    def get_balance(self: object) -> float:
        """
        Returns the current balance of the budget category based on
        the deposits and withdrawals that have occured.

        :returns: the current balance -> float
        """
        return self.budget

    def transfer(self: object, amount: float, another_budget: object) -> bool:
        """
        Transfer `amount` from some budget category to `another budget` 
        category. Add a withdrawal with the amount and the description
        'Transfer to [Destination Budget Category]'. Then add a 
        deposit to the other budget category with the amount and the
        description 'Transfer from [Source Budget Category]'.
        If there are not enough funds, nothing should be added
        to either ledgers.

        :amount: value to be transfered -> float
        :another_budget: destination budget category -> object
        :returns: True if the transfer took place, False otherwise -> bool

        """
        if self.check_funds(amount):
            description = f'Transfer from {self.category}'
            another_budget.deposit(amount, description)

            amount = -amount
            item = {
                'amount': amount,
                'description': f'Transfer to {another_budget.category}'
            }
            self.budget += amount
            self.ledger.append(item)

            return True
        else:
            return False


def create_spend_chart(categories: list) -> str:
    """
    Takes a list of categories as argument and return a bar chart.

    :categories: list of categories (instances from `Category`) -> list
    :returns: bar chart -> str
    """
    msg = 'Percentage spent by category\n'

    # calc total spents in each category and the 
    # total spents in `categories` list
    totals = 0
    cat_total = dict()
    max_word_size = 0
    for category in categories:
        ledger = category.ledger
        name = category.category
        word_size = len(name)
        if word_size > max_word_size:
            max_word_size = word_size
        cat_total[name] = 0
        for item in ledger:
            amount = item['amount']
            if amount < 0:
                cat_total[name] += amount
        totals += cat_total[name]

    # calc percentages
    cat_percentage = dict()
    for category, amount in cat_total.items():
        percentage = 100 * (amount / totals)
        integer = round(percentage)
        nearest = 10 * (integer // 10)
        cat_percentage[category] = nearest

    # print axis
    for i in range(100, -1, -10):
        msg += f'{i:>3}| '
        for value in cat_percentage.values():
            if value < i:
                msg += '   '
            else:
                msg += 'o  '
        msg += '\n'

    # print separator
    width = len(categories) * 3
    msg += '    -' + '-' * width + '\n'

    # print labels
    for i in range(0, max_word_size):
        msg += '     '
        for category in categories:
            name = category.category
            try:
                msg += f'{name[i]}  '
            except:
                msg += f'   '
        if i < max_word_size - 1:
            msg += '\n'

    return msg


if __name__ == "__main__":
    food = Category('Food')
    business = Category('Business')
    entertainment = Category('Entertainment')

    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    actual = create_spend_chart([business, food, entertainment])

    for i, s in enumerate(ndiff(expected, actual)):
        if s[0] == ' ': continue
        elif s[0] == '-':
            print(u'Delete "{}" from position {}'.format(s[-1], i))
        elif s[0] == '+':
            print(u'Add "{}" to position {}'.format(s[-1], i))
        print()

    print(actual)
