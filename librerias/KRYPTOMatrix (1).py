# librerias/KRYPTOMATRIX.py

class KRYPTOMATRIX:

    # =========================
    # CREACIÓN DE MATRICES
    # =========================

    @staticmethod
    def mat_zeros(filas, columnas):

        # Crea una matriz llena de ceros
        return [
            [0.0 for _ in range(columnas)]
            for _ in range(filas)
        ]


    @staticmethod
    def mat_ones(filas, columnas):

        # Crea una matriz llena de unos
        return [
            [1.0 for _ in range(columnas)]
            for _ in range(filas)
        ]


    @staticmethod
    def mat_identity(n):

        # Matriz identidad
        # Los 1 van en la diagonal principal

        res = KRYPTOMATRIX.mat_zeros(n, n)

        for i in range(n):
            res[i][i] = 1.0

        return res


    # =========================
    # ACCESO A DATOS
    # =========================

    @staticmethod
    def mat_set(matriz, i, j, valor):

        # Se hace copia para no modificar
        # la matriz original

        nueva = [fila[:] for fila in matriz]

        nueva[int(i)][int(j)] = float(valor)

        return nueva


    @staticmethod
    def mat_get(matriz, i, j):

        return matriz[int(i)][int(j)]


    @staticmethod
    def mat_row(matriz, i):

        # Devuelve una fila completa
        return matriz[int(i)]


    @staticmethod
    def mat_col(matriz, j):

        # Devuelve una columna completa

        return [
            fila[int(j)]
            for fila in matriz
        ]


    @staticmethod
    def mat_shape(matriz):

        # Devuelve tamaño de la matriz

        if not matriz:
            return [0, 0]

        return [len(matriz), len(matriz[0])]


    # =========================
    # OPERACIONES BÁSICAS
    # =========================

    @staticmethod
    def mat_add(A, B):

        filas = len(A)
        columnas = len(A[0])

        res = KRYPTOMATRIX.mat_zeros(filas, columnas)

        for i in range(filas):

            for j in range(columnas):

                res[i][j] = A[i][j] + B[i][j]

        return res


    @staticmethod
    def mat_sub(A, B):

        filas = len(A)
        columnas = len(A[0])

        res = KRYPTOMATRIX.mat_zeros(filas, columnas)

        for i in range(filas):

            for j in range(columnas):

                res[i][j] = A[i][j] - B[i][j]

        return res


    @staticmethod
    def mat_scalar(A, k):

        # Multiplicación por escalar

        filas = len(A)
        columnas = len(A[0])

        res = KRYPTOMATRIX.mat_zeros(filas, columnas)

        for i in range(filas):

            for j in range(columnas):

                res[i][j] = A[i][j] * k

        return res


    # =========================
    # ÁLGEBRA LINEAL
    # =========================

    @staticmethod
    def mat_transpose(A):

        filas = len(A)
        columnas = len(A[0])

        res = KRYPTOMATRIX.mat_zeros(columnas, filas)

        for i in range(filas):

            for j in range(columnas):

                res[j][i] = A[i][j]

        return res


    @staticmethod
    def mat_mul(A, B):

        # Multiplicación clásica de matrices

        f1 = len(A)
        c1 = len(A[0])

        f2 = len(B)
        c2 = len(B[0])

        if c1 != f2:
            raise Exception("Matrices incompatibles")

        res = KRYPTOMATRIX.mat_zeros(f1, c2)

        for i in range(f1):

            for j in range(c2):

                suma = 0

                for k in range(c1):

                    suma += A[i][k] * B[k][j]

                res[i][j] = suma

        return res


    @staticmethod
    def mat_dot(v1, v2):

        # Producto punto entre vectores

        suma = 0

        for x, y in zip(v1, v2):

            suma += x * y

        return suma


    @staticmethod
    def mat_trace(A):

        # Suma diagonal principal

        n = min(len(A), len(A[0]))

        suma = 0

        for i in range(n):

            suma += A[i][i]

        return suma


    @staticmethod
    def mat_norm(A):

        # Norma Frobenius

        from librerias.KRYPTOMATH import KRYPTOMATH

        suma = 0

        for fila in A:

            for valor in fila:

                suma += valor ** 2

        return KRYPTOMATH.sqrt(suma)


    # =========================
    # DETERMINANTE
    # =========================

    @staticmethod
    def mat_det(A):

        n = len(A)

        # Caso 1x1
        if n == 1:
            return A[0][0]

        # Caso 2x2
        if n == 2:

            return (
                A[0][0] * A[1][1]
                -
                A[0][1] * A[1][0]
            )

        det = 0

        # Expansión por cofactores
        for c in range(n):

            sub = [
                fila[:c] + fila[c+1:]
                for fila in A[1:]
            ]

            det += (
                ((-1) ** c)
                *
                A[0][c]
                *
                KRYPTOMATRIX.mat_det(sub)
            )

        return det


    # =========================
    # MATRIZ INVERSA
    # =========================

    @staticmethod
    def mat_inverse(A):

        n = len(A)

        det = KRYPTOMATRIX.mat_det(A)

        if det == 0:
            raise Exception("No tiene inversa")

        # Caso simple 2x2
        if n == 2:

            return [
                [ A[1][1] / det, -A[0][1] / det ],
                [ -A[1][0] / det, A[0][0] / det ]
            ]

        # Matriz adjunta
        adj = KRYPTOMATRIX.mat_zeros(n, n)

        for i in range(n):

            for j in range(n):

                sub = [
                    fila[:j] + fila[j+1:]
                    for fila in (A[:i] + A[i+1:])
                ]

                adj[j][i] = (
                    ((-1) ** (i + j))
                    *
                    KRYPTOMATRIX.mat_det(sub)
                    /
                    det
                )

        return adj