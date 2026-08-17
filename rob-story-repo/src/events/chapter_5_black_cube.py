"""
Глава 5: Чёрный Куб
"""

from locations.white_cube import WhiteCube
from locations.black_cube import BlackCube

class Chapter5:
    def run(self):
        print("=" * 50)
        print("ГЛАВА 5. ЧЁРНЫЙ КУБ")
        print("=" * 50)
        
        print("\nКуб начал чернеть...")
        print("Изнутри донёсся голос: 'Я ВСЕГДА ВОЗВРАЩАЮСЬ!'")
        
        # Трансформация
        white_cube = WhiteCube()
        black_cube = white_cube.turn_black()
        
        print("\nПоявился Рассказчик, закричал, но было поздно...")
        print("Из куба вышел новый Роб с чёрными глазами...")
        print("Он владел магией теней и бездны.")
        
        print("\nРассказчик открыл портал и сбежал...")
        print("Роб сказал: 'Я хочу уничтожить Тюрьму Бога'")
        
        print("\nБезликий убил Рассказчика...")
        print("Безликий телепортируется в Праймовую Лагуну...")
        
        return "awakened"