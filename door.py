class Door:
    """
    Représente une porte connectant une salle dans une direction donnée.
    """
    def __init__(self, room, direction, locked=False):
        """
        Initialise une nouvelle porte.

        :param room: La salle de destination.
        :param direction: La direction de la porte (ex: 'nord').
        :param locked: État de verrouillage de la porte.
        """

        self.room = room 
        self.direction = direction  
        self.locked = locked