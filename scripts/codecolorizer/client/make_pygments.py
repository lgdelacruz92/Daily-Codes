from pygments import highlight
from pygments.lexers.jvm import JavaLexer
from pygments.token import STANDARD_TYPES, Keyword
from pygments.formatters import HtmlFormatter
import sys

with open(sys.argv[2], 'r') as test_file:
    code = test_file.read()
    lexer = JavaLexer()
    print(highlight(code, lexer, HtmlFormatter()))