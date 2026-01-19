"""
Module contenant la classe Room pour représenter les pièces dans le jeu d'aventure.

Ce module définit la classe Room qui permet de modéliser les différentes pièces
dans lesquelles le joueur peut se déplacer. Chaque pièce peut contenir des objets,
des personnages, et avoir des sorties vers d'autres pièces.
"""

from inventory import Inventory
from door import Door
class Room:
    """
    Représente une pièce dans le jeu d'aventure.

    Une pièce est définie par un nom, une description, et des sorties vers d'autres pièces.
    Chaque sortie est associée à une direction (par exemple, "N", "E", "S", "O").
    Une pièce peut également contenir des objets, des personnages, et des portes verrouillées.

    Attributes:
        name (str): Le nom de la pièce.
        description (str): Une description textuelle de la pièce.
        exits (dict): Un dictionnaire associant une direction à une pièce.
        doors (dict): Un dictionnaire associant une direction à une porte (Door).
        inventory_room (Inventory): L'inventaire des objets présents dans la pièce.
        dark (bool): Indique si la pièce est sombre.
        characters (dict): Un dictionnaire associant le nom des personnages à leurs instances.

    Methods:
        get_exit(direction): Retourne la pièce ou la porte dans la direction donnée.
        get_exit_string(): Retourne une chaîne décrivant les sorties disponibles.
        get_long_description(): Retourne une description complète de la pièce.
        add_character(character): Ajoute un personnage à la pièce.
        remove_character(character_name): Retire un personnage de la pièce.
        get_inventory_room(): Retourne une description des objets et personnages présents.

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
        """
        Retourne la pièce ou la porte dans la direction donnée si elle existe.

        Args:
            direction (str): La direction dans laquelle chercher une sortie.

        Returns:
            Room or None: La pièce ou None si aucune sortie n'existe dans cette direction.

        Examples:
            >>> salle1 = Room("Salle1", "dans une pièce")
            >>> salle2 = Room("Salle2", "dans une autre pièce")
            >>> salle1.exits["N"] = salle2
            >>> salle1.get_exit("N") == salle2
            True
            >>> salle1.get_exit("S") is None
            True
        """
        if direction in self.exits:
            return self.exits[direction]
        if direction in self.doors:
            if not self.doors[direction].locked:
                return self.doors[direction].room
        return None

    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties disponibles de la pièce.

        Returns:
            str: Une chaîne de caractères décrivant les sorties disponibles.

        Examples:
            >>> salle1 = Room("Salle1", "dans une pièce")
            >>> salle2 = Room("Salle2", "dans une autre pièce")
            >>> salle1.exits["N"] = salle2
            >>> salle1.get_exit_string()
            'Sorties: N'
        """
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
        """
        Ajoute un personnage à la pièce.

        Args:
            character (Character): Le personnage à ajouter à la pièce.

        Examples:
            >>> salle = Room("Salle", "dans une salle.")
            >>> personnage = Character("Harry", "Un sorcier", salle, ["Bonjour !"])
            >>> salle.add_character(personnage)
            >>> "Harry" in salle.characters
            True
        """
        self.characters[character.name] = character

    def remove_character(self, character_name):
        """
        Retire un personnage de la pièce.

        Args:
            character_name (str): Le nom du personnage à retirer.

        Returns:
            bool: True si le personnage a été retiré, False sinon.

        Examples:
            >>> salle = Room("Salle", "dans une salle.")
            >>> personnage = Character("Harry", "Un sorcier", salle, ["Bonjour !"])
            >>> salle.add_character(personnage)
            >>> salle.remove_character("Harry")
            True
            >>> salle.remove_ character("Inexistant")
            False
        """
        if character_name in self.characters:
            del self.characters[character_name]
            return True
        return False

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Retourne une description complète de la pièce incluant les sorties.

        Returns:
            str: Une description complète de la pièce.

        Examples:
            >>> salle = Room("Salle", "dans une salle.")
            >>> salle.get_long_description()  # doctest: +ELLIPSIS
            '\\nVous êtes dans une salle.\\n\\nSorties: ...'
        """
        description = f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
        for door_dir, door in self.doors.items():
            if door.locked:
                description += f"Il y a une porte verrouillée vers le {door_dir}.\n"
        return description

    def get_inventory_room(self):
        """
        Retourne une description des objets et personnages présents dans la pièce.

        Returns:
            str: Une chaîne de caractères décrivant les objets et personnages présents.

        Examples:
            >>> salle = Room("Salle", "dans une salle.")
            >>> salle.get_inventory_room()
            'Il n'y a rien ici.'
        """
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
