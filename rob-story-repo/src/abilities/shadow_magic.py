"""
Магия теней — способность, полученная в Чёрном Кубе.
"""

class ShadowMagic:
    def __init__(self, user):
        self.user = user
        self.intensity = 0
    
    def activate(self):
        """Активация магии"""
        self.intensity = 100
        print("Магия теней активирована!")
    
    def stop_bullets(self, bullets):
        """Остановка пуль"""
        print(f"Остановлены пули: {bullets}")
        return self._reverse(bullets)
    
    def _reverse(self, bullets):
        """Разворот пуль"""
        print("Пули развёрнуты!")
        return bullets
    
    def freeze_limb(self, target, limb):
        """Заморозка конечности"""
        print(f"Конечность {limb} заморожена!")
        return "broken"
    
    def heat_explode(self, target):
        """Нагрев до взрыва"""
        print(f"{target.name} взорвался от нагрева!")
        return "destroyed"