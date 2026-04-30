from gramatica.KryptoParserVisitor import KryptoParserVisitor
from gramatica.KryptoParser import KryptoParser


class KryptoInterpreter(KryptoParserVisitor):

    def __init__(self):
        # Variables y funciones
        self.variables = {}
        self.functions = {}

    # -------- PROGRAMA --------
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # -------- STATEMENTS --------
    def visitStatement(self, ctx):
        if ctx.expr():
            result = self.visit(ctx.expr())

            if result is not None:
                print(result)

            return result

        return self.visitChildren(ctx)

    # -------- BLOQUES --------
    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # -------- VARIABLES --------
    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()

        value = self.visit(ctx.expr()) if ctx.expr() else None

        self.variables[name] = value

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()

        value = self.visit(ctx.expr())

        self.variables[name] = value

        return value

    # -------- IF --------
    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expr())

        if condition:
            self.visit(ctx.block(0))

        elif ctx.ELSE():
            self.visit(ctx.block(1))

    # -------- WHILE --------
    def visitWhileStatement(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.block())

    # -------- FOR --------
    def visitForStatement(self, ctx):

        self.visit(ctx.assignment(0))

        while self.visit(ctx.expr()):

            self.visit(ctx.block())

            self.visit(ctx.assignment(1))

    # -------- FUNCIONES --------
    def visitFunctionDecl(self, ctx):

        name = ctx.ID().getText()

        params = []

        if ctx.paramList():
            params = [p.getText() for p in ctx.paramList().ID()]

        self.functions[name] = {
            "params": params,
            "ctx": ctx
        }

    def visitFunctionCall(self, ctx):

        name = ctx.ID().getText()

        if name not in self.functions:
            raise Exception(
                f"RUNTIME ERROR: La función '{name}' no existe."
            )

        func = self.functions[name]

        params = func["params"]

        args = []

        if ctx.argList():
            args = [
                self.visit(e)
                for e in ctx.argList().expr()
            ]

        if len(args) != len(params):
            raise Exception(
                f"ARGUMENT ERROR: '{name}' requiere "
                f"{len(params)} parámetros."
            )

        local_vars = dict(zip(params, args))

        old_vars = self.variables.copy()

        self.variables.update(local_vars)

        result = None

        for stmt in func["ctx"].block().statement():

            if stmt.returnStmt():

                result = self.visit(
                    stmt.returnStmt().expr()
                )

                break

            self.visit(stmt)

        self.variables = old_vars

        return result

    # -------- EXPRESIONES --------
    def visitExpr(self, ctx):

        # Literales
        if ctx.literal():
            return self.visit(ctx.literal())

        # Funciones
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # Variables
        if ctx.ID():

            name = ctx.ID().getText()

            if name not in self.variables:
                raise Exception(
                    f"ACCESS ERROR: '{name}' no existe."
                )

            return self.variables[name]

        # Paréntesis
        if (
            ctx.getChildCount() == 3 and
            ctx.getChild(0).getText() == "("
        ):
            return self.visit(ctx.expr(0))

        # Operaciones binarias
        if ctx.getChildCount() == 3:

            left = self.visit(ctx.expr(0))

            right = self.visit(ctx.expr(1))

            op = ctx.getChild(1).getText()

            operations = {

                '+': lambda: left + right,
                '-': lambda: left - right,
                '*': lambda: left * right,
                '/': lambda: left / right,
                '%': lambda: left % right,
                '^': lambda: left ** right,

                '==': lambda: left == right,
                '!=': lambda: left != right,
                '<': lambda: left < right,
                '>': lambda: left > right,
                '<=': lambda: left <= right,
                '>=': lambda: left >= right,

                '&&': lambda: left and right,
                '||': lambda: left or right
            }

            if op in operations:
                return operations[op]()

        # NOT
        if (
            ctx.getChildCount() == 2 and
            ctx.getChild(0).getText() == "!"
        ):
            return not self.visit(ctx.expr(0))

    # -------- LITERALES --------
    def visitLiteral(self, ctx):

        if ctx.NUMBER():

            text = ctx.NUMBER().getText()

            if "." in text:
                return float(text)

            return int(text)

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        if ctx.BOOL_LIT():

            val = ctx.BOOL_LIT().getText()

            return True if val == "sisas" else False
