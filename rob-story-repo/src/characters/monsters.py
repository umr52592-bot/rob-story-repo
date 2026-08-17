"""
Монстры и противники Роба.
"""

class Gradul:
    """Каменный голем"""
    def __init__(self):
        self.name = "Градул"
        self.material = "stone"
        self.leg = "short"
        self.arms = "mismatched"
        self.core = "chest_mechanism"
    
    def exploit_weakness(self):
        """Использование слабости"""
        print("Роб использует слабость Градула!")
        print("Роб втыкает обломок меча в механизм в груди")
        self.destroy()
    
    def destroy(self):
        """Разрушение"""
        print("Градул бьётся головой о стену и рассыпается!")

class Colossus:
    """Огромный живой робот"""
    def __init__(self):
        self.name = "Колос"
        self.material = "steel"
        self.core = "blue_light"
        self.can_speak = True
    
    def self_destruct(self):
        """Самоуничтожение для спасения Роба"""
        print("Колос отрывает себе голову и подбрасывает в воздух")
        print("Колос уничтожен, чтобы не выдать след Роба")