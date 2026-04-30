import sys
import os
from antlr4 import InputStream, CommonTokenStream
from grammar.generated.KryptoLexer import KryptoLexer
from grammar.generated.KryptoParser import KryptoParser
from interpreter import KryptoInterpreter
from librerias.archivos import leer_archivo

def run_krypto_script():
    print("--- KRYPTO Engine v1.0 ---")
    
    try:
        # Pedimos el nombre del script
        target_file = input("➤ Nombre del script Krypto (sin extensión): ").strip()
        
        # Forzamos la extensión .kr para darle identidad al lenguaje
        if not target_file.endswith(".kr"):
            filename = f"{target_file}.kr"
        else:
            filename = target_file

        path = os.path.join("scripts", filename)

        if not os.path.exists(path):
            print(f"✖ Error: No se encontró el archivo '{filename}' en la carpeta 'scripts/'.")
            return

        # Cargamos el código fuente
        source_code = leer_archivo(path)
        
        # Configuración del pipeline de ANTLR4
        input_stream = InputStream(source_code)
        lexer = KryptoLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = KryptoParser(token_stream)
        
        # Generación del árbol sintáctico (AST)
        syntax_tree = parser.program()

        # Ejecución mediante el Visitor
        engine = KryptoInterpreter()
        print(f" Ejecutando {filename}...\n")
        engine.visit(syntax_tree)
        print("\n--- Ejecución finalizada con éxito ---")

    except Exception as error:
        print(f"[Krypto System Error]: {error}")

if __name__ == "__main__":
    run_krypto_script()