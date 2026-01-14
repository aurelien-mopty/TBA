import random

class Character:
    def __init__(self, name,description, current_room, msgs, required_items=None):
        self.name = name 
        self.description = description  
        self.current_room = current_room 
        self.msgs = msgs.copy()
        self.displayed_msgs = []
        self.required_items = required_items if required_items is not None else []

    def __str__(self):
        return  f"{self.name} : {self.description}"
    
    def move(self):
        if random.choice([True, False]):
            exits = []
            for direction, room in self.current_room.exits.items():
                if room is not None and room.name != "Chambre_des_secrets":
                    exits.append((direction, room))
            for direction, door in self.current_room.doors.items():
                if not door.locked and door.room.name !="Chambre_des_secrets" :
                    exits.append((direction, door.room))
            if exits:
                direction, next_room = random.choice(exits)
                self.current_room.remove_character(self.name)
                self.current_room = next_room
                self.current_room.add_character(self)
                return True
        return False
    
    def get_msg(self, player=None):
            if player is not None and self.required_items:
                has_required_items = any(any(item.name == required_item for required_item in self.required_items) for item in player.inventory.items.values())
                if not has_required_items:
                    return f"Sera tu assez valeureux pour trouver la baguette , si tu y arrives je te donnerais un indice. Voici un objet qui pourrait t'etre utile : {', '.join(self.required_items)}."

            if not self.msgs:
                return"J n'ai rien à dire."
            msg= self.msgs.pop(0)
            self.displayed_msgs.append(msg)
        

            if not self.msgs:
                self.msgs = self.displayed_msgs.copy()
                self.displayed_msgs = []
            return msg

