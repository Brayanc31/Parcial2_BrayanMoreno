# Demostración automática con justificación textual
EPSILON = 'ε'
EOF = '$'

gramatica = {
    'S': [['A', 'a', 'A', 'b'], ['B', 'b', 'B', 'a']],
    'A': [[EPSILON]],
    'B': [[EPSILON]]
}

def primeros_cadena(cadena, primeros):
    res = set()
    for sim in cadena:
        if sim in primeros:
            p = primeros[sim]
            res |= (p - {EPSILON})
            if EPSILON not in p:
                return res
        else:
            return {sim}
    return res | {EPSILON}

def calcular_primeros(gram):
    nts = list(gram.keys())
    primeros = {nt: set() for nt in nts}
    for _ in range(len(nts)):
        for nt, prods in gram.items():
            for prod in prods:
                primeros[nt] |= primeros_cadena(prod, primeros)
    return primeros

def calcular_siguientes(gram, primeros):
    nts = list(gram.keys())
    siguientes = {nt: set() for nt in nts}
    siguientes['S'].add(EOF)
    for _ in range(len(nts) * 2):
        for head, prods in gram.items():
            for prod in prods:
                for i, B in enumerate(prod):
                    if B in nts:
                        beta = prod[i+1:]
                        first_beta = primeros_cadena(beta, primeros)
                        siguientes[B] |= (first_beta - {EPSILON})
                        if EPSILON in first_beta:
                            siguientes[B] |= siguientes[head]
    return siguientes

def calcular_prediccion(gram, primeros, siguientes):
    pred = {}
    for head, prods in gram.items():
        for prod in prods:
            first_prod = primeros_cadena(prod, primeros)
            if EPSILON in first_prod:
                pred_set = (first_prod - {EPSILON}) | siguientes[head]
            else:
                pred_set = first_prod
            pred[(head, tuple(prod))] = pred_set
    return pred

def explicar_ll1(gram, prediccion):
    print("\nJUSTIFICACIÓN DE CONDICIÓN LL(1)\n")
    es_ll1 = True
    for head in gram:
        prods = [(prod, pred_set) for (h, prod), pred_set in prediccion.items() if h == head]
        if len(prods) > 1:
            print(f"Para el no terminal {head}:")
            for i in range(len(prods)):
                prod_str = ' '.join(prods[i][0])
                print(f"   Producción {i+1}: {head} → {prod_str} → PRED = {prods[i][1]}")
            # Verificar intersecciones
            conflictos = []
            for i in range(len(prods)):
                for j in range(i+1, len(prods)):
                    inter = prods[i][1] & prods[j][1]
                    if inter:
                        conflictos.append((i+1, j+1, inter))
                        es_ll1 = False
            if conflictos:
                for i, j, inter in conflictos:
                    print(f"   ✗ Conflicto: las producciones {i} y {j} comparten {inter}")
                print()
            else:
                print(f"   ✓ Los conjuntos PREDICCIÓN son disjuntos.\n")
        else:
            print(f"El no terminal {head} tiene una sola producción → no hay conflicto.\n")
    
    print("CONCLUSIÓN:")
    if es_ll1:
        print("La gramática ES LL(1) porque, para cada no terminal, los conjuntos PREDICCIÓN")
        print("de sus producciones son disjuntos. Esto significa que con un solo símbolo")
        print("de anticipación se puede decidir de manera única qué producción aplicar.")
    else:
        print("La gramática NO ES LL(1) debido a los conflictos mostrados arriba.")
    return es_ll1

if __name__ == "__main__":
    print("GRAMÁTICA:")
    for nt, prods in gramatica.items():
        for p in prods:
            print(f"  {nt} -> {' '.join(p)}")
    print()

    primeros = calcular_primeros(gramatica)
    siguientes = calcular_siguientes(gramatica, primeros)
    prediccion = calcular_prediccion(gramatica, primeros, siguientes)

    print("RESUMEN DE CONJUNTOS:")
    print("PRIMEROS:", {k: v for k, v in primeros.items()})
    print("SIGUIENTES:", {k: v for k, v in siguientes.items()})
    print("PREDICCIÓN:", {f"{k[0]} -> {' '.join(k[1])}": v for k, v in prediccion.items()})
    
    explicar_ll1(gramatica, prediccion)
