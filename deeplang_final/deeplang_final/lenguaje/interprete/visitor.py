import sys
import os

_BASE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(_BASE, '..', 'gramatica', 'generated'))
sys.path.insert(0, os.path.join(_BASE, '..', 'runtime'))

from generated.DeepLangVisitor  import DeepLangVisitor
from entorno  import Entorno
from errores  import ErrorDeepLang
import matrices as mx


class FormaUsuario:
    def __init__(self, nombre, params, cuerpo, closure):
        self.nombre  = nombre
        self.params  = params
        self.cuerpo  = cuerpo
        self.closure = closure


class EjecutorDeepLang(DeepLangVisitor):

    def __init__(self):
        from modulos import obtener_modulo
        self._obtener_modulo = obtener_modulo
        self.entorno = Entorno()

    # ──────────────────────────────────────────────────────────
    # Modulo
    # ──────────────────────────────────────────────────────────

    def visitModulo(self, ctx):
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)
        return resultado

    def visitSentencia(self, ctx):
        return self.visitChildren(ctx)

    def visitExpresionSentencia(self, ctx):
        return self.visit(ctx.expresion())

    # ──────────────────────────────────────────────────────────
    # Enlace y forma
    # ──────────────────────────────────────────────────────────

    def visitEnlace(self, ctx):
        nombre = ctx.IDENT().getText()
        valor  = self.visit(ctx.expresion())
        if self.entorno.existe_local(nombre):
            self.entorno.asignar(nombre, valor)
        else:
            self.entorno.definir(nombre, valor)
        return valor

    def visitForma(self, ctx):
        nombre = ctx.IDENT().getText()
        params = [p.getText() for p in ctx.params().IDENT()]
        cuerpo = ctx.expresion()
        fn     = FormaUsuario(nombre, params, cuerpo, self.entorno)
        if self.entorno.existe_local(nombre):
            self.entorno.asignar(nombre, fn)
        else:
            self.entorno.definir(nombre, fn)
        # Actualiza closure para habilitar recursion
        fn.closure = self.entorno
        return fn

    # ──────────────────────────────────────────────────────────
    # Modulos
    # ──────────────────────────────────────────────────────────

    def visitTraer(self, ctx):
        ids    = ctx.IDENT()
        nombre = ids[0].getText()
        alias  = ids[1].getText() if len(ids) > 1 else nombre
        mod    = self._cargar_modulo(nombre)
        if self.entorno.existe_local(alias):
            raise ErrorDeepLang(f"'{alias}' ya esta definido")
        self.entorno.definir(alias, mod)

    def visitTraerDe(self, ctx):
        nombre    = ctx.IDENT().getText()
        mod       = self._cargar_modulo(nombre)
        simbolos  = ctx.listaSimbolos()
        for tok in simbolos.IDENT():
            fn = tok.getText()
            if fn not in mod:
                raise ErrorDeepLang(f"'{fn}' no existe en '{nombre}'")
            if self.entorno.existe_local(fn):
                raise ErrorDeepLang(f"Conflicto: '{fn}' ya esta definido")
            self.entorno.definir(fn, mod[fn])

    def _cargar_modulo(self, nombre):
        try:
            return self._obtener_modulo(nombre)
        except RuntimeError as e:
            raise ErrorDeepLang(str(e))

    # ──────────────────────────────────────────────────────────
    # Invocaciones
    # ──────────────────────────────────────────────────────────

    def visitExpInvocacion(self, ctx):
        return self.visit(ctx.invocacion())

    def visitInvoSimple(self, ctx):
        nombre = ctx.IDENT().getText()
        fn     = self._resolver(nombre)
        args   = self._args(ctx)
        return self._invocar(fn, args, nombre)

    def visitInvoModulo(self, ctx):
        nombre_mod = ctx.IDENT(0).getText()
        nombre_fn  = ctx.IDENT(1).getText()
        mod        = self._resolver(nombre_mod)
        if not isinstance(mod, dict):
            raise ErrorDeepLang(f"'{nombre_mod}' no es un modulo")
        if nombre_fn not in mod:
            raise ErrorDeepLang(f"'{nombre_fn}' no existe en '{nombre_mod}'")
        fn   = mod[nombre_fn]
        args = self._args(ctx)
        return self._invocar(fn, args, f"{nombre_mod}::{nombre_fn}")

    def _args(self, ctx):
        if ctx.listaArgs():
            return [self.visit(e) for e in ctx.listaArgs().expresion()]
        return []

    def _resolver(self, nombre):
        try:
            return self.entorno.obtener(nombre)
        except RuntimeError:
            raise ErrorDeepLang(
                f"Nombre no definido: '{nombre}'. "
                f"Verifica que trajiste el modulo necesario."
            )

    def _invocar(self, fn, args, nombre):
        # Funcion de modulo (lambda Python)
        if callable(fn):
            try:
                return fn(args)
            except ErrorDeepLang:
                raise
            except (ValueError, TypeError, RuntimeError) as e:
                raise ErrorDeepLang(f"Error en '{nombre}': {e}")

        # Forma definida por el usuario
        if isinstance(fn, FormaUsuario):
            if len(args) != len(fn.params):
                raise ErrorDeepLang(
                    f"'{fn.nombre}' espera {len(fn.params)} argumento(s), "
                    f"recibio {len(args)}"
                )
            nuevo = fn.closure.nuevo_ambito()
            for p, v in zip(fn.params, args):
                nuevo.definir(p, v)
            env_ant      = self.entorno
            self.entorno = nuevo
            resultado    = self.visit(fn.cuerpo)
            self.entorno = env_ant
            return resultado

        # Constante de modulo (pi, e)
        if isinstance(fn, (int, float)):
            if args:
                raise ErrorDeepLang(f"'{nombre}' es una constante, no se puede invocar")
            return fn

        raise ErrorDeepLang(f"'{nombre}' no es invocable")

    # ──────────────────────────────────────────────────────────
    # Acceso a modulo como valor (mod::fn sin parentesis)
    # ──────────────────────────────────────────────────────────

    def visitExpAccesoModulo(self, ctx):
        return self.visit(ctx.accesoModulo())

    def visitAccesoModulo(self, ctx):
        nombre_mod = ctx.IDENT(0).getText()
        nombre_fn  = ctx.IDENT(1).getText()
        mod        = self._resolver(nombre_mod)
        if not isinstance(mod, dict):
            raise ErrorDeepLang(f"'{nombre_mod}' no es un modulo")
        if nombre_fn not in mod:
            raise ErrorDeepLang(f"'{nombre_fn}' no existe en '{nombre_mod}'")
        return mod[nombre_fn]

    # ──────────────────────────────────────────────────────────
    # Aritmetica
    # ──────────────────────────────────────────────────────────

    def visitExpSuma(self, ctx):
        return self.visit(ctx.expresionSuma()) + self.visit(ctx.expresionProd())

    def visitExpResta(self, ctx):
        return self.visit(ctx.expresionSuma()) - self.visit(ctx.expresionProd())

    def visitExpProd(self, ctx):
        return self.visit(ctx.expresionProd(0)) * self.visit(ctx.expresionProd(1))

    def visitExpDiv(self, ctx):
        d = self.visit(ctx.expresionProd(1))
        if d == 0:
            raise ErrorDeepLang("Division por cero")
        return self.visit(ctx.expresionProd(0)) / d

    def visitExpMod(self, ctx):
        d = self.visit(ctx.expresionProd(1))
        if d == 0:
            raise ErrorDeepLang("Modulo por cero")
        return self.visit(ctx.expresionProd(0)) % d

    def visitExpPotencia(self, ctx):
        from matematica import potencia
        base = self.visit(ctx.expresionUnaria())
        exp  = self.visit(ctx.expresionPotencia())
        try:
            return potencia(base, exp)
        except ValueError as e:
            raise ErrorDeepLang(str(e))

    def visitExpNegar(self, ctx):
        return -self.visit(ctx.expresionPrimaria())

    def visitExpNo(self, ctx):
        return not self.visit(ctx.expresionPrimaria())

    # ──────────────────────────────────────────────────────────
    # Tableros (matrices)
    # ──────────────────────────────────────────────────────────

    def visitExpMatSuma(self, ctx):
        return mx.sumar(
            self.visit(ctx.expresionSuma()),
            self.visit(ctx.expresionProd())
        )

    def visitExpMatResta(self, ctx):
        return mx.restar(
            self.visit(ctx.expresionSuma()),
            self.visit(ctx.expresionProd())
        )

    def visitExpMatProd(self, ctx):
        return mx.multiplicar(
            self.visit(ctx.expresionProd(0)),
            self.visit(ctx.expresionProd(1))
        )

    def visitLitTablero(self, ctx):
        return self.visit(ctx.tablero())

    def visitTablero(self, ctx):
        return [self.visit(h) for h in ctx.hilera()]

    def visitHilera(self, ctx):
        return [self.visit(e) for e in ctx.expresion()]

    # ──────────────────────────────────────────────────────────
    # Comparaciones y logica
    # ──────────────────────────────────────────────────────────

    def visitExpIgualdad(self, ctx):
        izq = self.visit(ctx.expresionIgualdad())
        der = self.visit(ctx.expresionOrd())
        op  = ctx.opIgualdad().getText()
        return izq == der if op == '==' else izq != der

    def visitExpOrd(self, ctx):
        izq = self.visit(ctx.expresionOrd())
        der = self.visit(ctx.expresionSuma())
        op  = ctx.opOrd().getText()
        tabla = {
            '<' : lambda a, b: a <  b,
            '>' : lambda a, b: a >  b,
            '<=': lambda a, b: a <= b,
            '>=': lambda a, b: a >= b,
        }
        return tabla[op](izq, der)

    def visitExpO(self, ctx):
        return self.visit(ctx.expresion()) or self.visit(ctx.expresionY())

    def visitExpY(self, ctx):
        return self.visit(ctx.expresionY()) and self.visit(ctx.expresionIgualdad())

    # ──────────────────────────────────────────────────────────
    # Literales
    # ──────────────────────────────────────────────────────────

    def visitLitEntero(self, ctx):
        return float(ctx.ENTERO().getText())

    def visitLitDecimal(self, ctx):
        return float(ctx.DECIMAL().getText())

    def visitLitCadena(self, ctx):
        return ctx.CADENA().getText()[1:-1]

    def visitLitCierto(self, ctx):
        return True

    def visitLitFalso(self, ctx):
        return False

    def visitExpIdent(self, ctx):
        return self._resolver(ctx.IDENT().getText())

    def visitExpAgrupada(self, ctx):
        return self.visit(ctx.expresion())

    # ──────────────────────────────────────────────────────────
    # Pases de precedencia (nodo de un solo hijo)
    # ──────────────────────────────────────────────────────────

    def visitExpOPasa(self, ctx):         return self.visitChildren(ctx)
    def visitExpYPasa(self, ctx):         return self.visitChildren(ctx)
    def visitExpIgualdadPasa(self, ctx):  return self.visitChildren(ctx)
    def visitExpOrdPasa(self, ctx):       return self.visitChildren(ctx)
    def visitExpSumaPasa(self, ctx):      return self.visitChildren(ctx)
    def visitExpProdPasa(self, ctx):      return self.visitChildren(ctx)
    def visitExpPotenciaPasa(self, ctx):  return self.visitChildren(ctx)
    def visitExpUnariaPasa(self, ctx):    return self.visitChildren(ctx)
