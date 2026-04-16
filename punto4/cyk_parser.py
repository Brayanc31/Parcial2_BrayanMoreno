
# Gramática en CNF para expresiones aritméticas con +, -, *, / y paréntesis.
# No terminales: E, T, F, A1, A2, P, C
# Terminales: num, +, -, *, /, (, )

CNF_PRODUCTIONS = {
    'E': [('E', 'A1'), ('T',)],
    'A1': [('+', 'T'), ('-', 'T')],
    'T': [('T', 'A2'), ('F',)],
    'A2': [('*', 'F'), ('/', 'F')],
    'F': [('P', 'E'), ('C',), ('num',)],
    'P': [('(',)],
    'C': [(')',)],
}

def cyk_parse(tokens):
    """Retorna True si la lista de tokens es generada por la gramática."""
    n = len(tokens)
    if n == 0:
        return False
    table = [[set() for _ in range(n)] for _ in range(n)]
    # Diagonal
    for i in range(n):
        tok = tokens[i]
        for nt, rhs_list in CNF_PRODUCTIONS.items():
            for rhs in rhs_list:
                if len(rhs) == 1 and rhs[0] == tok:
                    table[i][i].add(nt)
    # Longitudes mayores
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for nt, rhs_list in CNF_PRODUCTIONS.items():
                    for rhs in rhs_list:
                        if len(rhs) == 2:
                            B, C = rhs
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(nt)
    return 'E' in table[0][n-1]
