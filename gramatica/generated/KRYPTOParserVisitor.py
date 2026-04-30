# Generated from KryptoParser.g4 by ANTLR 4.13.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KryptoParser import KryptoParser
else:
    from KryptoParser import KryptoParser

class KryptoParserVisitor(ParseTreeVisitor):
    """
    Esta clase define el visitante para el árbol de sintaxis de Krypto.
    Cada método corresponde a una regla en KryptoParser.g4.
    """

    # --- NAVEGACIÓN PRINCIPAL ---
    def visitProgram(self, ctx:KryptoParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx:KryptoParser.StatementContext):
        return self.visitChildren(ctx)

    # --- VARIABLES Y TIPOS ---
    def visitVarDecl(self, ctx:KryptoParser.VarDeclContext):
        return self.visitChildren(ctx)

    def visitType(self, ctx:KryptoParser.TypeContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx:KryptoParser.AssignmentContext):
        return self.visitChildren(ctx)

    # --- ESTRUCTURAS DE CONTROL ---
    def visitIfStatement(self, ctx:KryptoParser.IfStatementContext):
        return self.visitChildren(ctx)

    def visitWhileStatement(self, ctx:KryptoParser.WhileStatementContext):
        return self.visitChildren(ctx)

    def visitForStatement(self, ctx:KryptoParser.ForStatementContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx:KryptoParser.BlockContext):
        return self.visitChildren(ctx)

    # --- FUNCIONES ---
    def visitFunctionDecl(self, ctx:KryptoParser.FunctionDeclContext):
        return self.visitChildren(ctx)

    def visitParamList(self, ctx:KryptoParser.ParamListContext):
        return self.visitChildren(ctx)

    def visitReturnStmt(self, ctx:KryptoParser.ReturnStmtContext):
        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx:KryptoParser.FunctionCallContext):
        return self.visitChildren(ctx)

    # --- EXPRESIONES Y OPERACIONES ---
    # Gracias a las etiquetas '#' en el Parser, podemos ser específicos:
    def visitOpPow(self, ctx:KryptoParser.OpPowContext):
        return self.visitChildren(ctx)

    def visitOpMulDiv(self, ctx:KryptoParser.OpMulDivContext):
        return self.visitChildren(ctx)

    def visitOpAddSub(self, ctx:KryptoParser.OpAddSubContext):
        return self.visitChildren(ctx)

    def visitOpCompare(self, ctx:KryptoParser.OpCompareContext):
        return self.visitChildren(ctx)

    def visitOpLogical(self, ctx:KryptoParser.OpLogicalContext):
        return self.visitChildren(ctx)

    def visitOpNot(self, ctx:KryptoParser.OpNotContext):
        return self.visitChildren(ctx)

    def visitOpParens(self, ctx:KryptoParser.OpParensContext):
        return self.visitChildren(ctx)

    def visitOpCall(self, ctx:KryptoParser.OpCallContext):
        return self.visitChildren(ctx)

    def visitOpLiteral(self, ctx:KryptoParser.OpLiteralContext):
        return self.visitChildren(ctx)

    def visitOpId(self, ctx:KryptoParser.OpIdContext):
        return self.visitChildren(ctx)

    # --- LITERALES ---
    def visitLiteral(self, ctx:KryptoParser.LiteralContext):
        return self.visitChildren(ctx)

    # --- MOTOR GRÁFICO (KRYPTO_CHART) ---
    def visitKryptoGraphicStmt(self, ctx:KryptoParser.KryptoGraphicStmtContext):
        """
        Este método es el encargado de capturar las llamadas a 
        k_plot, k_show, k_title, etc.
        """
        return self.visitChildren(ctx)