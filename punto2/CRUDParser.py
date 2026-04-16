# Generated from CRUD.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,37,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,7,71,8,7,1,7,1,7,
        1,8,1,8,1,8,5,8,78,8,8,10,8,12,8,81,9,8,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,3,10,91,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,
        1,2,0,1,1,17,17,90,0,23,1,0,0,0,2,29,1,0,0,0,4,36,1,0,0,0,6,38,1,
        0,0,0,8,45,1,0,0,0,10,52,1,0,0,0,12,61,1,0,0,0,14,68,1,0,0,0,16,
        74,1,0,0,0,18,82,1,0,0,0,20,90,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,
        0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,
        5,0,0,1,28,1,1,0,0,0,29,30,3,4,2,0,30,31,7,0,0,0,31,3,1,0,0,0,32,
        37,3,6,3,0,33,37,3,8,4,0,34,37,3,10,5,0,35,37,3,12,6,0,36,32,1,0,
        0,0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,5,1,0,0,0,38,39,
        5,8,0,0,39,40,5,2,0,0,40,41,5,13,0,0,41,42,5,3,0,0,42,43,3,14,7,
        0,43,44,5,4,0,0,44,7,1,0,0,0,45,46,5,9,0,0,46,47,5,2,0,0,47,48,5,
        13,0,0,48,49,5,3,0,0,49,50,3,14,7,0,50,51,5,4,0,0,51,9,1,0,0,0,52,
        53,5,10,0,0,53,54,5,2,0,0,54,55,5,13,0,0,55,56,5,3,0,0,56,57,3,14,
        7,0,57,58,5,3,0,0,58,59,3,14,7,0,59,60,5,4,0,0,60,11,1,0,0,0,61,
        62,5,11,0,0,62,63,5,2,0,0,63,64,5,13,0,0,64,65,5,3,0,0,65,66,3,14,
        7,0,66,67,5,4,0,0,67,13,1,0,0,0,68,70,5,5,0,0,69,71,3,16,8,0,70,
        69,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,6,0,0,73,15,1,0,0,
        0,74,79,3,18,9,0,75,76,5,3,0,0,76,78,3,18,9,0,77,75,1,0,0,0,78,81,
        1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,17,1,0,0,0,81,79,1,0,0,0,
        82,83,5,14,0,0,83,84,5,7,0,0,84,85,3,20,10,0,85,19,1,0,0,0,86,91,
        5,14,0,0,87,91,5,15,0,0,88,91,5,12,0,0,89,91,3,14,7,0,90,86,1,0,
        0,0,90,87,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,21,1,0,0,0,5,25,
        36,70,79,90
    ]

