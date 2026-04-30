import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'runtime'))
import matematica as mat
import matrices   as mx


def _num(args, idx, nombre):
    if idx >= len(args):
        raise RuntimeError(f"'{nombre}' necesita al menos {idx + 1} argumento(s)")
    v = args[idx]
    if not isinstance(v, (int, float)):
        raise RuntimeError(f"'{nombre}' esperaba un numero, recibio: {type(v).__name__}")
    return float(v)


def _mat(args, idx, nombre):
    if idx >= len(args):
        raise RuntimeError(f"'{nombre}' necesita al menos {idx + 1} argumento(s)")
    v = args[idx]
    if not isinstance(v, list):
        raise RuntimeError(f"'{nombre}' esperaba un tablero")
    return v


def _fmt(valor):
    if isinstance(valor, bool):
        return "cierto" if valor else "falso"
    if isinstance(valor, float) and valor == int(valor):
        return str(int(valor))
    if isinstance(valor, list):
        return str(valor)
    return str(valor)


# ─── Modulo nucleo ──────────────────────────────────────────
def _construir_nucleo():
    return {
        'emitir'    : lambda a: print(_fmt(a[0])),
        'sen'       : lambda a: mat.seno(_num(a, 0, 'sen')),
        'cos'       : lambda a: mat.coseno(_num(a, 0, 'cos')),
        'tan'       : lambda a: mat.tangente(_num(a, 0, 'tan')),
        'raiz'      : lambda a: mat.raiz(_num(a, 0, 'raiz')),
        'raizn'     : lambda a: mat.raiz(_num(a, 0, 'raizn'), _num(a, 1, 'raizn')),
        'abs'       : lambda a: mat.valor_absoluto(_num(a, 0, 'abs')),
        'exp'       : lambda a: mat.exponencial(_num(a, 0, 'exp')),
        'ln'        : lambda a: mat.logaritmo_natural(_num(a, 0, 'ln')),
        'pi'        : mat.PI,
        'e'         : mat.E,
    }


# ─── Modulo algebra (operaciones matriciales) ────────────────
def _construir_algebra():
    return {
        'transponer' : lambda a: mx.transponer(_mat(a, 0, 'transponer')),
        'invertir'   : lambda a: mx.invertir(_mat(a, 0, 'invertir')),
        'mostrar'    : lambda a: mx.mostrar_tablero(_mat(a, 0, 'mostrar')),
        'dim'        : lambda a: list(mx.dimensiones(_mat(a, 0, 'dim'))),
        'sumar'      : lambda a: mx.sumar(_mat(a, 0, 'sumar'), _mat(a, 1, 'sumar')),
        'restar'     : lambda a: mx.restar(_mat(a, 0, 'restar'), _mat(a, 1, 'restar')),
        'multiplicar': lambda a: mx.multiplicar(_mat(a, 0, 'multiplicar'), _mat(a, 1, 'multiplicar')),
    }


# ─── Modulo estadistica ──────────────────────────────────────
def _construir_estadistica():
    return {
        'ajustar'   : lambda a: mat.regresion_lineal(a[0], a[1]),
        'predecir'  : lambda a: mat.predecir_lineal(a[0], _num(a, 1, 'predecir')),
        'error_mse' : lambda a: mat.mse(a[0], a[1], a[2]),
        'media'     : lambda a: mat.media(a[0]),
        'varianza'  : lambda a: mat.varianza(a[0]),
        'desviacion': lambda a: mat.desviacion_estandar(a[0]),
    }


# ─── Modulo salida ───────────────────────────────────────────
def _construir_salida():
    return {
        'imprimir'  : lambda a: print(_fmt(a[0])),
        'linea'     : lambda a: print(),
        'rotulo'    : lambda a: print(str(a[0]) + ":", _fmt(a[1])),
        'tablero'   : lambda a: mx.mostrar_tablero(_mat(a, 0, 'tablero')),
    }


# ─── Modulo grafica (ASCII) ──────────────────────────────────
def _construir_grafica():
    def _histograma(args):
        datos = args[0]
        if isinstance(datos[0], list):
            datos = [x for f in datos for x in f]
        ancho = 40
        mn = min(datos)
        mx_ = max(datos)
        rango = mx_ - mn if mx_ != mn else 1
        barras = 10
        cubetas = [0] * barras
        for d in datos:
            idx = min(int((d - mn) / rango * barras), barras - 1)
            cubetas[idx] += 1
        max_c = max(cubetas) if cubetas else 1
        print("Histograma:")
        for i, c in enumerate(cubetas):
            val = mn + rango * i / barras
            barra = "#" * int(c / max_c * ancho)
            print(f"  {val:6.2f} | {barra} ({c})")

    def _dispersion(args):
        X = args[0]
        Y = args[1]
        if isinstance(X[0], list):
            X = [x for f in X for x in f]
        if isinstance(Y[0], list):
            Y = [y for f in Y for y in f]
        alto = 15
        ancho = 40
        xmn, xmx = min(X), max(X)
        ymn, ymx = min(Y), max(Y)
        rx = xmx - xmn if xmx != xmn else 1
        ry = ymx - ymn if ymx != ymn else 1
        lienzo = [[" "] * ancho for _ in range(alto)]
        for i in range(len(X)):
            col = min(int((X[i] - xmn) / rx * (ancho - 1)), ancho - 1)
            fil = min(int((Y[i] - ymn) / ry * (alto - 1)), alto - 1)
            lienzo[alto - 1 - fil][col] = "*"
        print("Dispersion:")
        print("  " + "-" * ancho)
        for fila in lienzo:
            print("  |" + "".join(fila) + "|")
        print("  " + "-" * ancho)

    return {
        'histograma'  : _histograma,
        'dispersion'  : _dispersion,
    }


MODULOS = {
    'nucleo'     : _construir_nucleo,
    'algebra'    : _construir_algebra,
    'estadistica': _construir_estadistica,
    'salida'     : _construir_salida,
    'grafica'    : _construir_grafica,
}


def obtener_modulo(nombre):
    if nombre not in MODULOS:
        disponibles = list(MODULOS.keys())
        raise RuntimeError(f"Modulo '{nombre}' no existe. Disponibles: {disponibles}")
    return MODULOS[nombre]()
