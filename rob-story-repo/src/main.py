"""
Главный модуль системы.
Запускает нарративный движок и управляет потоком событий.
"""

from characters.rob import Rob
from characters.bezlikiy import Bezlikiy
from locations.arena import Arena
from locations.white_cube import WhiteCube
from locations.black_cube import BlackCube
from locations.prime_lagoon import PrimeLagoon
from events import *

class NarrativeEngine:
    def __init__(self):
        self.rob = Rob()
        self.bezlikiy = Bezlikiy()
        self.current_location = None
        self.cycle_count = 0
    
    def start(self):
        """Запуск основного цикла"""
        print("Инициализация системы...")
        self.run_arena_cycle()
    
    def run_arena_cycle(self):
        """Цикл арены — стирание и перезапуск"""
        arena = Arena()
        result = arena.fight(self.rob)
        
        if result == "memory_wiped":
            self.cycle_count += 1
            self.bezlikiy.intervene()
            self.run_white_cube_phase()
    
    def run_white_cube_phase(self):
        """Фаза Белого Куба"""
        cube = WhiteCube()
        cube.imprison(self.rob)
        cube.erase_memory(self.rob)
    
    def run_black_cube_phase(self):
        """Фаза Чёрного Куба — пробуждение"""
        cube = BlackCube()
        cube.awaken(self.rob)
        cube.unleash_shadow_magic(self.rob)
    
    def run_prime_lagoon_phase(self):
        """Финальная битва"""
        lagoon = PrimeLagoon()
        lagoon.battle(self.rob, self.bezlikiy)

if __name__ == "__main__":
    engine = NarrativeEngine()
    engine.start()