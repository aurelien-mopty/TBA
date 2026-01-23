"""
Module contenant la classe Character pour représenter les personnages non-joueurs (PNJ) dans le jeu.

Cette classe permet de créer des personnages avec lesquels le joueur peut interagir,
et qui peuvent se déplacer aléatoirement dans le jeu.
"""

import random
class Character:
    """
    Représente un personnage non-joueur (PNJ) dans le jeu d'aventure.

    Un personnage est défini par un nom, une description, une pièce actuelle,
    des messages qu'il peut dire, et éventuellement des objets requis pour interagir avec lui.

    Attributes:
        name (str): Le nom du personnage.
        description (str): Une description textuelle du personnage.
        current_room (Room): La pièce dans laquelle se trouve actuellement le personnage.
        msgs (list): Une liste de messages que le personnage peut dire.
        displayed_msgs (list): Une liste des messages déjà affichés.
        required_items (list): Une liste d'objets requis pour interagir avec le personnage.
    """
    def __init__(self, name,description, current_room, msgs, required_items=None):
        """
        Initialise un nouveau personnage.

        Args:
            name (str): Le nom du personnage.
            description (str): La description du personnage.
            current_room (Room): La pièce actuelle où se trouve le personnage.
            msgs (list): Une liste de messages que le personnage peut dire.
            required_items (list, optional): Liste d'objets requis pour interagir avec le personnage.
                                           Defaults to None.

        Examples:
            >>> room = Room("Salle", "dans une salle")
            >>> character = Character("Dobby", "Un elfe de maison", room, ["Bonjour !"])
            >>> character.name
            'Dobby'
            >>> character.description
            'Un elfe de maison'
        """
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
                return print("Seras tu assez valeureux pour trouver la baguette. Si tu y arrives, je te donnerai un indice.")

        if not self.msgs:
            return"Je n'ai rien à dire."
        msg = self.msgs.pop(0)
        self.displayed_msgs.append(msg)

        if not self.msgs:
            self.msgs = self.displayed_msgs.copy()
            self.displayed_msgs = []
        return msg
