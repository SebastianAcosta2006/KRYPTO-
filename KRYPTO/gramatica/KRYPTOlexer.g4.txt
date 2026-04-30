lexer grammar KryptoLexer;

// --- PALABRAS RESERVADAS (Identidad Krypto) ---
IF       : 'krif';
ELSE     : 'krelse';
WHILE    : 'krloop';
FOR      : 'krfor';
IN       : 'krin';
FUNCTION : 'krfunc';
RETURN   : 'yield';
END      : 'stop';
IMPORT   : 'use';
AS       : 'alias';

// --- TIPOS DE DATOS ---
INT       : 'num';
FLOAT     : 'dec';
BOOL_T    : 'logic';
STRING_T  : 'text';
LIST      : 'chain';
DICC      : 'vault';
MATRIX    : 'grid';
DATAFRAME : 'dataset';

// --- LITERALES ---
// Mantenemos tu toque original con los booleanos
BOOL_LIT : 'sisas' | 'nokas'; 
NUMBER   : [0-9]+ ('.' [0-9]+)?;
STRING   : '"' (~["\r\n])* '"' ;

// --- IDENTIFICADORES ---
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// --- OPERADORES ARITMÉTICOS ---
PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
MOD    : '%' ;
POW    : '^' ;
ASSIGN : '=' ;

// --- SIGNOS DE PUNTUACIÓN ---
COLON  : ':' ;
COMMA  : ',' ;
SEMI   : ';' ;
DOT    : '.' ;

// --- AGRUPADORES ---
LPAREN : '(' ;
RPAREN : ')' ;
LBRACK : '[' ;
RBRACK : ']' ;
LBRACE : '{' ;
RBRACE : '}' ;

// --- OPERADORES LÓGICOS Y COMPARACIÓN ---
EQ  : '==' ;
NEQ : '!=' ;
LE  : '<=' ;
GE  : '>=' ;
LT  : '<' ;
GT  : '>' ;

OR  : '||' ;
AND : '&&' ;
NOT : '!' ;

// --- TOKENS LIBRERIA GRÁFICA (KRYPTO_CHART) ---
PLOTVAG    : 'k_plot';
SHOWVAG    : 'k_show';
TITLEVAG   : 'k_title';
XLABELVAG  : 'k_xlabel';
YLABELVAG  : 'k_ylabel';


// --- COMENTARIOS Y ESPACIOS ---
// Comentarios estilo C/JS
COMMENT : '//' ~[\r\n]* -> skip ;
// Comentarios de bloque (Añadido para más profesionalismo)
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
WS      : [ \t\r\n]+ -> skip ;