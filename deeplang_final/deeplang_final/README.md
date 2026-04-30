# DeepLang

DSL funcional para computacion numerica y aprendizaje automatico.
Implementado con ANTLRv4 y Python usando el patron Visitor.
Sin dependencias externas: todo implementado manualmente.

## Instalacion rapida

```bash
bash herramientas/instalar.sh
```

Esto instala el runtime de ANTLR4, descarga el generador y construye el parser.

## Ejecutar programas

```bash
python3 ejecucion/main.py programas/aritmetica.dl
python3 ejecucion/main.py programas/tableros.dl
python3 ejecucion/main.py programas/formas.dl
python3 ejecucion/main.py programas/modulos.dl
python3 ejecucion/main.py programas/regresion.dl
python3 ejecucion/main.py programas/grafica.dl
```

## Correr todas las pruebas

```bash
python3 pruebas/correr_pruebas.py
```

## Estructura del proyecto

```
deeplang/
├── lenguaje/
│   ├── gramatica/
│   │   ├── DeepLang.g4              <- Gramatica formal
│   │   └── generated/            <- Generado por ANTLR (no editar)
│   ├── interprete/
│   │   ├── visitor.py            <- Evaluador
│   │   ├── entorno.py            <- Tabla de simbolos
│   │   └── errores.py            <- Manejo de errores
│   └── runtime/
│       ├── matematica.py         <- Funciones matematicas manuales
│       ├── matrices.py           <- Operaciones matriciales manuales
│       └── modulos.py            <- Definicion de modulos del lenguaje
├── ejecucion/
│   └── main.py                   <- Punto de entrada
├── programas/                    <- Programas .dl de ejemplo
├── pruebas/
│   └── correr_pruebas.py
└── herramientas/
    └── instalar.sh
```

## Sintaxis de DeepLang

```
-- comentario de linea
{- comentario de bloque -}

-- Enlace de valores
fijar x <- 42
fijar nombre <- "DeepLang"

-- Tableros (matrices)
fijar A <- [[1, 2], [3, 4]]

-- Formas (funciones)
forma cuadrado { n } -> n ^ 2
forma distancia { x1 y1 x2 y2 } -> nucleo::raiz((x2-x1)^2 + (y2-y1)^2)

-- Modulos
traer nucleo
traer algebra ~> al          -- con alias
desde nucleo tomar { sen, cos }

-- Invocacion
nucleo::emitir(cuadrado(5))
al::mostrar(al::transponer(A))

-- Operadores de tablero
A [+] B    -- suma
A [-] B    -- resta
A [*] B    -- multiplicacion
```

## Modulos disponibles

| Modulo       | Funciones principales                                      |
|--------------|------------------------------------------------------------|
| `nucleo`     | emitir, sen, cos, tan, raiz, raizn, abs, exp, ln, pi, e   |
| `algebra`    | transponer, invertir, mostrar, dim, sumar, restar, multiplicar |
| `estadistica`| ajustar, predecir, error_mse, media, varianza, desviacion  |
| `salida`     | imprimir, linea, rotulo, tablero                           |
| `grafica`    | histograma, dispersion                                     |
