import re
from functools import total_ordering
from utility import extract_term


@total_ordering
class Term:
    def __init__(self, *, coeff, variable='x', power):
        if coeff < 0:
            raise AttributeError('coeff must be positive')
        if power < 0:
            raise AttributeError('power must be positive')
        if re.match('[a-z]$', variable) is None:
            raise AttributeError('variable must be small latin letter (a-z)')

        self.coeff = coeff
        self.variable = variable
        self.power = power

    @classmethod
    def constant(cls, constant):
        return cls(coeff=constant, power=0)

    @property
    def is_constant(self):
        return self.power == 0

    def __str__(self):
        if self.coeff == 0:
            return '0'
        if self.is_constant:
            return str(self.coeff)

        coeff = '' if self.coeff == 1 else f'{self.coeff}*'
        power = '' if self.power == 1 else f'^{self.power}'

        return f'{coeff}{self.variable}{power}'

    def __eq__(self, other):
        return (
            self.coeff == other.coeff and
            self.variable == other.variable and
            self.power == other.power
        )

    def __add__(self, other):
        assert self.variable == other.variable, 'Terms variables must be equal'
        assert self.power == other.power, 'Terms powers must be equal'

        return Term(
            coeff=self.coeff + other.coeff,
            power=self.power
        )

    def __gt__(self, other):
        return self.power > other.power

    def __repr__(self):
        return str(self)

    @property
    def derived(self):
        return Term(
            coeff=self.coeff * self.power,
            power=max(0, self.power - 1)
        )

    @classmethod
    def parse_term(cls, string):
        parts = extract_term(string)

        return Term(
            coeff=parts[0],
            variable=parts[1],
            power=parts[2]
        )
