import ox

lexer = ox.make_lexer([
	('NUMBER', r'[0-9]+'),
	('DO', r'do'),
	('ADD', r'add'),
    ('LOOP', r'loop'),
    ('DEC', r'dec'),
    ('INC', r'inc'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('RIGHT', r'right'),
    ('LEFT', r'left'),
    ('PRINT', r'print'),
    ('READ', r'read')
])

tokens = ['NUMBER', 'DO', 'ADD', 'LOOP, ''DEC', 'INC', 'LPAR', 'RPAR', 'LEFT', 'RIGHT', 'PRINT', 'READ']

parser = ox.make_parser([
	('term : LPAR DO ADD NUMBER RPAR', str),
], tokens)

source = input('lispf_ck: ')
tokens = lexer(source)
print('tokens: ', tokens)

#result = parser(tokens)
#print('result: ', result)
