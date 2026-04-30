import sys
import os

_RAIZ     = os.path.dirname(os.path.abspath(__file__))
_GRAM_GEN = os.path.join(_RAIZ, 'lenguaje', 'gramatica', 'generated')
_INTERP   = os.path.join(_RAIZ, 'lenguaje', 'interprete')
_RUNTIME  = os.path.join(_RAIZ, 'lenguaje', 'runtime')

sys.path.insert(0, _GRAM_GEN)
sys.path.insert(0, _INTERP)
sys.path.insert(0, _RUNTIME)

from antlr4 import CommonTokenStream, FileStream

from generated.DeepLangLexer    import DeepLangLexer
from generated.DeepLangParser   import DeepLangParser
from errores  import ErrorSintaxis, ErrorDeepLang
from visitor  import EjecutorDeepLang


def ejecutar(ruta):
    if not os.path.isfile(ruta):
        print(f"Archivo no encontrado: {ruta}", file=sys.stderr)
        sys.exit(1)

    flujo  = FileStream(ruta, encoding='utf-8')
    lexer  = DeepLangLexer(flujo)
    tokens = CommonTokenStream(lexer)
    parser = DeepLangParser(tokens)

    listener = ErrorSintaxis()
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(listener)
    parser.addErrorListener(listener)

    try:
        arbol = parser.modulo()
    except SyntaxError as e:
        print(f"Error de sintaxis: {e}", file=sys.stderr)
        sys.exit(1)

    ejecutor = EjecutorDeepLang()
    try:
        ejecutor.visit(arbol)
    except ErrorDeepLang as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 ejecucion/main.py <programa.dl>")
        sys.exit(1)
    ejecutar(sys.argv[1])
