from config.configuracion import Pantalla
from src.enrutador import Enrutador

if __name__ == "__main__":
    enrutador= Enrutador(Pantalla)
    enrutador.ejecutar()
