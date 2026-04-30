import math
import os

class KRYPTO_CHART:
    # --- CONFIGURACIÓN DEL MOTOR ---
    titulo = "KRYPTO VISUALIZER"
    label_x = "EJE X"
    label_y = "EJE Y"
    
    # Paleta de colores Krypto (Cian, Neon, Dark)
    color_primario = (0, 255, 190)   # Cian Krypto
    color_secundario = (255, 0, 120) # Magenta de contraste
    color_fondo = (15, 15, 25)       # Azul muy oscuro (modo noche)
    color_texto = (240, 240, 240)    # Blanco roto
    color_rejilla = (40, 40, 60)     # Gris azulado

    # Diccionario de fuentes Bitmap 3x5
    FONTS = {
        '0': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]], '1': [[0,1,0],[1,1,0],[0,1,0],[0,1,0],[1,1,1]],
        '2': [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]], '3': [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]],
        '4': [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]], '5': [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]],
        '6': [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]], '7': [[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,0,0]],
        '8': [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]], '9': [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]],
        'A': [[0,1,0],[1,0,1],[1,1,1],[1,0,1],[1,0,1]], 'B': [[1,1,0],[1,0,1],[1,1,0],[1,0,1],[1,1,1]],
        'C': [[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,1,1]], 'D': [[1,1,0],[1,0,1],[1,0,1],[1,0,1],[1,1,0]],
        'E': [[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,1,1]], 'F': [[1,1,1],[1,0,0],[1,1,0],[1,0,0],[1,0,0]],
        'G': [[1,1,1],[1,0,0],[1,0,1],[1,0,1],[1,1,1]], 'H': [[1,0,1],[1,0,1],[1,1,1],[1,0,1],[1,0,1]],
        'I': [[1,1,1],[0,1,0],[0,1,0],[0,1,0],[1,1,1]], 'J': [[0,0,1],[0,0,1],[0,0,1],[1,0,1],[1,1,1]],
        'K': [[1,0,1],[1,0,1],[1,1,0],[1,0,1],[1,0,1]], 'L': [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
        'M': [[1,0,1],[1,1,1],[1,1,1],[1,0,1],[1,0,1]], 'N': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1]],
        'O': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]], 'P': [[1,1,1],[1,0,1],[1,1,1],[1,0,0],[1,0,0]],
        'Q': [[1,1,1],[1,0,1],[1,1,1],[0,1,1],[0,0,1]], 'R': [[1,1,1],[1,0,1],[1,1,0],[1,0,1],[1,0,1]],
        'S': [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]], 'T': [[1,1,1],[0,1,0],[0,1,0],[0,1,0],[0,1,0]],
        'U': [[1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]], 'V': [[1,0,1],[1,0,1],[1,0,1],[0,1,0],[0,1,0]],
        'W': [[1,0,1],[1,0,1],[1,1,1],[1,1,1],[1,0,1]], 'X': [[1,0,1],[1,0,1],[0,1,0],[1,0,1],[1,0,1]],
        'Y': [[1,0,1],[1,0,1],[0,1,0],[0,1,0],[0,1,0]], 'Z': [[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,1,1]],
        ' ': [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    }

    @staticmethod
    def setup_canvas(titulo, x_label, y_label):
        KRYPTO_CHART.titulo = str(titulo).upper()
        KRYPTO_CHART.label_x = str(x_label).upper()
        KRYPTO_CHART.label_y = str(y_label).upper()

    @staticmethod
    def dibujar_texto(imagen, x_pos, y_pos, texto, color=None):
        if color is None: color = KRYPTO_CHART.color_texto
        for char in str(texto).upper():
            if char in KRYPTO_CHART.FONTS:
                matriz = KRYPTO_CHART.FONTS[char]
                for f in range(5):
                    for c in range(3):
                        if matriz[f][c] == 1:
                            for df in range(2):
                                for dc in range(2):
                                    py, px = y_pos + (f*2) + df, x_pos + (c*2) + dc
                                    if 0 <= py < len(imagen) and 0 <= px < len(imagen[0]):
                                        imagen[py][px] = color
            x_pos += 10

    @staticmethod
    def _preparar_lienzo(max_val):
        ancho, alto = 650, 500
        m_inf, m_izq, m_sup, m_der = 80, 80, 70, 50
        img = [[KRYPTO_CHART.color_fondo for _ in range(ancho)] for _ in range(alto)]

        KRYPTO_CHART.dibujar_texto(img, (ancho // 2) - (len(KRYPTO_CHART.titulo) * 5), 25, KRYPTO_CHART.titulo)
        KRYPTO_CHART.dibujar_texto(img, 10, m_sup - 30, KRYPTO_CHART.label_y)
        KRYPTO_CHART.dibujar_texto(img, (ancho // 2) - (len(KRYPTO_CHART.label_x) * 5), alto - 35, KRYPTO_CHART.label_x)

        # Ejes
        for y in range(m_sup, alto - m_inf): img[y][m_izq] = KRYPTO_CHART.color_texto
        for x in range(m_izq, ancho - m_der): img[alto - m_inf][x] = KRYPTO_CHART.color_texto

        # Rejilla y valores Y
        for i in range(0, 6):
            val_ref = int((i * 0.2) * max_val)
            y_p = (alto - m_inf) - int((i * 0.2) * (alto - m_inf - m_sup - 20))
            KRYPTO_CHART.dibujar_texto(img, m_izq - 50, y_p - 5, val_ref)
            for x in range(m_izq, ancho - m_der):
                if x % 6 == 0: img[y_p][x] = KRYPTO_CHART.color_rejilla
        
        return img, ancho, alto, m_inf, m_izq, m_sup, m_der

    @staticmethod
    def generar_barras(etiquetas, valores, nombre_archivo="chart_barras.ppm"):
        if not valores: return
        max_v = max(valores) if valores else 1
        img, anc, alt, m_inf, m_izq, m_sup, m_der = KRYPTO_CHART._preparar_lienzo(max_v)
        
        n = len(valores)
        ancho_secc = (anc - m_izq - m_der) // n

        for i, v in enumerate(valores):
            h = int((v / max_v) * (alt - m_inf - m_sup - 20))
            x_c = m_izq + (i * ancho_secc) + (ancho_secc // 2)
            x_i, x_f = x_c - (ancho_secc // 3), x_c + (ancho_secc // 3)
            
            for y in range((alt - m_inf) - h, alt - m_inf):
                for x in range(x_i, x_f):
                    if 0 <= y < alt and 0 <= x < anc: 
                        img[y][x] = KRYPTO_CHART.color_primario
        
        KRYPTO_CHART._guardar(img, anc, alt, nombre_archivo)

    @staticmethod
    def _guardar(imagen, ancho, alto, nombre):
        # Asegurar que existe carpeta de salida
        if not os.path.exists("outputs"): os.makedirs("outputs")
        ruta = os.path.join("outputs", nombre)
        
        with open(ruta, "w") as f:
            f.write(f"P3\n{ancho} {alto}\n255\n")
            for fila in imagen:
                f.write(" ".join(f"{r} {g} {b}" for r, g, b in fila) + "\n")
        print(f"⬚ [KRYPTO_GRAPH]: Renderizado exitoso en '{ruta}'")