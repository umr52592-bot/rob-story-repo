"""
Глава 11: Финал. Тюрьма Бога
"""

from locations.prison_of_god import PrisonOfGod
from characters.bezlikiy import Bezlikiy

class Chapter11:
    def run(self):
        print("=" * 50)
        print("ГЛАВА 11. ФИНАЛ. ТЮРЬМА БОГА")
        print("=" * 50)
        
        prison = PrisonOfGod()
        bezlikiy = Bezlikiy()
        
        print("\nВ Тюрьме Бога сидели ??? и Безликий...")
        print("Они ждали результата...")
        
        print("\nКоридоры начали чернеть...")
        print("Появились фиолетовые улыбки...")
        
        print("\n??? исчез...")
        print("Безликий рассыпался в пыль!")
        
        prison.shatter()
        
        return "god_prison_destroyed"