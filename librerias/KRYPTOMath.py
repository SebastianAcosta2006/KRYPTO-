# librerias/KRYPTOMATH.py

import os

class KRYPTOMATH:

    # =========================
    # CONFIGURACIÓN VISUAL
    # =========================

    titulo = "KRYPTO MATH"

    color_fondo   = (15, 15, 25)
    color_ejes    = (240, 240, 240)
    color_funcion = (0, 255, 190)
    color_rejilla = (40, 40, 60)

    ancho = 700
    alto = 500

    PI = 3.14159265358979323846
    E  = 2.71828182845904523536


    # =========================
    # FUNCIONES BÁSICAS
    # =========================

    @staticmethod
    def abs_val(x):
        return x if x >= 0 else -x

    @staticmethod
    def factorial(n):
        if n < 0:
            return None

        res = 1

        for i in range(2, int(n) + 1):
            res *= i

        return res


    # =========================
    # POTENCIAS Y RAÍCES
    # =========================

    @staticmethod
    def power(base, exp):

        if exp == 0:
            return 1

        if exp < 0:
            return 1 / KRYPTOMATH.power(base, -exp)

        if int(exp) == exp:

            res = 1

            for _ in range(int(exp)):
                res *= base

            return res

        return KRYPTOMATH.exp(exp * KRYPTOMATH.log(base))


    @staticmethod
    def sqrt(x):

        if x < 0:
            raise Exception("Raiz negativa")

        if x == 0:
            return 0

        res = x

        # Método de Newton
        for _ in range(10):
            res = 0.5 * (res + x / res)

        return res


    # =========================
    # EXPONENCIAL Y LOG
    # =========================

    @staticmethod
    def exp(x):

        res = 1.0
        termino = 1.0

        # Serie de Taylor
        for i in range(1, 20):

            termino *= x / i
            res += termino

        return res


    @staticmethod
    def log(x):

        if x <= 0:
            raise Exception("Log invalido")

        n = 0

        while x > 2:
            x /= KRYPTOMATH.E
            n += 1

        while x < 0.5:
            x *= KRYPTOMATH.E
            n -= 1

        z = (x - 1) / (x + 1)

        res = 0
        termino = z
        z2 = z * z

        for i in range(1, 20, 2):

            res += termino / i
            termino *= z2

        return 2 * res + n


    # =========================
    # TRIGONOMETRÍA
    # =========================

    @staticmethod
    def sin(x):

        x = x % (2 * KRYPTOMATH.PI)

        res = 0
        termino = x

        for i in range(1, 20, 2):

            res += termino
            termino *= -x * x / ((i + 1) * (i + 2))

        return res


    @staticmethod
    def cos(x):

        x = x % (2 * KRYPTOMATH.PI)

        res = 0
        termino = 1

        for i in range(0, 20, 2):

            res += termino
            termino *= -x * x / ((i + 1) * (i + 2))

        return res


    @staticmethod
    def tan(x):
        return KRYPTOMATH.sin(x) / KRYPTOMATH.cos(x)


    # =========================
    # CONVERSIÓN
    # =========================

    @staticmethod
    def radians(grados):
        return grados * KRYPTOMATH.PI / 180

    @staticmethod
    def degrees(rad):
        return rad * 180 / KRYPTOMATH.PI


    # =========================
    # ESTADÍSTICA
    # =========================

    @staticmethod
    def mean(lista):

        if not lista:
            return 0

        return sum(lista) / len(lista)


    @staticmethod
    def median(lista):

        if not lista:
            return 0

        datos = lista[:]
        n = len(datos)

        # Ordenamiento manual
        for i in range(n):

            for j in range(0, n - i - 1):

                if datos[j] > datos[j + 1]:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]

        if n % 2 == 0:
            return (datos[n//2 - 1] + datos[n//2]) / 2

        return datos[n//2]


    @staticmethod
    def variance(lista):

        if len(lista) < 2:
            return 0

        media = KRYPTOMATH.mean(lista)

        suma = 0

        for x in lista:
            suma += (x - media) ** 2

        return suma / (len(lista) - 1)


    # =========================
    # VECTORES
    # =========================

    @staticmethod
    def dot_product(v1, v2):

        if len(v1) != len(v2):
            raise Exception("Vectores diferentes")

        suma = 0

        for i in range(len(v1)):
            suma += v1[i] * v2[i]

        return suma


    @staticmethod
    def norm(v):

        suma = 0

        for x in v:
            suma += x * x

        return KRYPTOMATH.sqrt(suma)


    # =========================
    # COMBINATORIA
    # =========================

    @staticmethod
    def combinations(n, k):

        return (
            KRYPTOMATH.factorial(n) //
            (
                KRYPTOMATH.factorial(k) *
                KRYPTOMATH.factorial(n-k)
            )
        )


    @staticmethod
    def permutations(n, k):

        return (
            KRYPTOMATH.factorial(n) //
            KRYPTOMATH.factorial(n-k)
        )


    # =========================
    # GRAFICADOR
    # =========================

    @staticmethod
    def crear_lienzo():

        img = [
            [KRYPTOMATH.color_fondo for _ in range(KRYPTOMATH.ancho)]
            for _ in range(KRYPTOMATH.alto)
        ]

        centro_x = KRYPTOMATH.ancho // 2
        centro_y = KRYPTOMATH.alto // 2

        # Rejilla vertical
        for x in range(0, KRYPTOMATH.ancho, 50):

            for y in range(KRYPTOMATH.alto):
                img[y][x] = KRYPTOMATH.color_rejilla

        # Rejilla horizontal
        for y in range(0, KRYPTOMATH.alto, 50):

            for x in range(KRYPTOMATH.ancho):
                img[y][x] = KRYPTOMATH.color_rejilla

        # Eje X
        for x in range(KRYPTOMATH.ancho):
            img[centro_y][x] = KRYPTOMATH.color_ejes

        # Eje Y
        for y in range(KRYPTOMATH.alto):
            img[y][centro_x] = KRYPTOMATH.color_ejes

        return img


    @staticmethod
    def plot(funcion, xmin=-10, xmax=10, nombre="grafica.ppm"):

        img = KRYPTOMATH.crear_lienzo()

        centro_y = KRYPTOMATH.alto // 2

        escala_x = KRYPTOMATH.ancho / (xmax - xmin)
        escala_y = 40

        paso = 0.01
        x = xmin

        # Va recorriendo punto por punto
        while x <= xmax:

            try:

                y = funcion(x)

                px = int((x - xmin) * escala_x)
                py = int(centro_y - (y * escala_y))

                if (
                    0 <= px < KRYPTOMATH.ancho and
                    0 <= py < KRYPTOMATH.alto
                ):
                    img[py][px] = KRYPTOMATH.color_funcion

            except:
                pass

            x += paso

        KRYPTOMATH.guardar(img, nombre)


    @staticmethod
    def guardar(img, nombre):

        if not os.path.exists("outputs"):
            os.makedirs("outputs")

        ruta = os.path.join("outputs", nombre)

        with open(ruta, "w") as f:

            f.write(
                f"P3\n{KRYPTOMATH.ancho} {KRYPTOMATH.alto}\n255\n"
            )

            for fila in img:

                f.write(
                    " ".join(
                        f"{r} {g} {b}"
                        for r, g, b in fila
                    ) + "\n"
                )

        print(f"[KRYPTOMATH] Imagen guardada en: {ruta}")