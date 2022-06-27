""" Pylint checker plugin for checking usage of repetative if """
from tokenize import NAME, OP
from pylint.checkers import BaseTokenChecker


class GoldenHammerChecker(BaseTokenChecker):
    """
    This class is a pylint checker for if usage in same expression many times.
    """
    name = "golden_hammer_checker"
    msgs = {
        "R2403": (
            "Multiple if statements with the same `%s` condition found, \
                replace it with match/case statement",
            "use-match-case-instead-of-same-condition-if",
            "Used when match case should be used instead of same condition if."
        )
    }

    def _get_current_if(self, tokens, curr):
        current_dynamic = []
        for token in tokens[curr+1:]:
            if token.type != NAME and token.type != OP:
                continue
            if token.type == OP and token.string == ":":
                break
            current_dynamic.append(token.string)
        return ''.join(current_dynamic)

    def process_tokens(self, tokens):
        conditions = {}
        for token in tokens:
            if token.type == NAME and token.string == "if":
                condition = self._get_current_if(tokens, tokens.index(token))
                if condition and condition not in conditions:
                    conditions[condition] = [token.start[0]]
                elif condition and condition in conditions:
                    conditions[condition].append(token.start[0])

        for condition, lines in conditions.items():
            for line in lines if len(lines) > 1 else []:
                self.add_message('R2403', line=line, args=condition)


def register(linter):
    """
    register checker to pylint
    """
    linter.register_checker(GoldenHammerChecker(linter))
