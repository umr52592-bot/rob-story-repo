"""
Глава 3: Встреча с пиратами
"""

from characters.pirates import Krutlon, Hell, Rovaam, Droid
from artifacts.memory_device import MemoryDevice

class Chapter3:
    def run(self):
        print("=" * 50)
        print("ГЛАВА 3. ВСТРЕЧА С ПИРАТАМИ")
        print("=" * 50)
        
        print("\nРоб добирается до берега чёрного моря...")
        print("У обломков корабля четверо пиратов:")
        
        krutlon = Krutlon()
        hell = Hell()
        rovaam = Rovaam()
        droid = Droid()
        
        print(f"- {krutlon.name}: {krutlon.description}")
        print(f"- {hell.name}: {hell.description}")
        print(f"- {rovaam.name}: {rovaam.description}")
        print(f"- {droid.name}: {droid.description}")
        
        # Устройство памяти
        print("\nПираты сажают Роба на стул...")
        device = MemoryDevice()
        result = device.activate(krutlon)
        
        if result == "failing":
            print("Что-то идёт не так — устройство замедляется...")
            return "device_failed"
        
        return "pirates_met"