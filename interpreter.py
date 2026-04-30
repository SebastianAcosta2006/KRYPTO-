from gramatica.KryptoParserVisitor import KryptoParserVisitor
from gramatica.KryptoParser import KryptoParser
from librerias.KRYPTOMATH import KRYPTOMATH  # Tu librería personalizada

class KryptoInterpreter(KryptoParserVisitor):

    def __init__(self):
        # Memoria global
        self.variables = {}
        self.functions = {}
        # Pila de ámbitos para soportar recursión profunda
        self.scope_stack = [{}] 

    # --- UTILIDAD DE MEMORIA ---
    def get_var(self, name):
        # Busca primero en el ámbito local (cima de la pila) y luego en el global
        if name in self.scope_stack[-1]:
            return self.scope_stack[-1][name]
        if name in self.variables:
            return self.variables[name]
        raise Exception(f"ACCESS ERROR: '{name}' no existe.")

    def set_var(self, name, value):
        # Las declaraciones nuevas van al ámbito actual
        self.scope_stack[-1][name] = value

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
        self.set_var(name, value)

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        # Actualizamos donde sea que exista la variable
        if name in self.scope_stack[-1]:
            self.scope_stack[-1][name] = value
        else:
            self.variables[name] = value
        return value

    # -------- CONTROL DE FLUJO --------
    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.ELSE():
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.block())

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

        # 1. VERIFICAR SI ES UNA FUNCIÓN DE KRYPTOMATH
        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        math_functions = {
            "factorial": KRYPTOMATH.factorial,
            "sin": KRYPTOMATH.sin,
            "cos": KRYPTOMATH.cos,
            "sqrt": KRYPTOMATH.sqrt,
            "log": KRYPTOMATH.log,
            "abs": KRYPTOMATH.abs_val,
            "pow": KRYPTOMATH.power
        }

        if name in math_functions:
            return math_functions[name](*args)

        # 2. VERIFICAR SI ES UNA FUNCIÓN DEFINIDA POR EL USUARIO
        if name not in self.functions:
            raise Exception(f"RUNTIME ERROR: La función '{name}' no existe.")

        func = self.functions[name]
        params = func["params"]

        if len(args) != len(params):
            raise Exception(f"ARGUMENT ERROR: '{name}' requiere {len(params)} parámetros.")

        # Crear nuevo ámbito local (Scope)
        local_vars = dict(zip(params, args))
        self.scope_stack.append(local_vars)

        result = None
        # Ejecutar el bloque de la función
        try:
            for stmt in func["ctx"].block().statement():
                if stmt.returnStmt():
                    result = self.visit(stmt.returnStmt().expr())
                    break
                self.visit(stmt)
        finally:
            # Siempre eliminar el ámbito al terminar (importante para recursión)
            self.scope_stack.pop()

        return result

    # -------- EXPRESIONES --------
    def visitExpr(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        if ctx.ID():
            return self.get_var(ctx.ID().getText())

        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr(0))

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
            return operations[op]() if op in operations else None

        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "!":
            return not self.visit(ctx.expr(0))

    # -------- LITERALES --------
    def visitLiteral(self, ctx):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            return float(text) if "." in text else int(text)
        
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        
        if ctx.BOOL_LIT():
            return True if ctx.BOOL_LIT().getText() == "sisas" else False
