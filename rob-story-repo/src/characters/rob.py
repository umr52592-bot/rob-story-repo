"""
Главный персонаж — Роб.
Обладает способностью к эволюции и возвращению после смерти.
"""

class Rob:
    def __init__(self):
        self.name = "Роб"
        self.memory = []
        self.is_amnesiac = True
        self.has_shadow_power = False
        self.eyes = "normal"
        self.is_king = False
        self.iteration = 0
    
    def fight(self, opponent):
        """Сражается с противником"""
        if opponent.name == "Градул":
            return self._defeat_gradul(opponent)
        elif opponent.name == "Колос":
            return self._escape_colossus(opponent)
        elif opponent.name == "Хелл":
            return self._defeat_hell(opponent)
        elif opponent.name == "Роваам":
            return self._defeat_rovaam(opponent)
        else:
            return self._generic_fight(opponent)
    
    def _defeat_gradul(self, gradul):
        """Победа над Градулом"""
        gradul.exploit_weakness()
        return "victory"
    
    def _escape_colossus(self, colossus):
        """Побег от Колоса"""
        colossus.self_destruct()
        return "escape"
    
    def _defeat_hell(self, hell):
        """Победа над Хеллом"""
        hell.fall_into_void()
        return "victory"
    
    def _defeat_rovaam(self, rovaam):
        """Победа над Роваамом"""
        rovaam.corrupt_with_darkness()
        return "victory"
    
    def awaken_shadow(self):
        """Пробуждение магии теней"""
        self.has_shadow_power = True
        self.eyes = "black_with_purple"
        print("Роб пробудил магию теней!")
    
    def become_king(self):
        """Становление королём злодеев"""
        self.is_king = True
        print("Роб стал королём злодеев!")
    
    def __str__(self):
        status = "Король злодеев" if self.is_king else "Гладиатор"
        return f"{self.name} — {status}, итерация {self.iteration}"