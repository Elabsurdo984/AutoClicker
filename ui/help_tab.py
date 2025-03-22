"""
Componente de pestaña de ayuda para la interfaz del AutoClicker
"""
import tkinter as tk
from tkinter import ttk

def create_help_tab(parent):
    """
    Crea la pestaña de ayuda
    
    Args:
        parent (ttk.Frame): El contenedor padre
    
    Returns:
        None
    """
    help_text = """
    AutoClicker Avanzado - Instrucciones de Uso
    
    Configuración Básica:
    - Intervalo: Tiempo entre clics en segundos
    - Número de clics: Cantidad de clics a realizar (0 = infinito)
    - Tipo de clic: Simple o doble clic
    - Botón: Seleccione qué botón del ratón usar
    
    Configuración Avanzada:
    - Posición: Use la posición actual del cursor o especifique coordenadas
    - Teclas: Personalice las teclas para iniciar/detener
    
    Atajos de teclado:
    - F6 (predeterminado): Iniciar el autoclicker
    - F7 (predeterminado): Detener el autoclicker
    
    Nota: Puede cambiar y guardar su configuración para usos futuros.
    
    Consejos útiles:
    - Para juegos: Use un intervalo más corto y posición personalizada
    - Para formularios: Use un intervalo más largo y clics simples
    - Para seguridad: Use siempre la tecla de parada de emergencia
    """
    
    # Crear un marco con scroll para el texto de ayuda
    help_frame = ttk.Frame(parent)
    help_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Agregar scrollbar
    scrollbar = ttk.Scrollbar(help_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Crear área de texto
    help_text_widget = tk.Text(help_frame, wrap=tk.WORD, height=15, width=50)
    help_text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Configurar scrollbar
    scrollbar.config(command=help_text_widget.yview)
    help_text_widget.config(yscrollcommand=scrollbar.set)
    
    # Insertar texto de ayuda
    help_text_widget.insert(tk.END, help_text.strip())
    help_text_widget.config(state=tk.DISABLED)  # Hacer el texto no editable