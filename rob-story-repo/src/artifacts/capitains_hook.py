"""
Крюк Капитана — артефакт для активации сплава.
"""

class CaptainsHook:
    def __init__(self, owner):
        self.name = "Крюк Капитана"
        self.owner = owner
    
    def activate_alloy(self, alloy):
        """Активация сплава"""
        print("Капитан активирует сплав своим крюком!")
        alloy.activate()