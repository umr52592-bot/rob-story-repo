"""
Белый Куб — тюрьма бога.
Место стирания памяти и бесконечных циклов.
"""

class WhiteCube:
    def __init__(self):
        self.name = "Белый Куб"
        self.color = "white"
        self.corridors = "infinite"
        self.is_prison = True
        self.prisoners = []
    
    def imprison(self, target):
        """Заключение в тюрьму"""
        self.prisoners.append(target)
        print(f"{target.name} заключён в Белый Куб")
    
    def erase_memory(self, target):
        """Стирание памяти"""
        target.memory = []
        target.is_amnesiac = True
        target.iteration += 1
        print(f"Память {target.name} стёрта. Итерация {target.iteration}")
    
    def patrol(self):
        """Патрулирование коридоров"""
        from characters.servants import LeglessCreature, ShapelessEntity
        print("По коридорам бродят слуги...")
        return [LeglessCreature(), ShapelessEntity()]
    
    def turn_black(self):
        """Превращение в Чёрный Куб"""
        from .black_cube import BlackCube
        print("Куб начинает чернеть...")
        return BlackCube()