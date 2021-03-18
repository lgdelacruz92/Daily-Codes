from pygments import highlight
from pygments.lexers import guess_lexer 
from pygments.token import STANDARD_TYPES, Keyword
from pygments.formatters import HtmlFormatter
import sys

with open(sys.argv[1], 'r') as test_file:
    code = test_file.read()
    lexer = guess_lexer(code) 
    print(highlight(code, lexer, HtmlFormatter()))