"""
Funcionalidad principal del AutoClicker
"""
import time
import pyautogui
import threading
from utils.error_handler import handle_error

class Clicker:
    """Clase que maneja la funcionalidad principal del autoclicker"""
    
    def __init__(self, config, status_callback=None):
        """
        Inicializa el clicker con la configuración proporcionada
        
        Args:
            config (dict): Configuración del clicker
            status_callback (callable): Función para actualizar el estado
        """
        self.config = config
        self.status_callback = status_callback
        self.is_running = False
        self.click_thread = None
    
    def update_status(self, message):
        """Actualiza el estado utilizando el callback si está disponible"""
        if self.status_callback:
            self.status_callback(message)
    
    def perform_click(self):
        """Realiza los clics según la configuración"""
        try:
            click_count = self.config.get("click_count", 0)
            interval = self.config.get("click_interval", 1.0)
            click_type = self.config.get("click_type", "single")
            mouse_button = self.config.get("mouse_button", "left")
            position = self.config.get("click_position", "current")
            custom_x = self.config.get("custom_x", 0)
            custom_y = self.config.get("custom_y", 0)
            
            # Actualizar estado
            self.update_status("Estado: Ejecutando clics...")
            
            # Configurar contador
            counter = 0
            max_clicks = click_count if click_count > 0 else float('inf')
            
            while self.is_running and counter < max_clicks:
                try:
                    # Mover a la posición personalizada si está configurado
                    if position == "custom":
                        pyautogui.moveTo(custom_x, custom_y)
                    
                    # Realizar el clic según la configuración
                    if mouse_button == "left":
                        if click_type == "single":
                            pyautogui.click()
                        else:
                            pyautogui.doubleClick()
                    elif mouse_button == "right":
                        pyautogui.rightClick()
                    elif mouse_button == "middle":
                        pyautogui.middleClick()
                    
                    counter += 1
                    
                    # Actualizar estado con contador
                    if click_count > 0:
                        self.update_status(f"Estado: Ejecutando clics... ({counter}/{click_count})")
                    else:
                        self.update_status(f"Estado: Ejecutando clics... ({counter})")
                    
                    # Pausar según el intervalo
                    time.sleep(interval)
                except Exception as e:
                    handle_error(e, "Error al realizar clic")
                    self.stop()
                    break
            
            # Si terminó los clics sin ser detenido
            if counter >= max_clicks and self.is_running:
                self.stop()
                self.update_status(f"Estado: Completado ({counter} clics)")
                
        except Exception as e:
            handle_error(e, "Error en el proceso de clics")
            self.stop()
    
    def start(self):
        """Inicia el proceso de clics en un hilo separado"""
        if not self.is_running:
            self.is_running = True
            self.click_thread = threading.Thread(target=self.perform_click)
            self.click_thread.daemon = True
            self.click_thread.start()
            return True
        return False
    
    def stop(self):
        """Detiene el proceso de clics"""
        if self.is_running:
            self.is_running = False
            self.click_thread = None
            self.update_status("Estado: Detenido")
            return True
        return False
    
    def capture_current_position(self):
        """
        Captura la posición actual del cursor
        
        Returns:
            tuple: Coordenadas (x, y) de la posición actual
        """
        x, y = pyautogui.position()
        return (x, y)