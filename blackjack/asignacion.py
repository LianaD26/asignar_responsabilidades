class Carta:
    def __init__(self, pinta: str, valor: int):
        self.pinta: str = pinta
        self.valor: int = valor
        self.tapada: bool = False

class Mano:
    def __init__(self, cartas: list):
        self.cartas: list[Carta] = []

    def es_blackjack(self) -> bool:
        pass
    def verificar_mano_jugador(self):
        pass
    def verificar_mano_casa(self):
        pass

class Baraja:
    def __init__(self):
        self.cartas: list[Carta] = []

    def revolver(self):
        pass
    def repartir_carta(self, tapada: bool) -> Carta:
        pass
class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas
        self.mano: Mano = None
    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass

    def seleccionar_jugada(self):
        pass

    def recibir_carta(self, cartas: tuple[Carta, Carta]):
        pass
    def duplicar_fichas(self):
        pass
    def restar_fichas(self):
        pass
    def verificar_tiene_fichas(self) -> bool:
        pass
    def verificar_cartas(self):
        pass

class Casa:
    def __init__(self):
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass
    def mostrar_menu(self):
        pass
class Blackjack:
    def __init__(self):
        self.baraja: Baraja = None
        self.jugador: Jugador = None
        self.cupier: Casa = None
    def registrar_jugador(self, nombre: str):
        pass
    def iniciar_juego(self, apuesta: int):
        pass
    def destapar_carta(self):
        pass
    def verificar_ganador(self) -> bool:
        pass
    def verificar_empate(self) -> bool:
        pass