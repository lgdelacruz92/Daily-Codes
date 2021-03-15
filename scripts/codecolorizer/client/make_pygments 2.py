from pygments import highlight
from pygments.lexers import  get_lexer_by_name
from pygments.formatters import HtmlFormatter

with open('./test_grog.c', 'r') as test_file:
    code = test_file.read()
    lexer = get_lexer_by_name('c', stripall=True)
    print(highlight(code, lexer, HtmlFormatter()))