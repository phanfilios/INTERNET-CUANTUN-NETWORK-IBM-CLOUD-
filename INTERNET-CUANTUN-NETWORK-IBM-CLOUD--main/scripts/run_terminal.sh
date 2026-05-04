#!/bin/bash
# Script para ejecutar la terminal cuántica

cd "$(dirname "$0")/.."

# Verificar si existe entorno virtual
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Instalar dependencias si faltan
pip install -q rich prompt-toolkit psutil 2>/dev/null

# Ejecutar terminal
python scripts/quantum_terminal.py