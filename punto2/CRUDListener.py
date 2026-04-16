# Generated from CRUD.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CRUDParser import CRUDParser
else:
    from CRUDParser import CRUDParser

# This class defines a complete listener for a parse tree produced by CRUDParser.
class CRUDListener(ParseTreeListener):

    # Enter a parse tree produced by CRUDParser#programa.
    def enterPrograma(self, ctx:CRUDParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CRUDParser#programa.
    def exitPrograma(self, ctx:CRUDParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CRUDParser#instruccion.
    def enterInstruccion(self, ctx:CRUDParser.InstruccionContext):
        pass

    # Exit a parse tree produced by CRUDParser#instruccion.
    def exitInstruccion(self, ctx:CRUDParser.InstruccionContext):
        pass


    # Enter a parse tree produced by CRUDParser#operacion.
    def enterOperacion(self, ctx:CRUDParser.OperacionContext):
        pass

    # Exit a parse tree produced by CRUDParser#operacion.
    def exitOperacion(self, ctx:CRUDParser.OperacionContext):
        pass


    # Enter a parse tree produced by CRUDParser#create_op.
    def enterCreate_op(self, ctx:CRUDParser.Create_opContext):
        pass

    # Exit a parse tree produced by CRUDParser#create_op.
    def exitCreate_op(self, ctx:CRUDParser.Create_opContext):
        pass


    # Enter a parse tree produced by CRUDParser#read_op.
    def enterRead_op(self, ctx:CRUDParser.Read_opContext):
        pass

    # Exit a parse tree produced by CRUDParser#read_op.
    def exitRead_op(self, ctx:CRUDParser.Read_opContext):
        pass


    # Enter a parse tree produced by CRUDParser#update_op.
    def enterUpdate_op(self, ctx:CRUDParser.Update_opContext):
        pass

    # Exit a parse tree produced by CRUDParser#update_op.
    def exitUpdate_op(self, ctx:CRUDParser.Update_opContext):
        pass


    # Enter a parse tree produced by CRUDParser#delete_op.
    def enterDelete_op(self, ctx:CRUDParser.Delete_opContext):
        pass

    # Exit a parse tree produced by CRUDParser#delete_op.
    def exitDelete_op(self, ctx:CRUDParser.Delete_opContext):
        pass


    # Enter a parse tree produced by CRUDParser#diccionario.
    def enterDiccionario(self, ctx:CRUDParser.DiccionarioContext):
        pass

    # Exit a parse tree produced by CRUDParser#diccionario.
    def exitDiccionario(self, ctx:CRUDParser.DiccionarioContext):
        pass


    # Enter a parse tree produced by CRUDParser#pares.
    def enterPares(self, ctx:CRUDParser.ParesContext):
        pass

    # Exit a parse tree produced by CRUDParser#pares.
    def exitPares(self, ctx:CRUDParser.ParesContext):
        pass


    # Enter a parse tree produced by CRUDParser#par.
    def enterPar(self, ctx:CRUDParser.ParContext):
        pass

    # Exit a parse tree produced by CRUDParser#par.
    def exitPar(self, ctx:CRUDParser.ParContext):
        pass


    # Enter a parse tree produced by CRUDParser#valor.
    def enterValor(self, ctx:CRUDParser.ValorContext):
        pass

    # Exit a parse tree produced by CRUDParser#valor.
    def exitValor(self, ctx:CRUDParser.ValorContext):
        pass



del CRUDParser