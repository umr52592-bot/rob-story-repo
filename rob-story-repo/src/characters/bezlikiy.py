"""
Безликий — главный антагонист.
Существо без головы, управляющее циклами памяти.
"""

class Bezlikiy:
    def __init__(self):
        self.name = "Безликий"
        self.has_head = False
        self.can_teleport = True
        self.hive_mind = True
        self.iteration = 0
    
    def intervene(self):
        """Вмешательство в цикл"""
        self.iteration += 1
        print(f"Безликий вмешался. Итерация {self.iteration}")
    
    def inject_memory_serum(self, target):
        """Впрыскивание сыворотки"""
        print("Безликий впрыскивает сыворотку")
        target.memory = []
        target.is_amnesiac = True
    
    def teleport(self, location):
        """Телепортация"""
        print(f"Безликий телепортируется в {location}")
        return location
    
    def summon_servants(self):
        """Призыв слуг"""
        from .servants import LeglessCreature, ShapelessEntity
        return [LeglessCreature(), ShapelessEntity()]
    
    def destroy(self):
        """Уничтожение Безликого"""
        print("Безликий рассыпается в пыль...")
        return "dust"