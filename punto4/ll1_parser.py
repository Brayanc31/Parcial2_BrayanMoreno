# ll1_parser.py
# Gramática LL(1) para el mismo lenguaje:
#   E  -> T E'
#   E' -> + T E' | - T E' | ε
#   T  -> F T'
#   T' -> * F T' | / F T' | ε
#   F  -> ( E ) | num

TERMINALS = {'num', '+', '-', '*', '/', '(', ')'}
LL1_TABLE = {
    ('E', 'num'): 'E -> T E\'',
    ('E', '('):   'E -> T E\'',
    ('E\'', '+'): 'E\' -> + T E\'',
    ('E\'', '-'): 'E\' -> - T E\'',
    ('E\'', ')'): 'E\' -> ε',
    ('E\'', '$'): 'E\' -> ε',
    ('T', 'num'): 'T -> F T\'',
    ('T', '('):   'T -> F T\'',
    ('T\'', '+'): 'T\' -> ε',
    ('T\'', '-'): 'T\' -> ε',
    ('T\'', '*'): 'T\' -> * F T\'',
    ('T\'', '/'): 'T\' -> / F T\'',
    ('T\'', ')'): 'T\' -> ε',
    ('T\'', '$'): 'T\' -> ε',
    ('F', 'num'): 'F -> num',
    ('F', '('):   'F -> ( E )',
}

def ll1_parse(tokens):
    tokens = tokens + ['$']
    stack = ['$', 'E']
    idx = 0
    while stack:
        top = stack.pop()
        if top in TERMINALS or top == '$':
            if top == tokens[idx]:
                idx += 1
            else:
                return False
        else:
            lookahead = tokens[idx]
            key = (top, lookahead)
            if key not in LL1_TABLE:
                return False
            prod = LL1_TABLE[key]
            if prod == 'E -> T E\'':
                stack.extend(['E\'', 'T'])
            elif prod == 'E\' -> + T E\'':
                stack.extend(['E\'', 'T', '+'])
            elif prod == 'E\' -> - T E\'':
                stack.extend(['E\'', 'T', '-'])
            elif prod == 'E\' -> ε':
                pass
            elif prod == 'T -> F T\'':
                stack.extend(['T\'', 'F'])
            elif prod == 'T\' -> * F T\'':
                stack.extend(['T\'', 'F', '*'])
            elif prod == 'T\' -> / F T\'':
                stack.extend(['T\'', 'F', '/'])
            elif prod == 'T\' -> ε':
                pass
            elif prod == 'F -> num':
                stack.append('num')
            elif prod == 'F -> ( E )':
                stack.extend([')', 'E', '('])
            else:
                return False
    return True
