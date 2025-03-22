"""
Aplicación principal del AutoClicker con interfaz gráfica
"""
import tkinter as tk
import keyboard
from core.clicker import Clicker
from utils.config_manager import load_config, save_config
from ui.basic_tab import create_basic_tab
from ui.advanced_tab import create_advanced_tab
from ui.help_tab import create_help_tab

class AutoClickerApp:
    """Clase principal para la aplicación AutoClicker"""
    
    def __init__(self, root):
        """
        Inicializa la aplicación AutoClicker
        
        Args:
            root (tk.Tk): La ventana raíz de tkinter
        """
        self.root = root
        self.root.title("AutoClicker Avanzado")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Variables de estado
        self.config = load_config()
        self.clicker = Clicker(self.config, self.update_status)
        
        # Variables de tkinter
        self.create_variables()
        
        # Crear interfaz
        self.create_ui()
        
        # Configurar teclas globales
        self.setup_hotkeys()
    
    def create_variables(self):
        """Crea las variables de tkinter y las inicializa con los valores de configuración"""
        self.click_interval = tk.DoubleVar(value=self.config["click_interval"])
        self.click_count = tk.IntVar(value=self.config["click_count"])
        self.click_type = tk.StringVar(value=self.config["click_type"])
        self.mouse_button = tk.StringVar(value=self.config["mouse_button"])
        self.click_position = tk.StringVar(value=self.config["click_position"])
        self.custom_x = tk.IntVar(value=self.config["custom_x"])
        self.custom_y = tk.IntVar(value=self.config["custom_y"])
        self.start_key = tk.StringVar(value=self.config["start_key"])
        self.stop_key = tk.StringVar(value=self.config["stop_key"])
        self.status_var = tk.StringVar(value="Estado: Listo")
    
    def create_ui(self):
        """Crea la interfaz de usuario principal"""
        # Notebook para organizar configuraciones
        self.notebook = tk.ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear pestañas
        self.basic_tab = tk.ttk.Frame(self.notebook)
        self.advanced_tab = tk.ttk.Frame(self.notebook)
        self.help_tab = tk.ttk.Frame(self.notebook)
        
        self.notebook.add(self.basic_tab, text="Configuración Básica")
        self.notebook.add(self.advanced_tab, text="Configuración Avanzada")
        self.notebook.add(self.help_tab, text="Ayuda")
        
        # Crear contenido de las pestañas
        create_basic_tab(
            self.basic_tab, 
            self.click_interval, 
            self.click_count, 
            self.click_type, 
            self.mouse_button, 
            self.start_clicking, 
            self.stop_clicking
        )
        
        create_advanced_tab(
            self.advanced_tab, 
            self.click_position, 
            self.custom_x, 
            self.custom_y, 
            self.start_key, 
            self.stop_key,
            self.capture_position, 
            self.update_hotkeys, 
            self.save_current_config
        )
        
        create_help_tab(self.help_tab)
        
        # Estado actual
        status_label = tk.ttk.Label(self.root, textvariable=self.status_var, font=("Arial", 10, "bold"))
        status_label.pack(side=tk.BOTTOM, pady=5)
    
    def update_status(self, message):
        """Actualiza el mensaje de estado"""
        self.status_var.set(message)
    
    def setup_hotkeys(self):
        """Configura las teclas de acceso rápido"""
        keyboard.unhook_all()
        keyboard.add_hotkey(self.start_key.get().lower(), self.start_clicking)
        keyboard.add_hotkey(self.stop_key.get().lower(), self.stop_clicking)
    
    def update_hotkeys(self):
        """Actualiza las teclas de acceso rápido según la configuración"""
        self.setup_hotkeys()
    
    def start_clicking(self):
        """Inicia el proceso de clics"""
        # Actualizar la configuración con los valores actuales
        self.update_config_from_ui()
        self.clicker.config = self.config
        self.clicker.start()
    
    def stop_clicking(self):
        """Detiene el proceso de clics"""
        self.clicker.stop()
    
    def capture_position(self):
        """Captura la posición actual del cursor"""
        self.root.iconify()  # Minimizar la ventana
        import time
        time.sleep(2)  # Dar tiempo al usuario para posicionar el cursor
        x, y = self.clicker.capture_current_position()
        self.custom_x.set(x)
        self.custom_y.set(y)
        self.click_position.set("custom")
        self.root.deiconify()  # Restaurar la ventana
        tk.messagebox.showinfo("Posición capturada", f"Posición capturada: X={x}, Y={y}")
    
    def update_config_from_ui(self):
        """Actualiza la configuración con los valores actuales de la interfaz"""
        self.config["click_interval"] = self.click_interval.get()
        self.config["click_count"] = self.click_count.get()
        self.config["click_type"] = self.click_type.get()
        self.config["mouse_button"] = self.mouse_button.get()
        self.config["click_position"] = self.click_position.get()
        self.config["custom_x"] = self.custom_x.get()
        self.config["custom_y"] = self.custom_y.get()
        self.config["start_key"] = self.start_key.get()
        self.config["stop_key"] = self.stop_key.get()
    
    def save_current_config(self):
        """Guarda la configuración actual"""
        self.update_config_from_ui()
        if save_config(self.config):
            tk.messagebox.showinfo("Configuración", "Configuración guardada correctamente")