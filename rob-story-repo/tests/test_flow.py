"""
Тестовый запуск всей истории.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.events import *

def test_full_story():
    """Запуск всей истории по главам"""
    
    print("\n" + "=" * 60)
    print("ЗАПУСК ИСТОРИИ РОБА — ПОЛНЫЙ ТЕСТ")
    print("=" * 60 + "\n")
    
    chapters = [
        Chapter1(),
        Chapter2(),
        Chapter3(),
        Chapter4(),
        Chapter5(),
        Chapter6(),
        Chapter7(),
        Chapter8(),
        Chapter9(),
        Chapter10(),
        Chapter11(),
        Epilogue()
    ]
    
    for chapter in chapters:
        chapter.run()
        print("\n" + "-" * 40 + "\n")
    
    print("Тест завершён!")

if __name__ == "__main__":
    test_full_story()