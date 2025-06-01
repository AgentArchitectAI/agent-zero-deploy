#!/bin/bash
export PYTHONUNBUFFERED=1
export PORT=${PORT:-5000}  # Railway define PORT automáticamente

# Reemplaza con el script correcto si usas otro
python run_ui.py