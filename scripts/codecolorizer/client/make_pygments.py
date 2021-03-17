from pygments import highlight
from pygments.lexers import  get_lexer_by_name
from pygments.formatters import HtmlFormatter
import sys

with open(sys.argv[2], 'r') as test_file:
    code = test_file.read()
    lexer = get_lexer_by_name(sys.argv[1], stripall=True)
    print(highlight(code, lexer, HtmlFormatter()))