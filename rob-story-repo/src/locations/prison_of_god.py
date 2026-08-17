"""
Тюрьма Бога — финальная локация.
Здесь уничтожается порядок.
"""

class PrisonOfGod:
    def __init__(self):
        self.name = "Тюрьма Бога"
        self.contained = []
        self.is_shattered = False
    
    def contain(self, entity):
        """Заключение сущности"""
        self.contained.append(entity)
        print(f"{entity.name} заключён в Тюрьму Бога")
    
    def shatter(self):
        """Разрушение тюрьмы"""
        self.is_shattered = True
        print("Тюрьма Бога разрушена!")
        print("Фиолетовые улыбки расцвели на стенах реальности")