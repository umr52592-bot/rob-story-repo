"""
Пираты — помощники Роба.
Включают Крутлона, Роваама, Хелла и Дроида.
"""

class Pirate:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_ally = True

class Krutlon(Pirate):
    """Кристальный сутулый голем"""
    def __init__(self):
        super().__init__("Крутлон", "Кристальный сутулый голем")
        self.core = "crystal"
    
    def activate_device(self):
        """Запуск устройства памяти"""
        print("Крутлон запускает устройство...")
        return "memory_restore_attempt"

class Hell(Pirate):
    """Получеловек-полудемон"""
    def __init__(self):
        super().__init__("Хелл", "Получеловек-полудемон")
        self.eye = "red"
        self.height = 2.0  # обычный рост
    
    def transform(self):
        """Трансформация в 4-метровую форму"""
        self.height = 4.0
        print("Хелл вырос до 4 метров!")
    
    def open_hell_portal(self):
        """Открытие портала в ад"""
        print("Хелл открывает портал в ад!")
        return "hell_portal"

class Rovaam(Pirate):
    """Робот с рунами"""
    def __init__(self):
        super().__init__("Роваам", "Робот с рунами на сервоприводах")
        self.runes = True
        self.is_corrupted = False
    
    def shoot_magic(self):
        """Стрельба самонаводящейся магией"""
        print("Роваам стреляет магией!")
        return "homing_magic"
    
    def corrupt(self):
        """Заражение тьмой"""
        self.is_corrupted = True
        print("Роваам заражён тьмой...")

class Droid(Pirate):
    """Однорукий великан"""
    def __init__(self):
        super().__init__("Дроид", "Однорукий великан с огромной нижней губой")
        self.arms = 1
        self.jaw = "large"
    
    def attack(self):
        """Атака"""
        print("Дроид атакует!")
        return "smash"