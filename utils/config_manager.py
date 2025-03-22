"""
Gestión de configuración para AutoClicker
"""
import os
import json
from tkinter import messagebox

DEFAULT_CONFIG = {
    "click_interval": 1.0,
    "click_count": 0,
    "click_type": "single",
    "mouse_button": "left",
    "click_position": "current",
    "custom_x": 0,
    "custom_y": 0,
    "start_key": "F6",
    "stop_key": "F4"
}

CONFIG_FILE = "autoclicker_config.json"

def save_config(config):
    """
    Guarda la configuración en un archivo JSON
    
    Args:
        config (dict): Diccionario con la configuración a guardar
    
    Returns:
        bool: True si se guardó correctamente, False en caso contrario
    """
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la configuración: {str(e)}")
        return False

def load_config():
    """
    Carga la configuración desde un archivo JSON
    
    Returns:
        dict: Diccionario con la configuración cargada o la configuración por defecto
    """
    config = DEFAULT_CONFIG.copy()
    
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                loaded_config = json.load(f)
                
            # Actualizar solo las claves existentes
            for key in config:
                if key in loaded_config:
                    config[key] = loaded_config[key]
    except Exception as e:
        print(f"Error al cargar la configuración: {e}")
    
    return config