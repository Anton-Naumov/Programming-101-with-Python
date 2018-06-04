from term import Term


class Polinom:
    def __init__(self, terms):
        self._terms = {}

        for term in terms:
            self.add_term(term)

    def add_term(self, term):
        if term.power not in self._terms:
            self._terms[term.power] = term
        else:
            self._terms[term.power] += term

    def __str__(self):
        sorted_terms = []

        for term_power in sorted(self._terms.keys(), reverse=True):
            if self._terms[term_power] != Term.constant(0):
                sorted_terms.append(str(self._terms[term_power]))

        return ' + '.join(sorted_terms)

    def derivative(self):
        terms_derivatives = [
            term.derived for term in self._terms.values()
        ]

        return Polinom(terms_derivatives)

    @classmethod
    def parse_from_string(cls, s):
        unparsed_terms = s.split('+')

        terms = [
            Term.parse_term(t) for t in unparsed_terms
        ]

        return cls(terms)
