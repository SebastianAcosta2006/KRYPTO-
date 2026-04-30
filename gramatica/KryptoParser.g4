parser grammar KryptoParser;

options { tokenVocab=KryptoLexer; }

// -------- ESTRUCTURA RAÍZ --------

program
    : statement* EOF
    ;

// -------- SENTENCIAS PRINCIPALES --------

statement
    : varDecl SEMI
    | assignment SEMI
    | ifStatement
    | whileStatement
    | forStatement
    | functionDecl
    | returnStmt SEMI
    | kryptoGraphicStmt    // Integración de las reglas gráficas
    | expr SEMI
    ;

// -------- GESTIÓN DE DATOS --------

varDecl
    : type ID (ASSIGN expr)?
    ;

type
    : INT
    | FLOAT
    | BOOL_T
    | STRING_T
    | LIST
    | MATRIX
    | DICC
    | DATAFRAME
    ;

assignment
    : ID ASSIGN expr
    ;

// -------- CONTROL DE FLUJO (ESTILO KRYPTO) --------

ifStatement
    : IF LPAREN expr RPAREN block
      (ELSE block)?
      STOP                 // Cambiado END por STOP según el Lexer
    ;

whileStatement
    : WHILE LPAREN expr RPAREN block STOP
    ;

forStatement
    : FOR LPAREN assignment SEMI expr SEMI assignment RPAREN block STOP
    ;

// -------- BLOQUES Y ESTRUCTURAS --------

block
    : LBRACE statement* RBRACE
    ;

functionDecl
    : FUNCTION ID LPAREN paramList? RPAREN block STOP
    ;

paramList
    : ID (COMMA ID)*
    ;

returnStmt
    : RETURN expr
    ;

// -------- MOTOR DE EXPRESIONES (PRECEDENCIA) --------

expr
    : expr POW expr                     # opPow
    | (MUL | DIV | MOD) expr            # opMulDiv
    | expr (PLUS | MINUS) expr          # opAddSub
    | expr (EQ | NEQ | LT | GT | LE | GE) expr # opCompare
    | expr (AND | OR) expr              # opLogical
    | NOT expr                          # opNot
    | LPAREN expr RPAREN                # opParens
    | functionCall                      # opCall
    | literal                           # opLiteral
    | ID                                # opId
    ;

// -------- LLAMADAS Y ARGUMENTOS --------

functionCall
    : ID LPAREN argList? RPAREN
    ;

argList
    : expr (COMMA expr)*
    ;

literal
    : NUMBER
    | STRING
    | BOOL_LIT
    ;

// -------- COMANDOS DEL MOTOR GRÁFICO (KRYPTO_CHART) --------

kryptoGraphicStmt
    : PLOTVAG LPAREN expr COMMA expr RPAREN SEMI    // k_plot(x, y);
    | TITLEVAG LPAREN STRING RPAREN SEMI           // k_title("Mi Grafico");
    | XLABELVAG LPAREN STRING RPAREN SEMI          // k_xlabel("Tiempo");
    | YLABELVAG LPAREN STRING RPAREN SEMI          // k_ylabel("Precio");
    | SHOWVAG LPAREN RPAREN SEMI                   // k_show();
    ;