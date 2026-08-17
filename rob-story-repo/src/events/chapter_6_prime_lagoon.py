"""
Глава 6: Праймовая Лагуна
"""

from locations.prime_lagoon import PrimeLagoon
from characters.rob import Rob
from characters.bezlikiy import Bezlikiy

class Chapter6:
    def run(self):
        print("=" * 50)
        print("ГЛАВА 6. ПРАЙМОВАЯ ЛАГУНА")
        print("=" * 50)
        
        print("\nБезликий собрал лучшие версии пиратов...")
        
        lagoon = PrimeLagoon()
        rob = Rob()
        bezlikiy = Bezlikiy()
        
        # Бой с Аквой
        print("\nРоб встречает Акву с дробовиком...")
        print("Роб останавливает пули и разворачивает их...")
        print("Роб ломает дробовик...")
        print("Роб замораживает руку Аквы...")
        print("Роб нагревает Акву — голова взрывается!")
        
        return "lagoon_started"