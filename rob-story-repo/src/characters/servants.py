"""
Слуги Безликого.
"""

class LeglessCreature:
    """Существо без ног с руками-когтями"""
    def __init__(self):
        self.name = "Существо без ног"
        self.legs = 0
        self.claws = True
    
    def attack(self):
        print("Существо без ног атакует когтями!")

class ShapelessEntity:
    """Существо с неразличимым силуэтом"""
    def __init__(self):
        self.name = "Неразличимое существо"
        self.silhouette = "неразличим"
    
    def stalk(self):
        print("Неразличимое существо следит...")