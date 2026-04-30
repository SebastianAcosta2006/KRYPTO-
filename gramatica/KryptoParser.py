# Generated from gramatica/KryptoParser.g4 by ANTLR 4.13.1
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
        4,1,57,210,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,3,2,66,8,2,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,81,8,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,5,8,105,8,8,10,8,12,8,108,9,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,
        116,8,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,125,8,10,10,10,12,10,
        128,9,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,145,8,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,5,12,159,8,12,10,12,12,12,162,9,12,
        1,13,1,13,1,13,3,13,167,8,13,1,13,1,13,1,14,1,14,1,14,5,14,174,8,
        14,10,14,12,14,177,9,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,208,8,16,1,16,0,1,24,
        17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,6,1,0,11,18,1,
        0,25,27,1,0,23,24,1,0,40,45,1,0,46,47,1,0,19,21,221,0,37,1,0,0,0,
        2,59,1,0,0,0,4,61,1,0,0,0,6,67,1,0,0,0,8,69,1,0,0,0,10,73,1,0,0,
        0,12,84,1,0,0,0,14,91,1,0,0,0,16,102,1,0,0,0,18,111,1,0,0,0,20,121,
        1,0,0,0,22,129,1,0,0,0,24,144,1,0,0,0,26,163,1,0,0,0,28,170,1,0,
        0,0,30,178,1,0,0,0,32,207,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,
        39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,
        0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,3,4,2,0,43,44,5,32,0,0,44,60,
        1,0,0,0,45,46,3,8,4,0,46,47,5,32,0,0,47,60,1,0,0,0,48,60,3,10,5,
        0,49,60,3,12,6,0,50,60,3,14,7,0,51,60,3,18,9,0,52,53,3,22,11,0,53,
        54,5,32,0,0,54,60,1,0,0,0,55,60,3,32,16,0,56,57,3,24,12,0,57,58,
        5,32,0,0,58,60,1,0,0,0,59,42,1,0,0,0,59,45,1,0,0,0,59,48,1,0,0,0,
        59,49,1,0,0,0,59,50,1,0,0,0,59,51,1,0,0,0,59,52,1,0,0,0,59,55,1,
        0,0,0,59,56,1,0,0,0,60,3,1,0,0,0,61,62,3,6,3,0,62,65,5,22,0,0,63,
        64,5,29,0,0,64,66,3,24,12,0,65,63,1,0,0,0,65,66,1,0,0,0,66,5,1,0,
        0,0,67,68,7,0,0,0,68,7,1,0,0,0,69,70,5,22,0,0,70,71,5,29,0,0,71,
        72,3,24,12,0,72,9,1,0,0,0,73,74,5,1,0,0,74,75,5,34,0,0,75,76,3,24,
        12,0,76,77,5,35,0,0,77,80,3,16,8,0,78,79,5,2,0,0,79,81,3,16,8,0,
        80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,57,0,0,83,11,1,
        0,0,0,84,85,5,3,0,0,85,86,5,34,0,0,86,87,3,24,12,0,87,88,5,35,0,
        0,88,89,3,16,8,0,89,90,5,57,0,0,90,13,1,0,0,0,91,92,5,4,0,0,92,93,
        5,34,0,0,93,94,3,8,4,0,94,95,5,32,0,0,95,96,3,24,12,0,96,97,5,32,
        0,0,97,98,3,8,4,0,98,99,5,35,0,0,99,100,3,16,8,0,100,101,5,57,0,
        0,101,15,1,0,0,0,102,106,5,38,0,0,103,105,3,2,1,0,104,103,1,0,0,
        0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,
        0,108,106,1,0,0,0,109,110,5,39,0,0,110,17,1,0,0,0,111,112,5,6,0,
        0,112,113,5,22,0,0,113,115,5,34,0,0,114,116,3,20,10,0,115,114,1,
        0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,5,35,0,0,118,119,3,
        16,8,0,119,120,5,57,0,0,120,19,1,0,0,0,121,126,5,22,0,0,122,123,
        5,31,0,0,123,125,5,22,0,0,124,122,1,0,0,0,125,128,1,0,0,0,126,124,
        1,0,0,0,126,127,1,0,0,0,127,21,1,0,0,0,128,126,1,0,0,0,129,130,5,
        7,0,0,130,131,3,24,12,0,131,23,1,0,0,0,132,133,6,12,-1,0,133,134,
        7,1,0,0,134,145,3,24,12,9,135,136,5,48,0,0,136,145,3,24,12,5,137,
        138,5,34,0,0,138,139,3,24,12,0,139,140,5,35,0,0,140,145,1,0,0,0,
        141,145,3,26,13,0,142,145,3,30,15,0,143,145,5,22,0,0,144,132,1,0,
        0,0,144,135,1,0,0,0,144,137,1,0,0,0,144,141,1,0,0,0,144,142,1,0,
        0,0,144,143,1,0,0,0,145,160,1,0,0,0,146,147,10,10,0,0,147,148,5,
        28,0,0,148,159,3,24,12,11,149,150,10,8,0,0,150,151,7,2,0,0,151,159,
        3,24,12,9,152,153,10,7,0,0,153,154,7,3,0,0,154,159,3,24,12,8,155,
        156,10,6,0,0,156,157,7,4,0,0,157,159,3,24,12,7,158,146,1,0,0,0,158,
        149,1,0,0,0,158,152,1,0,0,0,158,155,1,0,0,0,159,162,1,0,0,0,160,
        158,1,0,0,0,160,161,1,0,0,0,161,25,1,0,0,0,162,160,1,0,0,0,163,164,
        5,22,0,0,164,166,5,34,0,0,165,167,3,28,14,0,166,165,1,0,0,0,166,
        167,1,0,0,0,167,168,1,0,0,0,168,169,5,35,0,0,169,27,1,0,0,0,170,
        175,3,24,12,0,171,172,5,31,0,0,172,174,3,24,12,0,173,171,1,0,0,0,
        174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,29,1,0,0,0,177,
        175,1,0,0,0,178,179,7,5,0,0,179,31,1,0,0,0,180,181,5,49,0,0,181,
        182,5,34,0,0,182,183,3,24,12,0,183,184,5,31,0,0,184,185,3,24,12,
        0,185,186,5,35,0,0,186,187,5,32,0,0,187,208,1,0,0,0,188,189,5,51,
        0,0,189,190,5,34,0,0,190,191,5,21,0,0,191,192,5,35,0,0,192,208,5,
        32,0,0,193,194,5,52,0,0,194,195,5,34,0,0,195,196,5,21,0,0,196,197,
        5,35,0,0,197,208,5,32,0,0,198,199,5,53,0,0,199,200,5,34,0,0,200,
        201,5,21,0,0,201,202,5,35,0,0,202,208,5,32,0,0,203,204,5,50,0,0,
        204,205,5,34,0,0,205,206,5,35,0,0,206,208,5,32,0,0,207,180,1,0,0,
        0,207,188,1,0,0,0,207,193,1,0,0,0,207,198,1,0,0,0,207,203,1,0,0,
        0,208,33,1,0,0,0,13,37,59,65,80,106,115,126,144,158,160,166,175,
        207
    ]

