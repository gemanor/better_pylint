from tokenize import NAME, OP
from pylint.checkers import BaseTokenChecker


class GoldenHammerChecker(BaseTokenChecker):
    name = "golden_hammer_checker"
    msgs = {
        "R2403": (
            "Multiple if statements with the same %s condition found, replace it with match/case statement",
            "use-match-case-instead-of-same-condition-if",
            "Used when match case should be used instead of same condition if."
        )
    }

    def __init__(self, linter):
        super().__init__(linter)

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
            [self.add_message('R2403', line=line, args=condition)
                for line in lines if len(lines) > 1]


def register(linter):
    linter.register_checker(GoldenHammerChecker(linter))
