"""
Устройство возврата памяти — артефакт пиратов.
"""

class MemoryDevice:
    def __init__(self):
        self.name = "Устройство возврата памяти"
        self.is_functional = True
        self.charge = 100
    
    def activate(self, target):
        """Активация устройства"""
        print("Устройство запущено...")
        self.charge -= 10
        
        if self.charge > 0:
            print("Память начинает возвращаться...")
            return "restoring"
        else:
            print("Устройство замедляется...")
            return "failing"