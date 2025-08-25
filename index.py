# Importamos la clase Pantalla desde el módulo de configuración
# Aquí se supone que Pantalla contiene los parámetros principales de la ventana o interfaz
from config.configuracion import Pantalla  

# Importamos la clase Enrutador desde la carpeta src
# El Enrutador se encargará de manejar las rutas, vistas o la lógica central del programa
from src.enrutador import Enrutador  


# Punto de entrada principal del programa
if __name__ == "__main__":
    # Creamos una instancia de la clase Enrutador, pasándole como parámetro la configuración de Pantalla
    enrutador = Enrutador(Pantalla)

    # Llamamos al método ejecutar(), que inicia el flujo principal del programa
    enrutador.ejecutar()
