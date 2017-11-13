import ox

lexer = ox.make_lexer([
    ('loop', r'loop'),
    ('dec', r'dec'),
    ('inc', r'inc'),
    ('lpar', r'\('),
    ('rpar', r'\)'),
    ('right', r'right'),
    ('left', r'left'),
    ('print', r'print'),
    ('read', r'read')
])

tokens = ['dec', 'inc', 'right', 'left', 'print']

source = input('lispf_ck: ')
tokens = lexer(source)
print('tokens: ', tokens)
