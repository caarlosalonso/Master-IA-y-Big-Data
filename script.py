import sys
import subprocess

print("=== Verificación de Instalación Python ===\n")

# 1. Versión de Python
print(f"Versión Python: {sys.version}")
print(f"Ejecutable: {sys.executable}\n")

# 2. PATH
import os
python_in_path = any("Python" in p for p in os.environ["PATH"].split(os.pathsep))
print(f"Python en PATH: {'✓ Sí' if python_in_path else '✗ No'}\n")

# 3. pip
try:
    result = subprocess.run(["pip", "--version"], capture_output=True, text=True)
    print(f"pip: ✓ {result.stdout.strip()}\n")
except FileNotFoundError:
    print("pip: ✗ No encontrado\n")

# 4. Paquetes esenciales
paquetes = ["numpy", "pandas", "matplotlib", "jupyter"]
print("Paquetes instalados:")
for pkg in paquetes:
    try:
        __import__(pkg)
        print(f"  ✓ {pkg}")
    except ImportError:
        print(f"  ✗ {pkg} (ejecutar: pip install {pkg})")

print("\n=== Verificación completada ===")