class KryptoParser ( Parser ):

    grammarFileName = "KryptoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'krif'", "'krelse'", "'krloop'", "'krfor'", 
                     "'krin'", "'krfunc'", "'yield'", "'stop'", "'use'", 
                     "'alias'", "'num'", "'dec'", "'logic'", "'text'", "'chain'", 
                     "'vault'", "'grid'", "'dataset'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'='", "':'", "','", "';'", "'.'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'", "'||'", "'&&'", "'!'", 
                     "'k_plot'", "'k_show'", "'k_title'", "'k_xlabel'", 
                     "'k_ylabel'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FOR", "IN", "FUNCTION", 
                      "RETURN", "END", "IMPORT", "AS", "INT", "FLOAT", "BOOL_T", 
                      "STRING_T", "LIST", "DICC", "MATRIX", "DATAFRAME", 
                      "BOOL_LIT", "NUMBER", "STRING", "ID", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "POW", "ASSIGN", "COLON", "COMMA", 
                      "SEMI", "DOT", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                      "LBRACE", "RBRACE", "EQ", "NEQ", "LE", "GE", "LT", 
                      "GT", "OR", "AND", "NOT", "PLOTVAG", "SHOWVAG", "TITLEVAG", 
                      "XLABELVAG", "YLABELVAG", "COMMENT", "BLOCK_COMMENT", 
                      "WS", "STOP" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_type = 3
    RULE_assignment = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_block = 8
    RULE_functionDecl = 9
    RULE_paramList = 10
    RULE_returnStmt = 11
    RULE_expr = 12
    RULE_functionCall = 13
    RULE_argList = 14
    RULE_literal = 15
    RULE_kryptoGraphicStmt = 16

    ruleNames =  [ "program", "statement", "varDecl", "type", "assignment", 
                   "ifStatement", "whileStatement", "forStatement", "block", 
                   "functionDecl", "paramList", "returnStmt", "expr", "functionCall", 
                   "argList", "literal", "kryptoGraphicStmt" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FOR=4
    IN=5
    FUNCTION=6
    RETURN=7
    END=8
    IMPORT=9
    AS=10
    INT=11
    FLOAT=12
    BOOL_T=13
    STRING_T=14
    LIST=15
    DICC=16
    MATRIX=17
    DATAFRAME=18
    BOOL_LIT=19
    NUMBER=20
    STRING=21
    ID=22
    PLUS=23
    MINUS=24
    MUL=25
    DIV=26
    MOD=27
    POW=28
    ASSIGN=29
    COLON=30
    COMMA=31
    SEMI=32
    DOT=33
    LPAREN=34
    RPAREN=35
    LBRACK=36
    RBRACK=37
    LBRACE=38
    RBRACE=39
    EQ=40
    NEQ=41
    LE=42
    GE=43
    LT=44
    GT=45
    OR=46
    AND=47
    NOT=48
    PLOTVAG=49
    SHOWVAG=50
    TITLEVAG=51
    XLABELVAG=52
    YLABELVAG=53
    COMMENT=54
    BLOCK_COMMENT=55
    WS=56
    STOP=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KryptoParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.StatementContext)
            else:
                return self.getTypedRuleContext(KryptoParser.StatementContext,i)


        def getRuleIndex(self):
            return KryptoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = KryptoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17732940955908314) != 0):
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(KryptoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(KryptoParser.VarDeclContext,0)


        def SEMI(self):
            return self.getToken(KryptoParser.SEMI, 0)

        def assignment(self):
            return self.getTypedRuleContext(KryptoParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(KryptoParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(KryptoParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(KryptoParser.ForStatementContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(KryptoParser.FunctionDeclContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(KryptoParser.ReturnStmtContext,0)


        def kryptoGraphicStmt(self):
            return self.getTypedRuleContext(KryptoParser.KryptoGraphicStmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def getRuleIndex(self):
            return KryptoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = KryptoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.varDecl()
                self.state = 43
                self.match(KryptoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.assignment()
                self.state = 46
                self.match(KryptoParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.returnStmt()
                self.state = 53
                self.match(KryptoParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 55
                self.kryptoGraphicStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 56
                self.expr(0)
                self.state = 57
                self.match(KryptoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(KryptoParser.TypeContext,0)


        def ID(self):
            return self.getToken(KryptoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(KryptoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def getRuleIndex(self):
            return KryptoParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = KryptoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.type_()
            self.state = 62
            self.match(KryptoParser.ID)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 63
                self.match(KryptoParser.ASSIGN)
                self.state = 64
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(KryptoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(KryptoParser.FLOAT, 0)

        def BOOL_T(self):
            return self.getToken(KryptoParser.BOOL_T, 0)

        def STRING_T(self):
            return self.getToken(KryptoParser.STRING_T, 0)

        def LIST(self):
            return self.getToken(KryptoParser.LIST, 0)

        def MATRIX(self):
            return self.getToken(KryptoParser.MATRIX, 0)

        def DICC(self):
            return self.getToken(KryptoParser.DICC, 0)

        def DATAFRAME(self):
            return self.getToken(KryptoParser.DATAFRAME, 0)

        def getRuleIndex(self):
            return KryptoParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = KryptoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 522240) != 0)):
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KryptoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(KryptoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def getRuleIndex(self):
            return KryptoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = KryptoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(KryptoParser.ID)
            self.state = 70
            self.match(KryptoParser.ASSIGN)
            self.state = 71
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(KryptoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(KryptoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(KryptoParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.BlockContext)
            else:
                return self.getTypedRuleContext(KryptoParser.BlockContext,i)


        def STOP(self):
            return self.getToken(KryptoParser.STOP, 0)

        def ELSE(self):
            return self.getToken(KryptoParser.ELSE, 0)

        def getRuleIndex(self):
            return KryptoParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = KryptoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(KryptoParser.IF)
            self.state = 74
            self.match(KryptoParser.LPAREN)
            self.state = 75
            self.expr(0)
            self.state = 76
            self.match(KryptoParser.RPAREN)
            self.state = 77
            self.block()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 78
                self.match(KryptoParser.ELSE)
                self.state = 79
                self.block()


            self.state = 82
            self.match(KryptoParser.STOP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(KryptoParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(KryptoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(KryptoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KryptoParser.BlockContext,0)


        def STOP(self):
            return self.getToken(KryptoParser.STOP, 0)

        def getRuleIndex(self):
            return KryptoParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = KryptoParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(KryptoParser.WHILE)
            self.state = 85
            self.match(KryptoParser.LPAREN)
            self.state = 86
            self.expr(0)
            self.state = 87
            self.match(KryptoParser.RPAREN)
            self.state = 88
            self.block()
            self.state = 89
            self.match(KryptoParser.STOP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(KryptoParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(KryptoParser.LPAREN, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(KryptoParser.AssignmentContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(KryptoParser.SEMI)
            else:
                return self.getToken(KryptoParser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(KryptoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KryptoParser.BlockContext,0)


        def STOP(self):
            return self.getToken(KryptoParser.STOP, 0)

        def getRuleIndex(self):
            return KryptoParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = KryptoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(KryptoParser.FOR)
            self.state = 92
            self.match(KryptoParser.LPAREN)
            self.state = 93
            self.assignment()
            self.state = 94
            self.match(KryptoParser.SEMI)
            self.state = 95
            self.expr(0)
            self.state = 96
            self.match(KryptoParser.SEMI)
            self.state = 97
            self.assignment()
            self.state = 98
            self.match(KryptoParser.RPAREN)
            self.state = 99
            self.block()
            self.state = 100
            self.match(KryptoParser.STOP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(KryptoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(KryptoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.StatementContext)
            else:
                return self.getTypedRuleContext(KryptoParser.StatementContext,i)


        def getRuleIndex(self):
            return KryptoParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = KryptoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(KryptoParser.LBRACE)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17732940955908314) != 0):
                self.state = 103
                self.statement()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(KryptoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(KryptoParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(KryptoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(KryptoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(KryptoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KryptoParser.BlockContext,0)


        def STOP(self):
            return self.getToken(KryptoParser.STOP, 0)

        def paramList(self):
            return self.getTypedRuleContext(KryptoParser.ParamListContext,0)


        def getRuleIndex(self):
            return KryptoParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = KryptoParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(KryptoParser.FUNCTION)
            self.state = 112
            self.match(KryptoParser.ID)
            self.state = 113
            self.match(KryptoParser.LPAREN)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 114
                self.paramList()


            self.state = 117
            self.match(KryptoParser.RPAREN)
            self.state = 118
            self.block()
            self.state = 119
            self.match(KryptoParser.STOP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(KryptoParser.ID)
            else:
                return self.getToken(KryptoParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KryptoParser.COMMA)
            else:
                return self.getToken(KryptoParser.COMMA, i)

        def getRuleIndex(self):
            return KryptoParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = KryptoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(KryptoParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 122
                self.match(KryptoParser.COMMA)
                self.state = 123
                self.match(KryptoParser.ID)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(KryptoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def getRuleIndex(self):
            return KryptoParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = KryptoParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(KryptoParser.RETURN)
            self.state = 130
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KryptoParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OpNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(KryptoParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpNot" ):
                listener.enterOpNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpNot" ):
                listener.exitOpNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpNot" ):
                return visitor.visitOpNot(self)
            else:
                return visitor.visitChildren(self)


    class OpParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(KryptoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(KryptoParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpParens" ):
                listener.enterOpParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpParens" ):
                listener.exitOpParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpParens" ):
                return visitor.visitOpParens(self)
            else:
                return visitor.visitChildren(self)


    class OpLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(KryptoParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpLiteral" ):
                listener.enterOpLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpLiteral" ):
                listener.exitOpLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpLiteral" ):
                return visitor.visitOpLiteral(self)
            else:
                return visitor.visitChildren(self)


    class OpPowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.ExprContext)
            else:
                return self.getTypedRuleContext(KryptoParser.ExprContext,i)

        def POW(self):
            return self.getToken(KryptoParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpPow" ):
                listener.enterOpPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpPow" ):
                listener.exitOpPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpPow" ):
                return visitor.visitOpPow(self)
            else:
                return visitor.visitChildren(self)


    class OpAddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.ExprContext)
            else:
                return self.getTypedRuleContext(KryptoParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(KryptoParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(KryptoParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAddSub" ):
                listener.enterOpAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAddSub" ):
                listener.exitOpAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAddSub" ):
                return visitor.visitOpAddSub(self)
            else:
                return visitor.visitChildren(self)


    class OpLogicalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.ExprContext)
            else:
                return self.getTypedRuleContext(KryptoParser.ExprContext,i)

        def AND(self):
            return self.getToken(KryptoParser.AND, 0)
        def OR(self):
            return self.getToken(KryptoParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpLogical" ):
                listener.enterOpLogical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpLogical" ):
                listener.exitOpLogical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpLogical" ):
                return visitor.visitOpLogical(self)
            else:
                return visitor.visitChildren(self)


    class OpIdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(KryptoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpId" ):
                listener.enterOpId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpId" ):
                listener.exitOpId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpId" ):
                return visitor.visitOpId(self)
            else:
                return visitor.visitChildren(self)


    class OpMulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(KryptoParser.ExprContext,0)

        def MUL(self):
            return self.getToken(KryptoParser.MUL, 0)
        def DIV(self):
            return self.getToken(KryptoParser.DIV, 0)
        def MOD(self):
            return self.getToken(KryptoParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMulDiv" ):
                listener.enterOpMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMulDiv" ):
                listener.exitOpMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMulDiv" ):
                return visitor.visitOpMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class OpCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(KryptoParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpCall" ):
                listener.enterOpCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpCall" ):
                listener.exitOpCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpCall" ):
                return visitor.visitOpCall(self)
            else:
                return visitor.visitChildren(self)


    class OpCompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KryptoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.ExprContext)
            else:
                return self.getTypedRuleContext(KryptoParser.ExprContext,i)

        def EQ(self):
            return self.getToken(KryptoParser.EQ, 0)
        def NEQ(self):
            return self.getToken(KryptoParser.NEQ, 0)
        def LT(self):
            return self.getToken(KryptoParser.LT, 0)
        def GT(self):
            return self.getToken(KryptoParser.GT, 0)
        def LE(self):
            return self.getToken(KryptoParser.LE, 0)
        def GE(self):
            return self.getToken(KryptoParser.GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpCompare" ):
                listener.enterOpCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpCompare" ):
                listener.exitOpCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpCompare" ):
                return visitor.visitOpCompare(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KryptoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = KryptoParser.OpMulDivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 133
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 134
                self.expr(9)
                pass

            elif la_ == 2:
                localctx = KryptoParser.OpNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(KryptoParser.NOT)
                self.state = 136
                self.expr(5)
                pass

            elif la_ == 3:
                localctx = KryptoParser.OpParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(KryptoParser.LPAREN)
                self.state = 138
                self.expr(0)
                self.state = 139
                self.match(KryptoParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = KryptoParser.OpCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.functionCall()
                pass

            elif la_ == 5:
                localctx = KryptoParser.OpLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.literal()
                pass

            elif la_ == 6:
                localctx = KryptoParser.OpIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(KryptoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 158
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = KryptoParser.OpPowContext(self, KryptoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 146
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 147
                        self.match(KryptoParser.POW)
                        self.state = 148
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = KryptoParser.OpAddSubContext(self, KryptoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 149
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 150
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 151
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = KryptoParser.OpCompareContext(self, KryptoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 152
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 153
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69269232549888) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 154
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = KryptoParser.OpLogicalContext(self, KryptoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 155
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 156
                        _la = self._input.LA(1)
                        if not(_la==46 or _la==47):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 157
                        self.expr(7)
                        pass

             
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KryptoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(KryptoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(KryptoParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(KryptoParser.ArgListContext,0)


        def getRuleIndex(self):
            return KryptoParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = KryptoParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(KryptoParser.ID)
            self.state = 164
            self.match(KryptoParser.LPAREN)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 281492399325184) != 0):
                self.state = 165
                self.argList()


            self.state = 168
            self.match(KryptoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.ExprContext)
            else:
                return self.getTypedRuleContext(KryptoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KryptoParser.COMMA)
            else:
                return self.getToken(KryptoParser.COMMA, i)

        def getRuleIndex(self):
            return KryptoParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = KryptoParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.expr(0)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 171
                self.match(KryptoParser.COMMA)
                self.state = 172
                self.expr(0)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(KryptoParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(KryptoParser.STRING, 0)

        def BOOL_LIT(self):
            return self.getToken(KryptoParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return KryptoParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = KryptoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
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


    class KryptoGraphicStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOTVAG(self):
            return self.getToken(KryptoParser.PLOTVAG, 0)

        def LPAREN(self):
            return self.getToken(KryptoParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KryptoParser.ExprContext)
            else:
                return self.getTypedRuleContext(KryptoParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(KryptoParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(KryptoParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(KryptoParser.SEMI, 0)

        def TITLEVAG(self):
            return self.getToken(KryptoParser.TITLEVAG, 0)

        def STRING(self):
            return self.getToken(KryptoParser.STRING, 0)

        def XLABELVAG(self):
            return self.getToken(KryptoParser.XLABELVAG, 0)

        def YLABELVAG(self):
            return self.getToken(KryptoParser.YLABELVAG, 0)

        def SHOWVAG(self):
            return self.getToken(KryptoParser.SHOWVAG, 0)

        def getRuleIndex(self):
            return KryptoParser.RULE_kryptoGraphicStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKryptoGraphicStmt" ):
                listener.enterKryptoGraphicStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKryptoGraphicStmt" ):
                listener.exitKryptoGraphicStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKryptoGraphicStmt" ):
                return visitor.visitKryptoGraphicStmt(self)
            else:
                return visitor.visitChildren(self)




    def kryptoGraphicStmt(self):

        localctx = KryptoParser.KryptoGraphicStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_kryptoGraphicStmt)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(KryptoParser.PLOTVAG)
                self.state = 181
                self.match(KryptoParser.LPAREN)
                self.state = 182
                self.expr(0)
                self.state = 183
                self.match(KryptoParser.COMMA)
                self.state = 184
                self.expr(0)
                self.state = 185
                self.match(KryptoParser.RPAREN)
                self.state = 186
                self.match(KryptoParser.SEMI)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(KryptoParser.TITLEVAG)
                self.state = 189
                self.match(KryptoParser.LPAREN)
                self.state = 190
                self.match(KryptoParser.STRING)
                self.state = 191
                self.match(KryptoParser.RPAREN)
                self.state = 192
                self.match(KryptoParser.SEMI)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(KryptoParser.XLABELVAG)
                self.state = 194
                self.match(KryptoParser.LPAREN)
                self.state = 195
                self.match(KryptoParser.STRING)
                self.state = 196
                self.match(KryptoParser.RPAREN)
                self.state = 197
                self.match(KryptoParser.SEMI)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 198
                self.match(KryptoParser.YLABELVAG)
                self.state = 199
                self.match(KryptoParser.LPAREN)
                self.state = 200
                self.match(KryptoParser.STRING)
                self.state = 201
                self.match(KryptoParser.RPAREN)
                self.state = 202
                self.match(KryptoParser.SEMI)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 5)
                self.state = 203
                self.match(KryptoParser.SHOWVAG)
                self.state = 204
                self.match(KryptoParser.LPAREN)
                self.state = 205
                self.match(KryptoParser.RPAREN)
                self.state = 206
                self.match(KryptoParser.SEMI)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




