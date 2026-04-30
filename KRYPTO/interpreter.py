from grammar.generated.KryptoParserVisitor import KryptoParserVisitor
from grammar.generated.KryptoParser import KryptoParser

class KryptoInterpreter(KryptoParserVisitor):

    def __init__(self):
        # Almacenamiento de variables y funciones en tiempo de ejecución
        self.variables = {}
        self.functions = {}

    # -------- PROGRAMA --------
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # -------- SENTENCIAS (STATEMENTS) --------
    def visitStatement(self, ctx):
        if ctx.expr():
            result = self.visit(ctx.expr())
            # Si es una expresión suelta (como en el REPL), la mostramos
            if result is not None:
                print(result)
            return result
        return self.visitChildren(ctx)

    # -------- BLOQUE DE CÓDIGO --------
    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # -------- GESTIÓN DE VARIABLES --------
    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        # Si tiene asignación inicial, la procesamos; si no, es None
        value = self.visit(ctx.expr()) if ctx.expr() else None
        self.variables[name] = value

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        
        # En Krypto, si asignas a algo que no existe, lo creamos (dinámico)
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
        # inicialización (ej: i = 0)
        self.visit(ctx.assignment(0))
        # condición y ejecución
        while self.visit(ctx.expr()):
            self.visit(ctx.block())
            # actualización (ej: i = i + 1)
            self.visit(ctx.assignment(1))

    # -------- FUNCIONES --------
    def visitFunctionDecl(self, ctx):
        name = ctx.ID().getText()
        params = []
        if ctx.paramList():
            params = [p.getText() for p in ctx.paramList().ID()]
        
        # Guardamos la estructura de la función para usarla después
        self.functions[name] = {
            "params": params,
            "ctx": ctx
        }

    def visitFunctionCall(self, ctx):
        name = ctx.ID().getText()

        if name not in self.functions:
            raise Exception(f"RUNTIME ERROR: La función '{name}' no existe en el registro de Krypto.")

        func = self.functions[name]
        params = func["params"]

        # Procesar argumentos pasados
        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        if len(args) != len(params):
            raise Exception(f"ARGUMENT ERROR: '{name}' requiere {len(params)} parámetros, pero recibiste {len(args)}.")

        # Manejo de ámbito (Scope) local simple
        local_vars = dict(zip(params, args))
        old_vars = self.variables.copy()
        self.variables.update(local_vars)

        result = None
        # Ejecutar el cuerpo de la función
        for stmt in func["ctx"].block().statement():
            if stmt.returnStmt():
                result = self.visit(stmt.returnStmt().expr())
                break
            self.visit(stmt)

        # Restauramos las variables al salir de la función
        self.variables = old_vars
        return result

    # -------- LÓGICA DE EXPRESIONES --------
    def visitExpr(self, ctx):
        # 1. Literales (Números, Strings, Bools)
        if ctx.literal():
            return self.visit(ctx.literal())

        # 2. Llamadas a funciones dentro de expresiones
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # 3. Identificadores (Variables)
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.variables:
                raise Exception(f"ACCESS ERROR: La variable '{name}' no ha sido definida.")
            return self.variables[name]

        # 4. Agrupación (Paréntesis)
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr(0))

        # 5. Operaciones Binarias (Matemáticas y Lógicas)
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            operations = {
                '+':  lambda: left + right,
                '-':  lambda: left - right,
                '*':  lambda: left * right,
                '/':  lambda: left / right,
                '%':  lambda: left % right,
                '^':  lambda: left ** right,
                '==': lambda: left == right,
                '!=': lambda: left != right,
                '<':  lambda: left < right,
                '>':  lambda: left > right,
                '<=': lambda: left <= right,
                '>=': lambda: left >= right,
                '&&': lambda: left and right,
                '||': lambda: left or right
            }
            return operations[op]() if op in operations else None

        # 6. Operación Unaria (NOT)
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "!":
            return not self.visit(ctx.expr(0))

    # -------- TIPOS DE DATOS (LITERALES) --------
    def visitLiteral(self, ctx):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            return float(text) if "." in text else int(text)

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        if ctx.BOOL_LIT():
            val = ctx.BOOL_LIT().getText()
            # Mantenemos tu lógica personalizada: sisas = True, nop = False
            return True if val == "sisas" else False