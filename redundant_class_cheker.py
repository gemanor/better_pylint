"""Pylint checker plugin for checking redundant class definition# """
from pylint.checkers import BaseChecker
from astroid import AssignAttr


class RedundantClassChecker(BaseChecker):
    """
    Checker for redundant class
    """
    name = "redundant_class_cheker.py"
    msgs = {
        "W2501": (
            "Missing init function, class should not be used",
            "class-not-used-missing-init-function",
            "Used when class should not be used."
        ),
        "W2502": (
            "No self assignement in constrcutor",
            "class-not-used-no-self-assignment",
            "Used when class has no self assignment in constructor."
        )
    }

    def leave_classdef(self, node):
        """
        Checks if class has init function and if it has
        self assignment in constructor.
        """
        if node.bases:
            return

        has_constructor = '__init__' in [m.name for m in node.mymethods()]
        if not has_constructor:
            self.add_message(
                msgid="W2501",
                node=node
            )
            return

        const_func = node.local_attr('__init__')[0]
        has_self_assignment = 'self' in [
            a.expr.name for a in const_func.nodes_of_class(AssignAttr)
        ]
        if not has_self_assignment:
            self.add_message(
                msgid="W2502",
                node=const_func
            )


def register(linter):
    """
    Register checker to pylint
    """
    linter.register_checker(RedundantClassChecker(linter))
