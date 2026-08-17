"""
Портал-магия — способность Роба.
"""

class PortalMagic:
    def __init__(self, user):
        self.user = user
        self.active_portals = []
    
    def open_portal(self, destination):
        """Открытие портала"""
        portal = Portal(destination)
        self.active_portals.append(portal)
        print(f"Портал в {destination} открыт!")
        return portal
    
    def summon_tentacles(self, count=2):
        """Призыв щупалец из портала"""
        print(f"Из порталов вылезли {count} щупальца!")
        return ["tentacle"] * count

class Portal:
    def __init__(self, destination):
        self.destination = destination
        self.is_open = True
    
    def close(self):
        self.is_open = False
        print("Портал закрыт")