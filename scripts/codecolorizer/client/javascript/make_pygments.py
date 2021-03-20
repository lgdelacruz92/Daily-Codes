from pygments import highlight
from pygments.lexers.javascript import JavascriptLexer 
from pygments.formatters import HtmlFormatter
import sys

with open(sys.argv[1], 'r') as test_file:
    code = test_file.read()
    lexer = JavascriptLexer()
    print(highlight(code, lexer, HtmlFormatter()))