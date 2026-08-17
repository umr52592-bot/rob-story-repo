"""
Чёрный Куб — место пробуждения Роба.
Здесь активируется магия теней.
"""

class BlackCube:
    def __init__(self):
        self.name = "Чёрный Куб"
        self.color = "black"
        self.has_purple_smiles = True
        self.is_cracked = False
    
    def awaken(self, rob):
        """Пробуждение силы"""
        print("Изнутри куба доносится голос: 'Я ВСЕГДА ВОЗВРАЩАЮСЬ!'")
        self.is_cracked = True
        rob.awaken_shadow()
        print("Роб вышел из Чёрного Куба с чёрными глазами!")
    
    def unleash_shadow_magic(self, rob):
        """Высвобождение магии теней"""
        rob.has_shadow_power = True
        print("Магия теней и бездны активирована!")