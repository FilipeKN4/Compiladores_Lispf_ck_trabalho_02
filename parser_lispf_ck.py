import ox
import click

lexer = ox.make_lexer([
    ('LOOP', r'loop'),
    ('DEC', r'dec'),
    ('INC', r'inc'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('RIGHT', r'right'),
    ('LEFT', r'left'),
    ('PRINT', r'print'),
    ('READ', r'read'),
    ('DO', r'do'),
    ('DO_AFTER', r'do-after'),
    ('DO_BEFORE', r'do-before'),
    ('ADD', r'add'),
    ('NUMBER', r'[0-9]+'),
    ('COMMENT', r';[^\n]*'),
    ('BREAK_LINE', r'\n'),
    ('SPACE', r'\s')
])

tokens = ['DEC',
          'INC',
          'RIGHT',
          'LEFT',
          'PRINT',
          'LOOP',
          'LPAR',
          'RPAR',
          'RIGHT',
          'LEFT',
          'PRINT',
          'READ',
          'DO',
          'DO_AFTER',
          'DO_BEFORE',
          'ADD',
          'NUMBER',
          'COMMENT',
          'BREAK_LINE',
          'SPACE']

@click.command()
@click.argument('source', type=click.File('r'))

def make_ast(source):
    source_code = source.read()
    tokens = lexer(source_code)
    print('tokens: ', tokens)

if __name__ == '__main__':
    make_ast()
