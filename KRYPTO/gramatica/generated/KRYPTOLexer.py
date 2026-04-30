# Generated from KryptoLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

class KryptoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN()) # (Omitido el array gigante por brevedad, se genera al compilar)

    # --- DEFINICIÓN DE TOKENS ACTUALIZADA ---
    IF = 1
    ELSE = 2
    WHILE = 3
    FOR = 4
    IN = 5
    FUNCTION = 6
    RETURN = 7
    STOP = 8      # Antes END
    IMPORT = 9
    AS = 10
    INT = 11
    FLOAT = 12
    BOOL_T = 13
    STRING_T = 14
    LIST = 15
    DICC = 16
    MATRIX = 17
    DATAFRAME = 18
    BOOL_LIT = 19
    NUMBER = 20
    STRING = 21
    ID = 22
    # ... (Resto de tokens: PLUS, MINUS, etc.)

    # --- NUEVOS LITERALES DE KRYPTO ---
    literalNames = [ "<INVALID>",
            "'krif'", "'krelse'", "'krloop'", "'krfor'", "'krin'", 
            "'krfunc'", "'yield'", "'stop'", "'use'", "'alias'", 
            "'num'", "'dec'", "'logic'", "'text'", "'chain'", 
            "'vault'", "'grid'", "'dataset'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'^'", "'='", "':'", "','", "';'", "'.'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'=='", "'!='", "'<='", 
            "'>='", "'<'", "'>'", "'||'", "'&&'", "'!'", 
            "'k_plot'", "'k_show'", "'k_title'", "'k_xlabel'", "'k_ylabel'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "WHILE", "FOR", "IN", "FUNCTION", "RETURN", "STOP", 
            "IMPORT", "AS", "INT", "FLOAT", "BOOL_T", "STRING_T", "LIST", 
            "DICC", "MATRIX", "DATAFRAME", "BOOL_LIT", "NUMBER", "STRING", 
            "ID", "PLUS", "MINUS", "MUL", "DIV", "MOD", "POW", "ASSIGN", 
            "COLON", "COMMA", "SEMI", "DOT", "LPAREN", "RPAREN", "LBRACK", 
            "RBRACK", "LBRACE", "RBRACE", "EQ", "NEQ", "LE", "GE", "LT", 
            "GT", "OR", "AND", "NOT", "PLOTVAG", "SHOWVAG", "TITLEVAG", 
            "XLABELVAG", "YLABELVAG", "COMMENT", "WS" ]

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())