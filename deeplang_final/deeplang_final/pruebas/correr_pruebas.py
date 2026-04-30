#!/usr/bin/env python3
"""
Ejecuta todos los programas de ejemplo y reporta cuales pasan.
Uso: python3 pruebas/correr_pruebas.py
"""
import subprocess
import sys
import os

RAIZ      = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRAMAS = os.path.join(RAIZ, 'programas')
MAIN      = os.path.join(RAIZ, 'ejecucion', 'main.py')

archivos = sorted(f for f in os.listdir(PROGRAMAS) if f.endswith('.dl'))

pasados = 0
fallidos = []

for archivo in archivos:
    ruta = os.path.join(PROGRAMAS, archivo)
    resultado = subprocess.run(
        [sys.executable, MAIN, ruta],
        capture_output=True, text=True
    )
    if resultado.returncode == 0:
        print(f"[OK]  {archivo}")
        pasados += 1
    else:
        print(f"[FALLO] {archivo}")
        print(resultado.stderr.strip())
        fallidos.append(archivo)

print(f"\n{pasados}/{len(archivos)} programas pasaron")
if fallidos:
    print("Fallidos:", fallidos)
    sys.exit(1)
