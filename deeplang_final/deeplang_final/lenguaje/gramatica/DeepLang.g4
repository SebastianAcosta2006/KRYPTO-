grammar DeepLang;

// ─── Raiz ────────────────────────────────────────────────────
modulo
    : sentencia* FIN_ARCHIVO
    ;

sentencia
    : enlace
    | forma
    | traer
    | traerDe
    | expresionSentencia
    ;

// ─── Enlace de valores ───────────────────────────────────────
// Sintaxis: fijar nombre <- expresion
enlace
    : FIJAR IDENT FLECHA_IZQ expresion
    ;

// ─── Definicion de forma (funcion) ──────────────────────────
// Sintaxis: forma nombre { param1 param2 } -> expresion
forma
    : FORMA IDENT LLAVE_AB params LLAVE_CE APUNTA expresion
    ;

params
    : IDENT*
    ;

// ─── Modulos ─────────────────────────────────────────────────
// Sintaxis: traer nucleo
// Sintaxis: traer nucleo ~> alias
traer
    : TRAER IDENT (RENOMBRAR IDENT)?
    ;

// Sintaxis: desde nucleo tomar { sen cos }
traerDe
    : DESDE IDENT TOMAR LLAVE_AB listaSimbolos LLAVE_CE
    ;

listaSimbolos
    : IDENT (SEPARADOR IDENT)*
    ;

expresionSentencia
    : expresion
    ;

// ─── Expresiones (precedencia ascendente) ────────────────────
expresion
    : expresion DISYUNCION expresionY          # expO
    | expresionY                               # expOPasa
    ;

expresionY
    : expresionY CONJUNCION expresionIgualdad  # expY
    | expresionIgualdad                        # expYPasa
    ;

expresionIgualdad
    : expresionIgualdad opIgualdad expresionOrd  # expIgualdad
    | expresionOrd                               # expIgualdadPasa
    ;

expresionOrd
    : expresionOrd opOrd expresionSuma         # expOrd
    | expresionSuma                            # expOrdPasa
    ;

expresionSuma
    : expresionSuma MAS expresionProd          # expSuma
    | expresionSuma MENOS expresionProd        # expResta
    | expresionSuma UNION_MAT expresionProd    # expMatSuma
    | expresionSuma DIFER_MAT expresionProd    # expMatResta
    | expresionProd                            # expSumaPasa
    ;

expresionProd
    : expresionProd POR expresionProd          # expProd
    | expresionProd ENTRE expresionProd        # expDiv
    | expresionProd RESTO expresionProd        # expMod
    | expresionProd PROD_MAT expresionProd     # expMatProd
    | expresionPotencia                        # expProdPasa
    ;

expresionPotencia
    : expresionUnaria POTENCIA expresionPotencia  # expPotencia
    | expresionUnaria                             # expPotenciaPasa
    ;

expresionUnaria
    : MENOS expresionPrimaria                  # expNegar
    | NEGAR expresionPrimaria                  # expNo
    | expresionPrimaria                        # expUnariaPasa
    ;

expresionPrimaria
    : ENTERO                                   # litEntero
    | DECIMAL                                  # litDecimal
    | CADENA                                   # litCadena
    | CIERTO                                   # litCierto
    | FALSO                                    # litFalso
    | tablero                                  # litTablero
    | invocacion                               # expInvocacion
    | accesoModulo                             # expAccesoModulo
    | IDENT                                    # expIdent
    | PAREN_AB expresion PAREN_CE              # expAgrupada
    ;

// ─── Tablero (matriz) ────────────────────────────────────────
// Sintaxis: [ [1 2] [3 4] ]
tablero
    : CORCH_AB hilera (SEPARADOR hilera)* CORCH_CE
    ;

hilera
    : CORCH_AB expresion (SEPARADOR expresion)* CORCH_CE
    ;

// ─── Invocacion ──────────────────────────────────────────────
// Simple: fn(a b)   -- espacios separan argumentos, sin comas
// Con modulo: mod::fn(a b)
invocacion
    : IDENT PAREN_AB listaArgs? PAREN_CE           # invoSimple
    | IDENT SEPARADOR_MOD IDENT PAREN_AB listaArgs? PAREN_CE  # invoModulo
    ;

listaArgs
    : expresion (SEPARADOR expresion)*
    ;

accesoModulo
    : IDENT SEPARADOR_MOD IDENT
    ;

opIgualdad
    : IGUAL_IGUAL | DISTINTO
    ;

opOrd
    : MENOR | MAYOR | MENOR_IGUAL | MAYOR_IGUAL
    ;

// ─── Tokens ──────────────────────────────────────────────────

FIJAR        : 'fijar'  ;
FORMA        : 'forma'  ;
TRAER        : 'traer'  ;
DESDE        : 'desde'  ;
TOMAR        : 'tomar'  ;
RENOMBRAR    : '~>'     ;
CIERTO       : 'cierto' ;
FALSO        : 'falso'  ;
DISYUNCION   : 'o'      ;
CONJUNCION   : 'y'      ;
NEGAR        : 'no'     ;

FLECHA_IZQ   : '<-'     ;
APUNTA       : '->'     ;
LLAVE_AB     : '{'      ;
LLAVE_CE     : '}'      ;
PAREN_AB     : '('      ;
PAREN_CE     : ')'      ;
CORCH_AB     : '['      ;
CORCH_CE     : ']'      ;
SEPARADOR    : ','      ;
SEPARADOR_MOD: '::'     ;

MAS          : '+'      ;
MENOS        : '-'      ;
POR          : '*'      ;
ENTRE        : '/'      ;
RESTO        : '%'      ;
POTENCIA     : '^'      ;
UNION_MAT    : '[+]'    ;
DIFER_MAT    : '[-]'    ;
PROD_MAT     : '[*]'    ;

IGUAL_IGUAL  : '=='     ;
DISTINTO     : '/='     ;
MENOR        : '<'      ;
MAYOR        : '>'      ;
MENOR_IGUAL  : '<='     ;
MAYOR_IGUAL  : '>='     ;

DECIMAL      : [0-9]+ '.' [0-9]+ ;
ENTERO       : [0-9]+             ;
CADENA       : '"' (~["\r\n])* '"' ;
IDENT        : [a-zA-Z_][a-zA-Z0-9_]* ;

COMENTARIO   : '--' ~[\r\n]* -> skip ;
BLOQUE_COM   : '{-' .*? '-}' -> skip ;
ESPACIOS     : [ \t\r\n]+    -> skip ;
