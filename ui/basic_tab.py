"""
Componente de pestaña básica para la interfaz del AutoClicker
"""
import tkinter as tk
from tkinter import ttk

def create_basic_tab(parent, click_interval, click_count, click_type, mouse_button, start_callback, stop_callback):
    """
    Crea la pestaña de configuración básica
    
    Args:
        parent (ttk.Frame): El contenedor padre
        click_interval (tk.DoubleVar): Variable para el intervalo de clics
        click_count (tk.IntVar): Variable para el número de clics
        click_type (tk.StringVar): Variable para el tipo de clic
        mouse_button (tk.StringVar): Variable para el botón del ratón
        start_callback (callable): Función para iniciar los clics
        stop_callback (callable): Función para detener los clics
    
    Returns:
        None
    """
    # Intervalo entre clics
    ttk.Label(parent, text="Intervalo entre clics (segundos):").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    scale = ttk.Scale(parent, from_=0.1, to=10.0, variable=click_interval, orient=tk.HORIZONTAL, length=200)
    scale.grid(row=0, column=1, padx=10, pady=10)
    
    # Mostrar valor actual
    interval_value = tk.StringVar()
    
    def update_interval_label(*args):
        interval_value.set(f"{click_interval.get():.1f}")
    
    click_interval.trace_add("write", update_interval_label)
    update_interval_label()  # Inicializar
    
    ttk.Label(parent, textvariable=interval_value).grid(row=0, column=2, padx=10, pady=10)
    
    # Número de clics
    ttk.Label(parent, text="Número de clics (0 = infinito):").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    ttk.Entry(parent, textvariable=click_count, width=10).grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
    
    # Tipo de clic
    ttk.Label(parent, text="Tipo de clic:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    ttk.Radiobutton(parent, text="Clic simple", variable=click_type, value="single").grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
    ttk.Radiobutton(parent, text="Doble clic", variable=click_type, value="double").grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
    
    # Botón del ratón
    ttk.Label(parent, text="Botón del ratón:").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    ttk.Radiobutton(parent, text="Izquierdo", variable=mouse_button, value="left").grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
    ttk.Radiobutton(parent, text="Derecho", variable=mouse_button, value="right").grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
    ttk.Radiobutton(parent, text="Central", variable=mouse_button, value="middle").grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
    
    # Botones de control
    control_frame = ttk.Frame(parent)
    control_frame.grid(row=7, column=0, columnspan=3, pady=20)
    
    start_btn = ttk.Button(control_frame, text="Iniciar", width=15, command=start_callback)
    start_btn.pack(side=tk.LEFT, padx=10)
    
    stop_btn = ttk.Button(control_frame, text="Detener", width=15, command=stop_callback)
    stop_btn.pack(side=tk.LEFT, padx=10)