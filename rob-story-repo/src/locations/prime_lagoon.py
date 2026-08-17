"""
Праймовая Лагуна — поле битвы.
Финальная зона, где собираются лучшие версии персонажей.
"""

class PrimeLagoon:
    def __init__(self):
        self.name = "Праймовая Лагуна"
        self.portal = None
        self.bosses = []
    
    def battle(self, rob, bezlikiy):
        """Финальное сражение"""
        print("Роб входит в Праймовую Лагуну...")
        
        # Безликий собирает лучшие версии
        self._summon_best_versions()
        
        # Босс-файты
        self._boss_fight_acqua(rob)
        self._boss_fight_worm_brothers(rob)
        self._boss_fight_alloy(rob)
        self._boss_fight_droid(rob)
        self._boss_fight_hell_rovaam(rob)
        
        # Финальный бой с Безликим
        self._final_battle(rob, bezlikiy)
    
    def _summon_best_versions(self):
        """Призыв лучших версий"""
        print("Безликий собрал лучшие версии из всех измерений!")
    
    def _boss_fight_acqua(self, rob):
        """Бой с Аквой"""
        print("Аква стреляет из дробовика...")
        # Роб останавливает пули
        print("Роб остановил пули и сломал дробовик")
        print("Голова Аквы взорвалась!")
    
    def _boss_fight_worm_brothers(self, rob):
        """Бой с братьями-червями"""
        print("Идеальные черви атакуют...")
        print("Роб прошёл сквозь них, как тень")
        print("Братья-черви уничтожены!")
    
    def _boss_fight_alloy(self, rob):
        """Бой со сплавом"""
        print("Сплав активирован...")
        print("Сплав отказался подчиняться и ушёл в портал")
        print("Капитан обезглавлен, Пикси сгорела")
    
    def _boss_fight_droid(self, rob):
        """Бой с Дроидом"""
        print("Дроид атакует...")
        print("Роб разломал Дроида и всосал провода")
    
    def _boss_fight_hell_rovaam(self, rob):
        """Бой с Хеллом и Роваамом"""
        print("Хелл (4 метра) и Роваам атакуют...")
        print("Хелл сброшен в бездну и умер")
        print("Роваам заражён тьмой")
    
    def _final_battle(self, rob, bezlikiy):
        """Финальный бой с Безликим"""
        print("Коридоры чернеют...")
        print("Появляются фиолетовые улыбки...")
        print("Безликий рассыпается в пыль!")
        return "victory"