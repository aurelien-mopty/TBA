import random
class Character:
    def __init__(self, name,description, current_room, msgs):
        self.name = name 
        self.description = description  
        self.current_room = current_room 
        self.msgs = []


    def __str__(self):
        return  f"{self.name} : {self.description}"
    
    def move(self):
        if random.choice([True, False]):
            exits = []
            for direction, room in self.current_room.exits.items():
                if room is not None:
                    exits.append((direction, room))
            for direction, door in self.current_room.doors.items():
                if not door.locked:
                    exits.append((direction, door.room))
            if exits:
                direction, next_room = random.choice(exits)
                self.current_room.remove_character(self.name)
                self.current_room = next_room
                self.current_room.add_character(self)
                return True
        return False