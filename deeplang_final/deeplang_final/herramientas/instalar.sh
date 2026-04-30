#!/usr/bin/env bash
# Instala dependencias y genera el parser desde la gramatica.
# Ejecutar desde la raiz del proyecto: bash herramientas/instalar.sh

set -e

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
GRAM="$RAIZ/lenguaje/gramatica"
JAR="$GRAM/antlr4.jar"
GEN="$GRAM/generated"

echo "-- Instalando runtime de ANTLR4 para Python..."
pip3 install antlr4-python3-runtime==4.13.1

echo "-- Descargando generador ANTLR4..."
wget -q https://www.antlr.org/download/antlr-4.13.1-complete.jar -O "$JAR"

echo "-- Generando parser..."
mkdir -p "$GEN"
java -jar "$JAR" -Dlanguage=Python3 -visitor -o "$GEN" "$GRAM/DeepLang.g4"
touch "$GEN/__init__.py"

echo "-- Listo. Ejecuta un programa con:"
echo "   python3 ejecucion/main.py programas/aritmetica.dl"
