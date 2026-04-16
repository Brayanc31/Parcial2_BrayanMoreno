
# Parcial 2 - Compiladores

**Estudiante:** Brayan Moreno  
**Fecha:** Abril 2026

---

## Estructura de la entrega

```
Parcial2_BrayanMoreno/
├── Punto1_Gramatica_CRUD/
│   └── gramatica_crud.txt
├── Punto2_ANTLR/
│   ├── CRUD.g4
│   ├── main.py
│   ├── CRUDLexer.py
│   ├── CRUDParser.py
│   └── CRUDListener.py
├── Punto3_Demostracion_LL1/
│   ├── demostracion_ll1.py
│   └── salida_demostracion.txt
├── Punto4_Comparacion_CYK_LL1/
│   ├── cyk_parser.py
│   ├── ll1_parser.py
│   ├── comparar.py
│   └── comparacion_parsers.png
├── Punto5_Calculadora_Booleana/
│   ├── boolean_calc.y
│   └── captura_ejecucion.txt
└── README.md
```

---

## Punto 1 – Gramática CRUD (Diseño)

**Archivo:** `Punto1_Gramatica_CRUD/gramatica_crud.txt`

**Nota:** Este punto es únicamente de **diseño teórico**. No requiere ejecución ni implementación.

Se diseñó una gramática independiente del contexto (BNF) para un lenguaje de programación que permite operaciones CRUD sobre una base de datos no relacional.

### Características de la gramática
- **Operaciones:** `create`, `read`, `update`, `delete`
- **Estructuras:** Diccionarios anidados (`{clave: valor, ...}`)
- **Tipos de datos:** Strings, números, booleanos
- **Separadores:** Punto y coma (`;`) o salto de línea (`\n`)

### Gramática (resumen)

```
<programa>      ::= <instruccion> { <instruccion> }
<instruccion>   ::= <operacion> ( ";" | "\n" )
<operacion>     ::= <create_op> | <read_op> | <update_op> | <delete_op>
<create_op>     ::= "create" "(" <id> "," <diccionario> ")"
<read_op>       ::= "read" "(" <id> "," <diccionario> ")"
<update_op>     ::= "update" "(" <id> "," <diccionario> "," <diccionario> ")"
<delete_op>     ::= "delete" "(" <id> "," <diccionario> ")"
<diccionario>   ::= "{" [ <pares> ] "}"
<pares>         ::= <par> { "," <par> }
<par>           ::= <string> ":" <valor>
<valor>         ::= <string> | <numero> | <booleano> | <diccionario>
```

La gramática completa se encuentra en el archivo `gramatica_crud.txt`.

---

## Punto 2 – Implementación en ANTLR

**Archivos:** `Punto2_ANTLR/`

### Requisitos
- Python 3.6+
- ANTLR4 runtime para Python
  ```bash
  pip install antlr4-python3-runtime
  ```

### Ejecución
```bash
cd Punto2_ANTLR
python main.py
```

### Salida esperada
```
=== ANALIZADOR SINTÁCTICO CRUD ===

Entrada:
    create(usuarios, {"nombre": "Brayan", "id": 101});
    read(usuarios, {"id": 101});
    update(usuarios, {"id": 101}, {"nombre": "Brayan Moreno"});
    delete(usuarios, {"id": 101});

RESULTADO:
  Estado: EXITOSO
  Total instrucciones: 4
  Operaciones encontradas: CREATE, READ, UPDATE, DELETE

¡Prueba exitosa! El lenguaje reconoció todas las operaciones CRUD.
```

### Nota
Los archivos `CRUDLexer.py`, `CRUDParser.py` y `CRUDListener.py` fueron generados con:
```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 CRUD.g4
```

---

## Punto 3 – Demostración LL(1)

**Archivos:** `Punto3_Demostracion_LL1/`

### Gramática analizada
```
S → A a A b
S → B b B a
A → ε
B → ε
```

### Ejecución
```bash
cd Punto3_Demostracion_LL1
python demostracion_ll1.py
```

### Salida esperada
El script calcula:
- Conjuntos PRIMEROS
- Conjuntos SIGUIENTES
- Conjuntos de PREDICCIÓN
- Verifica la condición LL(1)

**Conclusión:** La gramática ES LL(1) porque los conjuntos de predicción de las producciones del mismo no terminal son disjuntos:
- `PRED(S → A a A b) = {a}`
- `PRED(S → B b B a) = {b}`
- `PRED(A → ε) = {a, b}`
- `PRED(B → ε) = {a, b}`

---

## Punto 4 – Comparación CYK vs LL(1)

**Archivos:** `Punto4_Comparacion_CYK_LL1/`

### Requisitos
- Python 3.6+
- Matplotlib (para la gráfica)
  ```bash
  pip install matplotlib
  ```

### Ejecución
```bash
cd Punto4_Comparacion_CYK_LL1
python comparar.py
```

### Resultados
- Se generan expresiones aritméticas de complejidad creciente.
- Se miden los tiempos de ejecución de ambos algoritmos.
- Se genera la gráfica `comparacion_parsers.png` mostrando la diferencia de rendimiento.

### Tabla de resultados (ejemplo)

| Tokens | CYK (s) | LL1 (s) | Aceleración |
|--------|---------|---------|-------------|
| 3      | 0.000026| 0.000010| 2.6x        |
| 7      | 0.000096| 0.000010| 9.6x        |
| 15     | 0.000677| 0.000014| 48.4x       |
| 31     | 0.006295| 0.000033| 190.8x      |
| 63     | 0.048481| 0.000049| 985.1x      |

### Conclusión
- **LL(1):** Tiempo lineal O(n), muy rápido (microsegundos por expresión).
- **CYK:** Tiempo cúbico O(n³), se vuelve extremadamente lento para entradas largas (ej. n=63 → ~1000 veces más lento).
- Para una calculadora en tiempo real, LL(1) es claramente superior.

---

## Punto 5 – Calculadora Booleana en YACC

**Archivos:** `Punto5_Calculadora_Booleana/`

### Requisitos
- YACC (o Bison)
- GCC

### Compilación
```bash
cd Punto5_Calculadora_Booleana
yacc -d boolean_calc.y
gcc -o boolean_calc y.tab.c
```

### Ejecución
```bash
./boolean_calc
```

### Ejemplo de uso
```
true & false
0
true | false
1
!true
0
(true & false) | true
1
false | (true & true)
1
true
1
false
0
```

### Operadores soportados
- `&` = and (conjunción)
- `|` = or (disyunción)
- `!` = not (negación)
- Paréntesis `(` y `)`

### Para salir
Presione `Ctrl+D` (fin de archivo)

### Desempeño del analizador
- El analizador generado por YACC (LALR(1)) es **lineal O(n)**.
- Responde instantáneamente para expresiones típicas de una calculadora.
- Las directivas `%left`, `%right` resuelven conflictos de precedencia y asociatividad eficientemente.

---
