# Generated from KryptoParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .KryptoParser import KryptoParser
else:
    from KryptoParser import KryptoParser

# Esta clase define un listener completo para el árbol de sintaxis de Krypto.
class KryptoParserListener(ParseTreeListener):

    # Entrar a un árbol de análisis producido por KryptoParser#program.
    def enterProgram(self, ctx:KryptoParser.ProgramContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#program.
    def exitProgram(self, ctx:KryptoParser.ProgramContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#statement.
    def enterStatement(self, ctx:KryptoParser.StatementContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#statement.
    def exitStatement(self, ctx:KryptoParser.StatementContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#varDecl.
    def enterVarDecl(self, ctx:KryptoParser.VarDeclContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#varDecl.
    def exitVarDecl(self, ctx:KryptoParser.VarDeclContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#type.
    def enterType(self, ctx:KryptoParser.TypeContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#type.
    def exitType(self, ctx:KryptoParser.TypeContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#assignment.
    def enterAssignment(self, ctx:KryptoParser.AssignmentContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#assignment.
    def exitAssignment(self, ctx:KryptoParser.AssignmentContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#ifStatement.
    def enterIfStatement(self, ctx:KryptoParser.IfStatementContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#ifStatement.
    def exitIfStatement(self, ctx:KryptoParser.IfStatementContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#whileStatement.
    def enterWhileStatement(self, ctx:KryptoParser.WhileStatementContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#whileStatement.
    def exitWhileStatement(self, ctx:KryptoParser.WhileStatementContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#forStatement.
    def enterForStatement(self, ctx:KryptoParser.ForStatementContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#forStatement.
    def exitForStatement(self, ctx:KryptoParser.ForStatementContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#block.
    def enterBlock(self, ctx:KryptoParser.BlockContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#block.
    def exitBlock(self, ctx:KryptoParser.BlockContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#functionDecl.
    def enterFunctionDecl(self, ctx:KryptoParser.FunctionDeclContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#functionDecl.
    def exitFunctionDecl(self, ctx:KryptoParser.FunctionDeclContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#paramList.
    def enterParamList(self, ctx:KryptoParser.ParamListContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#paramList.
    def exitParamList(self, ctx:KryptoParser.ParamListContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#returnStmt.
    def enterReturnStmt(self, ctx:KryptoParser.ReturnStmtContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#returnStmt.
    def exitReturnStmt(self, ctx:KryptoParser.ReturnStmtContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#expr.
    def enterExpr(self, ctx:KryptoParser.ExprContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#expr.
    def exitExpr(self, ctx:KryptoParser.ExprContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#functionCall.
    def enterFunctionCall(self, ctx:KryptoParser.FunctionCallContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#functionCall.
    def exitFunctionCall(self, ctx:KryptoParser.FunctionCallContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#argList.
    def enterArgList(self, ctx:KryptoParser.ArgListContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#argList.
    def exitArgList(self, ctx:KryptoParser.ArgListContext):
        pass


    # Entrar a un árbol de análisis producido por KryptoParser#literal.
    def enterLiteral(self, ctx:KryptoParser.LiteralContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#literal.
    def exitLiteral(self, ctx:KryptoParser.LiteralContext):
        pass

    # --- NUEVOS MÉTODOS PARA KRYPTO_CHART ---
    
    # Entrar a un árbol de análisis producido por KryptoParser#kryptoGraphicStmt.
    def enterKryptoGraphicStmt(self, ctx:KryptoParser.KryptoGraphicStmtContext):
        pass

    # Salir de un árbol de análisis producido por KryptoParser#kryptoGraphicStmt.
    def exitKryptoGraphicStmt(self, ctx:KryptoParser.KryptoGraphicStmtContext):
        pass


del KryptoParser