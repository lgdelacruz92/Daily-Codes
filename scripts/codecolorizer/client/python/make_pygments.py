from pygments import highlight
from pygments.lexers.python import PythonLexer 
from pygments.token import STANDARD_TYPES, Keyword
from pygments.formatters import HtmlFormatter
import sys

with open(sys.argv[1], 'r') as test_file:
    code = test_file.read()
    lexer = PythonLexer()
    print(highlight(code, lexer, HtmlFormatter()))