class CRUDParser ( Parser ):

    grammarFileName = "CRUD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'{'", "'}'", 
                     "':'", "'create'", "'read'", "'update'", "'delete'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CREATE", "READ", "UPDATE", "DELETE", "BOOLEAN", "ID", 
                      "STRING", "NUMBER", "WS", "NL" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_operacion = 2
    RULE_create_op = 3
    RULE_read_op = 4
    RULE_update_op = 5
    RULE_delete_op = 6
    RULE_diccionario = 7
    RULE_pares = 8
    RULE_par = 9
    RULE_valor = 10

    ruleNames =  [ "programa", "instruccion", "operacion", "create_op", 
                   "read_op", "update_op", "delete_op", "diccionario", "pares", 
                   "par", "valor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    CREATE=8
    READ=9
    UPDATE=10
    DELETE=11
    BOOLEAN=12
    ID=13
    STRING=14
    NUMBER=15
    WS=16
    NL=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CRUDParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CRUDParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(CRUDParser.InstruccionContext,i)


        def getRuleIndex(self):
            return CRUDParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = CRUDParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.instruccion()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                    break

            self.state = 27
            self.match(CRUDParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacion(self):
            return self.getTypedRuleContext(CRUDParser.OperacionContext,0)


        def NL(self):
            return self.getToken(CRUDParser.NL, 0)

        def getRuleIndex(self):
            return CRUDParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = CRUDParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.operacion()
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==1 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_op(self):
            return self.getTypedRuleContext(CRUDParser.Create_opContext,0)


        def read_op(self):
            return self.getTypedRuleContext(CRUDParser.Read_opContext,0)


        def update_op(self):
            return self.getTypedRuleContext(CRUDParser.Update_opContext,0)


        def delete_op(self):
            return self.getTypedRuleContext(CRUDParser.Delete_opContext,0)


        def getRuleIndex(self):
            return CRUDParser.RULE_operacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion" ):
                listener.enterOperacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion" ):
                listener.exitOperacion(self)




    def operacion(self):

        localctx = CRUDParser.OperacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operacion)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.create_op()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.read_op()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.update_op()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.delete_op()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(CRUDParser.CREATE, 0)

        def ID(self):
            return self.getToken(CRUDParser.ID, 0)

        def diccionario(self):
            return self.getTypedRuleContext(CRUDParser.DiccionarioContext,0)


        def getRuleIndex(self):
            return CRUDParser.RULE_create_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_op" ):
                listener.enterCreate_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_op" ):
                listener.exitCreate_op(self)




    def create_op(self):

        localctx = CRUDParser.Create_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_create_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CRUDParser.CREATE)
            self.state = 39
            self.match(CRUDParser.T__1)
            self.state = 40
            self.match(CRUDParser.ID)
            self.state = 41
            self.match(CRUDParser.T__2)
            self.state = 42
            self.diccionario()
            self.state = 43
            self.match(CRUDParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(CRUDParser.READ, 0)

        def ID(self):
            return self.getToken(CRUDParser.ID, 0)

        def diccionario(self):
            return self.getTypedRuleContext(CRUDParser.DiccionarioContext,0)


        def getRuleIndex(self):
            return CRUDParser.RULE_read_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_op" ):
                listener.enterRead_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_op" ):
                listener.exitRead_op(self)




    def read_op(self):

        localctx = CRUDParser.Read_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_read_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(CRUDParser.READ)
            self.state = 46
            self.match(CRUDParser.T__1)
            self.state = 47
            self.match(CRUDParser.ID)
            self.state = 48
            self.match(CRUDParser.T__2)
            self.state = 49
            self.diccionario()
            self.state = 50
            self.match(CRUDParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.filtro = None # DiccionarioContext
            self.datos = None # DiccionarioContext

        def UPDATE(self):
            return self.getToken(CRUDParser.UPDATE, 0)

        def ID(self):
            return self.getToken(CRUDParser.ID, 0)

        def diccionario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CRUDParser.DiccionarioContext)
            else:
                return self.getTypedRuleContext(CRUDParser.DiccionarioContext,i)


        def getRuleIndex(self):
            return CRUDParser.RULE_update_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate_op" ):
                listener.enterUpdate_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate_op" ):
                listener.exitUpdate_op(self)




    def update_op(self):

        localctx = CRUDParser.Update_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_update_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CRUDParser.UPDATE)
            self.state = 53
            self.match(CRUDParser.T__1)
            self.state = 54
            self.match(CRUDParser.ID)
            self.state = 55
            self.match(CRUDParser.T__2)
            self.state = 56
            localctx.filtro = self.diccionario()
            self.state = 57
            self.match(CRUDParser.T__2)
            self.state = 58
            localctx.datos = self.diccionario()
            self.state = 59
            self.match(CRUDParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delete_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(CRUDParser.DELETE, 0)

        def ID(self):
            return self.getToken(CRUDParser.ID, 0)

        def diccionario(self):
            return self.getTypedRuleContext(CRUDParser.DiccionarioContext,0)


        def getRuleIndex(self):
            return CRUDParser.RULE_delete_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_op" ):
                listener.enterDelete_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_op" ):
                listener.exitDelete_op(self)




    def delete_op(self):

        localctx = CRUDParser.Delete_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_delete_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(CRUDParser.DELETE)
            self.state = 62
            self.match(CRUDParser.T__1)
            self.state = 63
            self.match(CRUDParser.ID)
            self.state = 64
            self.match(CRUDParser.T__2)
            self.state = 65
            self.diccionario()
            self.state = 66
            self.match(CRUDParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiccionarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pares(self):
            return self.getTypedRuleContext(CRUDParser.ParesContext,0)


        def getRuleIndex(self):
            return CRUDParser.RULE_diccionario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiccionario" ):
                listener.enterDiccionario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiccionario" ):
                listener.exitDiccionario(self)




    def diccionario(self):

        localctx = CRUDParser.DiccionarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_diccionario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(CRUDParser.T__4)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 69
                self.pares()


            self.state = 72
            self.match(CRUDParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def par(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CRUDParser.ParContext)
            else:
                return self.getTypedRuleContext(CRUDParser.ParContext,i)


        def getRuleIndex(self):
            return CRUDParser.RULE_pares

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPares" ):
                listener.enterPares(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPares" ):
                listener.exitPares(self)




    def pares(self):

        localctx = CRUDParser.ParesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pares)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.par()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 75
                self.match(CRUDParser.T__2)
                self.state = 76
                self.par()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CRUDParser.STRING, 0)

        def valor(self):
            return self.getTypedRuleContext(CRUDParser.ValorContext,0)


        def getRuleIndex(self):
            return CRUDParser.RULE_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)




    def par(self):

        localctx = CRUDParser.ParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(CRUDParser.STRING)
            self.state = 83
            self.match(CRUDParser.T__6)
            self.state = 84
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CRUDParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(CRUDParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(CRUDParser.BOOLEAN, 0)

        def diccionario(self):
            return self.getTypedRuleContext(CRUDParser.DiccionarioContext,0)


        def getRuleIndex(self):
            return CRUDParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = CRUDParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_valor)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(CRUDParser.STRING)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(CRUDParser.NUMBER)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(CRUDParser.BOOLEAN)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.diccionario()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





