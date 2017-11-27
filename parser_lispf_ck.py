import ox
import click
import pprint

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
    ('SUB', r'sub'),
    ('NUMBER', r'[0-9]+'),
    ('ignore_COMMENT', r';[^\n]*'),
    ('ignore_BREAK_LINE', r'\n'),
    ('ignore_SPACE', r'\s+')
])

tokens_list = ['DEC',
          'INC',
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
          'SUB',
          'NUMBER']

parser = ox.make_parser([
    ('expr : LPAR RPAR', lambda x,y: '()'),
    ('expr : LPAR term RPAR', lambda x,y,z: y),
    ('term : atom term', lambda x,y: (x,) + y),
    ('term : atom', lambda x : (x,)),
    ('atom : expr', lambda x : x),
    ('atom : DEC', lambda x : x),
    ('atom : INC', lambda x : x),
    ('atom : LOOP', lambda x : x),
    ('atom : RIGHT', lambda x : x),
    ('atom : LEFT', lambda x : x),
    ('atom : PRINT', lambda x : x),
    ('atom : READ', lambda x : x),
    ('atom : DO', lambda x : x),
    ('atom : DO_AFTER', lambda x : x),
    ('atom : DO_BEFORE', lambda x : x),
    ('atom : ADD', lambda x : x),
    ('atom : SUB', lambda x : x),
    ('atom : NUMBER', lambda x : x),
], tokens_list)

@click.command()
@click.argument('source', type=click.File('r'))

def make_tree(source):
    source_code = source.read()
    tokens = lexer(source_code)
    print('Lista de Tokens:\n', tokens)
    tree = parser(tokens)
    print("\nArvore Sintatica:")
    pprint.pprint(tree)

if __name__ == '__main__':
    make_tree()
