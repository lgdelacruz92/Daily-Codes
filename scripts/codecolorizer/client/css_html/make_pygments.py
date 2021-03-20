from pygments import highlight
from pygments.lexers.css import CssLexer 
from pygments.formatters import HtmlFormatter
import sys

with open(sys.argv[1], 'r') as test_file:
    code = test_file.read()
    print(highlight(code, CssLexer(), HtmlFormatter()))