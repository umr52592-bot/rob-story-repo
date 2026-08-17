"""
Нитрино-бомба — оружие против братьев-червей.
"""

class NitrinoBomb:
    def __init__(self):
        self.name = "Нитрино-бомба"
        self.power = 1000
    
    def detonate(self, target):
        """Взрыв"""
        print(f"Нитрино-бомба засунута в сердечник {target.name}!")
        print("ВЗРЫВ!")
        return self.destroy(target)
    
    def destroy(self, target):
        """Уничтожение цели"""
        print(f"От {target.name} остались только шлем и расколотый нагрудник")
        return "obliterated"