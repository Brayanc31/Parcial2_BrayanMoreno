import sys
from antlr4 import *
from CRUDLexer import CRUDLexer
from CRUDParser import CRUDParser

class CRUDListener(ParseTreeListener):
    
    def __init__(self):
        self.operations = []
    
    def enterCreate_op(self, ctx):
        self.operations.append("CREATE")
    
    def enterRead_op(self, ctx):
        self.operations.append("READ")
    
    def enterUpdate_op(self, ctx):
        self.operations.append("UPDATE")
    
    def enterDelete_op(self, ctx):
        self.operations.append("DELETE")

def main():
    input_text = """
    create(usuarios, {"nombre": "Brayan", "id": 101});
    read(usuarios, {"id": 101});
    update(usuarios, {"id": 101}, {"nombre": "Brayan Moreno"});
    delete(usuarios, {"id": 101});
    """
    
    print("ANALIZADOR SINTÁCTICO CRUD")
    print("\nEntrada:")
    print(input_text)
    
    input_stream = InputStream(input_text)
    lexer = CRUDLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CRUDParser(token_stream)
    
    # Ejecutar análisis
    tree = parser.programa()
    
    num_errors = parser.getNumberOfSyntaxErrors()
    
    if num_errors == 0:
        # Recorrer el árbol con un listener para recolectar operaciones
        listener = CRUDListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        print("\nRESULTADO:")
        print(f"  Estado: EXITOSO")
        print(f"  Total instrucciones: {len(listener.operations)}")
        print(f"  Operaciones encontradas: {', '.join(listener.operations)}")
        print("\n¡Prueba exitosa! El lenguaje reconoció todas las operaciones CRUD.")
    else:
        print(f"\nRESULTADO:")
        print(f"  Estado: FALLIDO")
        print(f"  Errores sintácticos: {num_errors}")
        print("\nRevisa la sintaxis de las instrucciones.")

if __name__ == '__main__':
    main()
