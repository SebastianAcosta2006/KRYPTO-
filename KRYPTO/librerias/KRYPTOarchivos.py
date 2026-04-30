import os

def cargar_fuente_krypto(ruta_acceso):
    """
    Carga el contenido de un script .kr para su procesamiento.
    """
    try:
        if not os.path.exists(ruta_acceso):
            raise FileNotFoundError(f"El segmento de código en '{ruta_acceso}' no existe.")
            
        with open(ruta_acceso, "r", encoding="utf-8") as raw_file:
            contenido = raw_file.read()
            return contenido
            
    except FileNotFoundError as e:
        raise Exception(f"IO_ERROR: {e}")
    except Exception as e:
        raise Exception(f"SYSTEM_ACCESS_ERROR: No se pudo leer el flujo de datos: {e}")


def exportar_resultado_krypto(identificador, datos):
    """
    Guarda datos o logs en un archivo físico.
    """
    try:
        # Aseguramos que el directorio de salida exista
        directorio = os.path.dirname(identificador)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

        with open(identificador, "w", encoding="utf-8") as out_file:
            out_file.write(str(datos))
        return True
        
    except Exception as e:
        raise Exception(f"EXPORT_ERROR: Fallo al escribir en el disco: {e}")