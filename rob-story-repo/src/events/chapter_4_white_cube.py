"""
Глава 4: Белый Куб
"""

from locations.white_cube import WhiteCube
from characters.rob import Rob

class Chapter4:
    def run(self):
        print("=" * 50)
        print("ГЛАВА 4. БЕЛЫЙ КУБ")
        print("=" * 50)
        
        print("\nБезликий хватает часть корабля...")
        print("Роб летит 6 секунд 66 миллисекунд...")
        print("Безликий телепортируется...")
        
        # Белый Куб
        cube = WhiteCube()
        rob = Rob()
        
        cube.imprison(rob)
        
        print("\nБезликий говорит: 'Третья итерация. Почти чисто.'")
        print("Белый Куб — это тюрьма бога.")
        print("Роб — один из заключённых.")
        print("Его память стирают снова и снова...")
        
        return "imprisoned"