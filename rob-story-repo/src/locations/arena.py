"""
Арена — начальная локация.
Место первого боя и стирания памяти.
"""

from characters.monsters import Gradul, Colossus

class Arena:
    def __init__(self):
        self.name = "Арена"
        self.sand = True
        self.crowd = []
        self.spectators_count = 0
    
    def fight(self, rob):
        """Бой на арене"""
        print("Роб выходит на арену...")
        
        # Первый бой
        gradul = Gradul()
        result = rob.fight(gradul)
        
        if result == "victory":
            print("Толпа замолкает...")
            # Безликий вмешивается
            from characters.bezlikiy import Bezlikiy
            bezlikiy = Bezlikiy()
            bezlikiy.inject_memory_serum(rob)
            return "memory_wiped"
        
        # Второй бой (после петли)
        colossus = Colossus()
        result = rob.fight(colossus)
        
        if result == "escape":
            print("Роб сбегает с арены!")
            return "escape"
    
    def roar_crowd(self):
        """Рёв толпы"""
        print("Толпа ревёт! АААА!")