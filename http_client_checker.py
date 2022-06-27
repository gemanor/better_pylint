""" Pylint checker plugin for checking usage of HTTP libraries """
from pylint.checkers import BaseRawFileChecker

IMPORT_TERMS = ['import', 'from']
REQUESTS_LIBRARIES = ['requests', 'urllib3']


class HTTPClientChecker(BaseRawFileChecker):
    """
    This class is a pylint checker for HTTPClient usage.
    To test it use the following command:
    `pylint --load-plugins=http_client_checker --disable=all --enable=W2400 handler.py`
    """

    name = "http_client_checker"
    msgs = {
        "W2400": (
            "requests library should not be used, use HTTPClient wrapper instead",
            "http-client-not-used",
            "Used when HTTPClient is not used."
        )
    }

    def process_module(self, node):
        """
        This method is called by pylint to process a file.
        :param file:
        :return:
        """
        if "http_client" in node.name:
            return

        with node.stream() as stream:
            for (lineno, line) in enumerate(stream):
                line_args = list(str(line, 'utf-8').split())
                indexes = [
                    index for index in range(len(line_args))
                    if line_args[index] in REQUESTS_LIBRARIES
                ]
                for index in indexes:
                    if index != 0 and line_args[index - 1] in IMPORT_TERMS:
                        self.add_message(
                            msgid="http-client-not-used",
                            line=lineno
                            )


def register(linter):
    """
    Register checker to pylint
    """
    linter.register_checker(HTTPClientChecker(linter))
