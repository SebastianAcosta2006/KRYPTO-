from antlr4 import InputStream, CommonTokenStream
# Importamos basándonos en el nuevo nombre del lenguaje
from grammar.generated.KryptoLexer import KryptoLexer
from grammar.generated.KryptoParser import KryptoParser
from interpreter import KryptoInterpreter

def main():
    print("--- KRYPTO Shell v1.0 ---")
    print("Escribe 'exit()' para finalizar la sesión.\n")

    # Instanciamos el intérprete con el nuevo nombre
    interpreter = KryptoInterpreter()

    while True:
        try:
            # Un prompt más minimalista y técnico
            linea = input("krypto ❯ ").strip()

            if linea.lower() in ["exit()", "salir", "quit"]:
                print("Cerrando sesión en Krypto. ¡Hasta luego!")
                break

            if not linea:
                continue

            # Flujo de ANTLR4 ajustado a Krypto
            input_stream = InputStream(linea)
            lexer = KryptoLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = KryptoParser(token_stream)

            # Asumimos que la regla inicial en tu .g4 sigue siendo 'program'
            tree = parser.program()

            # Ejecución del Visitor
            interpreter.visit(tree)

        except EOFError:
            break
        except Exception as e:
            print(f"⬑ Error de ejecución: {e}")

if __name__ == "__main__":
    main()