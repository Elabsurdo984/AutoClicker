# AutoClicker Avanzado

Un programa de autoclicker potente y flexible con interfaz gráfica para automatizar clics del ratón.

## Características

- **Control preciso**: Configura intervalos personalizados entre clics (de 0.1 a 10 segundos)
- **Versatilidad**: Soporta clic simple, doble clic y diferentes botones del ratón (izquierdo, derecho, central)
- **Posicionamiento**: Opera en la posición actual del cursor o en coordenadas específicas
- **Personalización**: Configura teclas de acceso rápido para iniciar/detener
- **Persistencia**: Guarda tu configuración para usos futuros
- **Interfaz intuitiva**: Diseño con pestañas para fácil navegación

## Requisitos

- Python 3.6 o superior
- Dependencias:
  - pyautogui
  - keyboard
  - tkinter (generalmente incluido con Python)

## Instalación

1. Clona o descarga este repositorio:

```bash
git clone https://github.com/tu-usuario/autoclicker-avanzado.git
cd autoclicker-avanzado
```

2. Ejecuta el programa:

```bash
python main.py
```

El programa verificará e instalará automáticamente las dependencias necesarias si no están presentes.

## Uso

### Configuración Básica

- **Intervalo entre clics**: Define el tiempo de espera entre clics (en segundos)
- **Número de clics**: Establece cuántos clics realizar (0 = infinito)
- **Tipo de clic**: Elige entre clic simple o doble clic
- **Botón del ratón**: Selecciona qué botón usar (izquierdo, derecho o central)

### Configuración Avanzada

- **Posición de clic**: 
  - Usa la posición actual del cursor mientras se ejecuta
  - Define coordenadas específicas en la pantalla
  - Captura la posición actual con el botón "Capturar posición actual"
- **Teclas de acceso rápido**:
  - Personaliza las teclas para iniciar/detener (predeterminadas: F6/F4)

### Controles Principales

- **Iniciar**: Comienza el proceso de clics automáticos
- **Detener**: Finaliza el proceso
- **Guardar configuración**: Almacena la configuración actual para usos futuros

## Atajos de Teclado

- **F6** (predeterminado): Inicia el autoclicker
- **F4** (predeterminado): Detiene el autoclicker

> Nota: Puedes personalizar estas teclas en la pestaña "Configuración Avanzada".

## Consejos de Uso

- **Para juegos**: Usa un intervalo corto y posición personalizada
- **Para formularios**: Configura un intervalo más largo y clics simples
- **Para tareas repetitivas**: Usa el número infinito de clics (0) para operaciones continuas
- **Para seguridad**: Familiarízate con la tecla de detención antes de iniciar

## Estructura del Proyecto

```
autoclicker/
├── core/
│   └── clicker.py       # Funcionalidad principal
├── ui/
│   ├── app.py           # Aplicación principal
│   ├── basic_tab.py     # Interfaz configuración básica
│   ├── advanced_tab.py  # Interfaz configuración avanzada
│   └── help_tab.py      # Pestaña de ayuda
├── utils/
│   ├── config_manager.py # Gestión de configuración
│   └── error_handler.py  # Manejo de errores
├── main.py              # Punto de entrada
├── README.md            # Info de la aplicacion
└── requirements.txt     # Dependencias
```

## Solución de Problemas

Si experimentas problemas:

1. Verifica que todas las dependencias estén instaladas correctamente
2. Comprueba el archivo de registro `autoclicker_error.log` para detalles de errores
3. Asegúrate de tener permisos adecuados para controlar el ratón

## Limitaciones

- El programa necesita permisos de accesibilidad en macOS y algunos entornos Linux
- Algunas aplicaciones o juegos pueden tener medidas anti-bot que bloqueen autoclickers
- Las teclas de función pueden estar reservadas por el sistema en algunos entornos

## Licencia

[MIT](LICENSE) - Siéntete libre de usar, modificar y distribuir este software.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.