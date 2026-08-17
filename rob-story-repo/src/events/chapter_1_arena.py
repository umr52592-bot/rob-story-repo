"""
Глава 1: Арена
"""

from locations.arena import Arena
from characters.rob import Rob
from characters.bezlikiy import Bezlikiy

class Chapter1:
    def run(self):
        print("=" * 50)
        print("ГЛАВА 1. АРЕНА")
        print("=" * 50)
        
        rob = Rob()
        arena = Arena()
        bezlikiy = Bezlikiy()
        
        # Бой с Градулом
        print("\nРоб просыпается в камере...")
        print("Его выводят на бой против Градула!")
        
        result = arena.fight(rob)
        
        # Встреча с Безликим
        print("\nИз тени появляется Безликий...")
        bezlikiy.inject_memory_serum(rob)
        
        # Новый бой
        print("\nПетля. Новый бой...")
        print("Роб снова просыпается в камере...")
        
        return result