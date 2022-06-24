from pylint.checkers import BaseChecker
from astroid import AssignAttr


class NoClassChecker(BaseChecker):

    name = "no_class_checker"
    msgs = {
        "R2401": (
            "Missing init function, class should not be used",
            "class-not-used-missing-init-function",
            "Used when class should not be used."
        ),
        "R2402": (
            "No self assignement in constrcutor",
            "class-not-used-no-self-assignment",
            "Used when class has no self assignment in constructor."
        )
    }

    def __init__(self, linter):
        super().__init__(linter)

    def leave_classdef(self, node):
        if node.bases:
            return

        has_constructor = '__init__' in [m.name for m in node.mymethods()]
        if not has_constructor:
            self.add_message(
                msgid="class-not-used-missing-init-function",
                line=node.fromlineno
            )
            return

        const_func = node.local_attr('__init__')[0]
        has_self_assignment = 'self' in [
            a.expr.name for a in const_func.nodes_of_class(AssignAttr)
        ]
        if not has_self_assignment:
            self.add_message(
                msgid="class-not-used-no-self-assignment",
                line=node.fromlineno
            )


def register(linter):
    linter.register_checker(NoClassChecker(linter))
