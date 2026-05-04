# Script para ejecutar la terminal cuántica en Windows
Set-Location $PSScriptRoot\..

# Verificar si existe entorno virtual
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
}

# Instalar dependencias si faltan
pip install -q rich prompt-toolkit psutil 2>$null

# Ejecutar terminal
python scripts\quantum_terminal.py