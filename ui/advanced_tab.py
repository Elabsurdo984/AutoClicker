"""
Componente de pestaña avanzada para la interfaz del AutoClicker
"""
import tkinter as tk
from tkinter import ttk

def create_advanced_tab(
    parent, 
    click_position, 
    custom_x, 
    custom_y, 
    start_key, 
    stop_key, 
    capture_callback, 
    update_hotkeys_callback, 
    save_callback
):
    """
    Crea la pestaña de configuración avanzada
    
    Args:
        parent (ttk.Frame): El contenedor padre
        click_position (tk.StringVar): Variable para la posición del clic
        custom_x (tk.IntVar): Variable para la coordenada X personalizada
        custom_y (tk.IntVar): Variable para la coordenada Y personalizada
        start_key (tk.StringVar): Variable para la tecla de inicio
        stop_key (tk.StringVar): Variable para la tecla de detención
        capture_callback (callable): Función para capturar la posición
        update_hotkeys_callback (callable): Función para actualizar teclas
        save_callback (callable): Función para guardar la configuración
    
    Returns:
        None
    """
    # Posición de clic
    ttk.Label(parent, text="Posición de clic:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    ttk.Radiobutton(
        parent, 
        text="Posición actual del cursor", 
        variable=click_position, 
        value="current"
    ).grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
    
    ttk.Radiobutton(
        parent, 
        text="Posición personalizada", 
        variable=click_position, 
        value="custom"
    ).grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
    
    # Coordenadas personalizadas
    coords_frame = ttk.Frame(parent)
    coords_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
    
    ttk.Label(coords_frame, text="X:").pack(side=tk.LEFT, padx=5)
    ttk.Entry(coords_frame, textvariable=custom_x, width=6).pack(side=tk.LEFT, padx=5)
    
    ttk.Label(coords_frame, text="Y:").pack(side=tk.LEFT, padx=5)
    ttk.Entry(coords_frame, textvariable=custom_y, width=6).pack(side=tk.LEFT, padx=5)
    
    # Botón de captura
    ttk.Button(
        parent, 
        text="Capturar posición actual", 
        command=capture_callback
    ).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    # Teclas de acceso rápido
    ttk.Label(parent, text="Tecla para iniciar:").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    
    function_keys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]
    
    start_key_combo = ttk.Combobox(parent, textvariable=start_key, values=function_keys, state="readonly")
    start_key_combo.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)
    start_key_combo.bind("<<ComboboxSelected>>", lambda e: update_hotkeys_callback())
    
    ttk.Label(parent, text="Tecla para detener:").grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
    
    stop_key_combo = ttk.Combobox(parent, textvariable=stop_key, values=function_keys, state="readonly")
    stop_key_combo.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)
    stop_key_combo.bind("<<ComboboxSelected>>", lambda e: update_hotkeys_callback())
    
    # Botón de guardar
    ttk.Button(
        parent, 
        text="Guardar configuración", 
        command=save_callback
    ).grid(row=6, column=0, columnspan=2, padx=10, pady=20)