"""
AutoClicker Avanzado - Programa principal
"""
import sys
import subprocess
import importlib.util
import tkinter as tk
from ui.app import AutoClickerApp

def check_dependencies():
    """Verifica e instala las dependencias necesarias"""
    required_packages = ['pyautogui', 'keyboard']
    missing_packages = []
    
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Instalando dependencias faltantes: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
            print("Dependencias instaladas correctamente.")
        except subprocess.CalledProcessError:
            print("Error al instalar dependencias. Por favor, instale manualmente:")
            print(f"pip install {' '.join(missing_packages)}")
            sys.exit(1)

def main():
    """Función principal que inicia la aplicación"""
    # Verificar dependencias
    check_dependencies()
    
    # Iniciar aplicación
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()