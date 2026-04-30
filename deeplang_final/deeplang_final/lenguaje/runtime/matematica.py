PI = 3.141592653589793
E  = 2.718281828459045


def valor_absoluto(x):
    return x if x >= 0 else -x


def potencia(base, exp):
    if exp == 0:
        return 1.0
    if isinstance(exp, float) and not exp.is_integer():
        if base < 0:
            raise ValueError("Potencia fraccionaria de base negativa no esta definida")
        if base == 0:
            return 0.0
        return exponencial(exp * logaritmo_natural(base))
    n = int(exp)
    negativo = n < 0
    n = abs(n)
    r = 1.0
    for _ in range(n):
        r *= base
    return 1.0 / r if negativo else r


def raiz(x, n=2):
    n = int(n)
    if x < 0 and n % 2 == 0:
        raise ValueError("Raiz par de numero negativo no esta definida")
    if x == 0:
        return 0.0
    est = x / n
    for _ in range(300):
        est = ((n - 1) * est + x / potencia(est, n - 1)) / n
    return est


def exponencial(x):
    if x > 709:
        raise ValueError(f"Desbordamiento en exp({x})")
    suma = 1.0
    term = 1.0
    for n in range(1, 200):
        term *= x / n
        suma += term
        if valor_absoluto(term) < 1e-15:
            break
    return suma


def logaritmo_natural(x):
    if x <= 0:
        raise ValueError("ln(x) indefinido para x <= 0")
    k = 0
    while x > 2:
        x /= 2
        k += 1
    while x < 0.5:
        x *= 2
        k -= 1
    y = (x - 1) / (x + 1)
    y2 = y * y
    suma = 0.0
    py = y
    for n in range(200):
        suma += py / (2 * n + 1)
        py *= y2
        if valor_absoluto(py) < 1e-15:
            break
    return 2 * suma + k * 0.6931471805599453


def _norm(x):
    while x > PI:
        x -= 2 * PI
    while x < -PI:
        x += 2 * PI
    return x


def seno(x):
    x = _norm(x)
    suma = 0.0
    term = x
    for n in range(1, 60):
        suma += term
        term *= -x * x / ((2 * n) * (2 * n + 1))
        if valor_absoluto(term) < 1e-15:
            break
    return suma


def coseno(x):
    x = _norm(x)
    suma = 0.0
    term = 1.0
    for n in range(1, 60):
        suma += term
        term *= -x * x / ((2 * n - 1) * (2 * n))
        if valor_absoluto(term) < 1e-15:
            break
    return suma


def tangente(x):
    c = coseno(x)
    if valor_absoluto(c) < 1e-10:
        raise ValueError("tan(x) indefinida en este punto")
    return seno(x) / c


def _aplanar(v):
    if not v:
        return []
    if isinstance(v[0], list):
        return [x for fila in v for x in fila]
    return list(v)


def regresion_lineal(X, Y):
    xs = _aplanar(X)
    ys = _aplanar(Y)
    if len(xs) != len(ys):
        raise ValueError("X e Y deben tener el mismo numero de elementos")
    n = len(xs)
    if n < 2:
        raise ValueError("Se necesitan al menos 2 puntos")
    sx  = sum(xs)
    sy  = sum(ys)
    sxy = sum(xs[i] * ys[i] for i in range(n))
    sx2 = sum(xs[i] ** 2    for i in range(n))
    den = n * sx2 - sx * sx
    if valor_absoluto(den) < 1e-12:
        raise ValueError("Division por cero en regresion: X sin variacion")
    m = (n * sxy - sx * sy) / den
    b = (sy - m * sx) / n
    return [m, b]


def predecir_lineal(modelo, x):
    if not isinstance(modelo, list) or len(modelo) != 2:
        raise ValueError("modelo debe ser [pendiente, intercepto]")
    m, b = modelo
    return m * x + b


def mse(X, Y, modelo):
    xs = _aplanar(X)
    ys = _aplanar(Y)
    m, b = modelo
    n = len(xs)
    return sum((ys[i] - (m * xs[i] + b)) ** 2 for i in range(n)) / n


def media(valores):
    v = _aplanar(valores)
    if not v:
        raise ValueError("Lista vacia")
    return sum(v) / len(v)


def varianza(valores):
    v = _aplanar(valores)
    mu = media(v)
    return sum((x - mu) ** 2 for x in v) / len(v)


def desviacion_estandar(valores):
    return raiz(varianza(valores))
