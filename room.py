# Define the Room class.
from inventory import Inventory
from door import Door
class Room:
    """
    Représente une pièce dans le jeu d'aventure.

    Une pièce est définie par un nom, une description, et des sorties
    vers d'autres pièces. Chaque sortie est associée à une direction
    (par exemple, "N", "E", "S", "O").

    Attributs:
        name (str): Le nom de la pièce.
        description (str): Une description textuelle de la pièce.
        exits (dict): Un dictionnaire associant une direction à une pièce.

    Methodes:
        get_exit(direction): Retourne la pièce dans la direction donnée.
        get_exit_string(): Retourne une chaîne décrivant les sorties disponibles.
        get_long_description(): Retourne une description complète de la pièce.

    Examples:
        >>> salle = Room("Salle", "dans une salle.")
        >>> salle.get_long_description()
        '\\nVous êtes dans une salle.\\n\\nSorties: \\n'
        >>> salle.exits["N"] = Room("Couloir", "dans un couloir.")
        >>> salle.get_exit_string()
        'Sorties: N'
        >>> salle.get_exit("N").name
        'Couloir'
        >>> salle.get_exit("S") is None
        True
    """
    # Define the constructor. 
    def __init__(self, name, description,dark=False):
        self.name = name
        self.description = description
        self.exits = {}
        self.doors = {}
        self.inventory_room=Inventory()
        self.dark=dark
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        elif direction in self.doors:
            if not self.doors[direction].locked:
                return self.doors[direction].room
        return None
    
        
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: "
        exits = []

        # Ajouter les sorties normales
        for exit in self.exits:
            if self.exits[exit] is not None:
                exits.append(exit)

        # Ajouter les portes déverrouillées
        for door_dir in self.doors:
            if not self.doors[door_dir].locked:
                # Vérifier si cette direction n'est pas déjà dans les sorties normales
                if door_dir not in exits:
                    exits.append(door_dir)
        if exits:
            exit_string += ", ".join(exits)
        else:
            exit_string += "Aucune"
        return exit_string

    def add_character(self, character):
        self.characters[character.name] = character

    def remove_character(self, character_name):
        if character_name in self.characters:
            del self.characters[character_name]
            return True
        return False

    # Return a long description of this room including exits.
    def get_long_description(self):
        description = f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
        for door_dir, door in self.doors.items():
            if door.locked:
                description += f"Il y a une porte verrouillée vers le {door_dir}.\n"
        return description

    def get_inventory_room(self): 
        ch1="Il n'y a rien ici."
        ch2="La pièce contient :\n"
        inventory_str = self.inventory_room.get_inventory(ch1,ch2)

        if self.characters:
            if len(self.inventory_room.items) > 0:
                inventory_str += "\n"
            inventory_str += "Personnages présents :\n"
            for character in self.characters.values():
                inventory_str += f"   - {character}\n"
        return inventory_str
        

