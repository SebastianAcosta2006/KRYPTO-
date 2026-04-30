def _validar(A):
    f = len(A)
    if f == 0:
        raise ValueError("Tablero vacio")
    c = len(A[0])
    for fila in A:
        if len(fila) != c:
            raise ValueError("Hileras de distinto tamano")
    return f, c


def dimensiones(A):
    return _validar(A)


def ceros(f, c):
    return [[0.0] * c for _ in range(f)]


def identidad(n):
    M = ceros(n, n)
    for i in range(n):
        M[i][i] = 1.0
    return M


def sumar(A, B):
    f, c = _validar(A)
    fb, cb = _validar(B)
    if f != fb or c != cb:
        raise ValueError(f"Dimensiones incompatibles: {f}x{c} vs {fb}x{cb}")
    return [[A[i][j] + B[i][j] for j in range(c)] for i in range(f)]


def restar(A, B):
    f, c = _validar(A)
    fb, cb = _validar(B)
    if f != fb or c != cb:
        raise ValueError(f"Dimensiones incompatibles: {f}x{c} vs {fb}x{cb}")
    return [[A[i][j] - B[i][j] for j in range(c)] for i in range(f)]


def multiplicar(A, B):
    fa, ca = _validar(A)
    fb, cb = _validar(B)
    if ca != fb:
        raise ValueError(f"No multiplicables: {fa}x{ca} · {fb}x{cb}")
    R = ceros(fa, cb)
    for i in range(fa):
        for j in range(cb):
            for k in range(ca):
                R[i][j] += A[i][k] * B[k][j]
    return R


def transponer(A):
    f, c = _validar(A)
    return [[A[i][j] for i in range(f)] for j in range(c)]


def invertir(A):
    n, c = _validar(A)
    if n != c:
        raise ValueError("Solo tableros cuadrados tienen inverso")
    aug = [A[i][:] + identidad(n)[i] for i in range(n)]
    for col in range(n):
        piv = None
        for fila in range(col, n):
            if abs(aug[fila][col]) > 1e-10:
                piv = fila
                break
        if piv is None:
            raise ValueError("Tablero singular, no tiene inverso")
        aug[col], aug[piv] = aug[piv], aug[col]
        f = aug[col][col]
        aug[col] = [v / f for v in aug[col]]
        for fila in range(n):
            if fila != col:
                fc = aug[fila][col]
                aug[fila] = [aug[fila][j] - fc * aug[col][j] for j in range(2 * n)]
    return [fila[n:] for fila in aug]


def mostrar_tablero(A, etiqueta=""):
    f, c = _validar(A)
    if etiqueta:
        print(f"Tablero {etiqueta} [{f}x{c}]:")
    for fila in A:
        print("  [" + "  ".join(f"{v:9.4f}" for v in fila) + "]")
