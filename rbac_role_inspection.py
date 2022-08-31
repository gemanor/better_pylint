""" Pylint checker plugin for checking usage of repetative if """
from tokenize import OP, AT, NEWLINE, STRING
from pylint.checkers import BaseTokenChecker


class RBACRoleInspectionChecker(BaseTokenChecker):
    """
    This class is a pylint checker for if usage in same expression many times.
    """
    name = "rbac_role_inspection"
    msgs = {
        "W2406": (
            "Authorizer with `all` should be used with caution and only from inpected code.",
            "do-not-use-all-authorizer",
            "Used when Authorizer with `all` is used."
        )
    }

    def _check_authorizer(self, tokens, curr):
        for token in tokens[curr+1:]:
            if token.type == STRING and token.string.find("all") != -1:
                return True
            if token.type == NEWLINE:
                return False
        return False

    def process_tokens(self, tokens):
        for index, token in enumerate(tokens):
            if token.type == OP and token.exact_type == AT:
                bad_authorizer = self._check_authorizer(tokens, index)
                if bad_authorizer:
                    self.add_message('W2406', line=token.start[0])


def register(linter):
    """
    register checker to pylint
    """
    linter.register_checker(RBACRoleInspectionChecker(linter))
