# Define the Room class.

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
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

