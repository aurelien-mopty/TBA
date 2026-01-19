"""
Module contenant la classe Door.
"""

class Door:
    """
    Représente une porte connectant une salle dans une direction donnée.
    """
    def __init__(self, room, direction, locked=False):
        """
        Initialise une nouvelle porte.

        Args:
            room (Room): La salle de destination.
            direction (str): La direction de la porte (ex: 'N').
            locked (bool, optional): État de verrouillage de la porte. Defaults to False.
        """

        self.room = room
        self.direction = direction
        self.locked = locked
