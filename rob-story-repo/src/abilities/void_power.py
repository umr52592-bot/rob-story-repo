"""
Сила бездны — поглощение и уничтожение.
"""

class VoidPower:
    def __init__(self, user):
        self.user = user
        self.black_hole_active = False
    
    def activate_black_hole(self):
        """Активация чёрной дыры в руке"""
        self.black_hole_active = True
        print("Рука превратилась в чёрную дыру!")
    
    def absorb(self, target):
        """Поглощение объекта"""
        if self.black_hole_active:
            print(f"{target.name} всосан в чёрную дыру!")
            return "absorbed"
        return "failed"