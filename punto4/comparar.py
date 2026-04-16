import random
import time
import matplotlib.pyplot as plt
from cyk_parser import cyk_parse
from ll1_parser import ll1_parse

def generar_expresion(profundidad):
   
    if profundidad == 0:
        return str(random.randint(1, 9))
    op = random.choice(['+', '-', '*', '/'])
    izq = generar_expresion(profundidad - 1)
    der = generar_expresion(profundidad - 1)
    return izq + op + der

def tokenizar(expr):
    return ['num' if c.isdigit() else c for c in expr]

def medir(parser, expr):
    tokens = tokenizar(expr)
    start = time.perf_counter()
    ok = parser(tokens)
    end = time.perf_counter()
    return end - start, ok

def main():
    
    profundidades = [1, 2, 3, 4, 5]   
    longitudes = []
    tiempos_cyk = []
    tiempos_ll1 = []

    print("Comparación CYK vs LL(1)\n")
    for prof in profundidades:
        expr = generar_expresion(prof)
        tokens = tokenizar(expr)
        n = len(tokens)
        t_cyk, ok_cyk = medir(cyk_parse, expr)
        t_ll1, ok_ll1 = medir(ll1_parse, expr)
        longitudes.append(n)
        tiempos_cyk.append(t_cyk)
        tiempos_ll1.append(t_ll1)
        print(f"n={n:3d} | CYK: {t_cyk:.6f}s | LL1: {t_ll1:.6f}s | válido={ok_cyk}")

    # Graficar
    plt.figure(figsize=(8,5))
    plt.loglog(longitudes, tiempos_cyk, 'o-', label='CYK (O(n³))', linewidth=2)
    plt.loglog(longitudes, tiempos_ll1, 's-', label='LL(1) predictivo (O(n))', linewidth=2)
    plt.xlabel('Longitud de la entrada (número de tokens)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de rendimiento: CYK vs LL(1)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('comparacion_parsers.png', dpi=150)
    plt.show()

    print("\n" + "="*60)
    print("CONCLUSIÓN")
    print("="*60)
    print(f"• Para n ≈ {longitudes[-1]}, CYK es ~{tiempos_cyk[-1]/tiempos_ll1[-1]:.1f} veces más lento.")
    print("• La gráfica muestra claramente la tendencia cúbica vs lineal.")
    print("• LL(1) es mucho más eficiente para una calculadora en tiempo real.")
    print("• CYK solo es útil si la gramática es no LL(1).")

if __name__ == "__main__":
    main()
