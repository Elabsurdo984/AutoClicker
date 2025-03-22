"""
Manejo de errores para AutoClicker
"""
import traceback
import logging
from tkinter import messagebox

# Configurar logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="autoclicker_error.log"
)

logger = logging.getLogger("AutoClicker")

def handle_error(error, message="Se produjo un error en la aplicación"):
    """
    Maneja errores mostrando un mensaje y registrando el error
    
    Args:
        error (Exception): La excepción producida
        message (str): Mensaje a mostrar al usuario
    
    Returns:
        None
    """
    error_details = traceback.format_exc()
    logger.error(f"{message}: {str(error)}\n{error_details}")
    messagebox.showerror("Error", f"{message}:\n{str(error)}")

def show_warning(message):
    """
    Muestra una advertencia al usuario
    
    Args:
        message (str): Mensaje de advertencia
    
    Returns:
        None
    """
    logger.warning(message)
    messagebox.showwarning("Advertencia", message)