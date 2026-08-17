"""
Глава 7: Братья-черви
"""

class Chapter7:
    def run(self):
        print("=" * 50)
        print("ГЛАВА 7. БРАТЬЯ-ЧЕРВИ")
        print("=" * 50)
        
        print("\nРоба встречают идеальные черви и чрево...")
        print("Тонкие извилистые ноги и руки обвили его...")
        print("Роб прошёл сквозь них, как тень...")
        
        # Нитрино-бомба
        from artifacts.nitrino_bomb import NitrinoBomb
        bomb = NitrinoBomb()
        
        print("Роб засунул в сердечник нитрино-бомбу...")
        bomb.detonate("братья-черви")
        
        print("От идеальных братьев остались только шлем и расколотый нагрудник.")
        
        return "worms_defeated"