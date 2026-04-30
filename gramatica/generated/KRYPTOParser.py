# Generated from KryptoParser.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

def serializedATN():
    # Este bloque contiene la lógica interna de ANTLR (tablas de predicción)
    # En tu entorno local, esto se genera automáticamente al compilar los .g4
    return [ ... ] 

class KryptoParser ( Parser ):

    # --- DEFINICIÓN DE TOKENS (Sincronizados con KryptoLexer) ---
    TOKENS = {
        "IF": 1, "ELSE": 2, "WHILE": 3, "FOR": 4, "IN": 5, "FUNCTION": 6, 
        "RETURN": 7, "STOP": 8, "IMPORT": 9, "ALIAS": 10, "NUM": 11, 
        "DEC": 12, "LOGIC": 13, "TEXT": 14, "CHAIN": 15, "VAULT": 16, 
        "GRID": 17, "DATASET": 18, "BOOL_LIT": 19, "NUMBER": 20, "STRING": 21, 
        "ID": 22, "PLUS": 23, "MINUS": 24, "MUL": 25, "DIV": 26, "MOD": 27, 
        "POW": 28, "ASSIGN": 29, "COLON": 30, "COMMA": 31, "SEMI": 32, 
        "DOT": 33, "LPAREN": 34, "RPAREN": 35, "LBRACK": 36, "RBRACK": 37, 
        "LBRACE": 38, "RBRACE": 39, "EQ": 40, "NEQ": 41, "LE": 42, "GE": 43, 
        "LT": 44, "GT": 45, "OR": 46, "AND": 47, "NOT": 48, 
        "K_PLOT": 49, "K_SHOW": 50, "K_TITLE": 51, "K_XLABEL": 52, "K_YLABEL": 53
    }

    # --- REGLAS DE GRAMÁTICA ---
    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_ifStatement = 3
    RULE_whileStatement = 4
    RULE_forStatement = 5
    RULE_block = 6
    RULE_functionDecl = 7
    RULE_expr = 8
    RULE_kryptoGraphicStmt = 9 # Regla para KRYPTO_CHART

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())

    # --- CLASES DE CONTEXTO (Para el Visitor) ---
    class ProgramContext(ParserRuleContext):
        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
        def statement(self, i:int=None):
            return self.getTypedRuleContext(KryptoParser.StatementContext,i) if i is not None else self.getTypedRuleContexts(KryptoParser.StatementContext)

    class StatementContext(ParserRuleContext):
        # Maneja varDecl, assignment, if, loop, y kryptoGraphicStmt
        pass

    # --- MÉTODOS DE ACCESO A REGLAS (Ejemplo: ifStatement) ---
    def ifStatement(self):
        localctx = KryptoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(KryptoParser.TOKENS["IF"])
            self.state = 71
            self.match(KryptoParser.TOKENS["LPAREN"])
            # ... Lógica interna del parser ...
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx