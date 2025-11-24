# Define the Player class.
class Player():
    """
    Représente un joueur dans le jeu d'aventure.

    Le joueur est caractérisé par un nom et une pièce courante.
    Il peut se déplacer entre les pièces du jeu.

    Attributs:
        name (str): Le nom du joueur.
        current_room (Room): La pièce dans laquelle se trouve actuellement le joueur.

    Méthodes:
        move(direction): Déplace le joueur dans la direction indiquée.

    Examples:
        >>> from room import Room
        >>> salle = Room("Salle", "dans une salle.")
        >>> joueur = Player("Alice")
        >>> joueur.current_room = salle
        >>> salle.exits = {"N": Room("Couloir", "dans un couloir.")}
        >>> joueur.move("N")
        \\nVous êtes dans un couloir.\\n\\nSorties: \\n
        True
        >>> joueur.move("S")
        \\nAucune porte dans cette direction !\\n
        False
    """
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history=[]
        self.visited_rooms_indexs = {}
        self.past_room=[]
        

    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.past_room.append(self.current_room)
        #self.history.append(self.current_room)

        if self.current_room not in self.history:
            self.history.append(self.current_room)
            self.visited_rooms_indexs[self.current_room.name]=1
        else:
            self.visited_rooms_indexs[self.current_room.name]+=1
        
        # Set the current room to the next room.

        self.current_room = next_room
        print(self.current_room.get_long_description())
       
        
        print(self.get_history())
        return True
    
    def can_back(self):#Verifie si la liste history  est vide , si oui
        return self.history!=[]
    
    def get_history(self): 
        str_history=" Vous avez déja visité:\n"
        for room in self.history:
            str_history+="-" + room.name +"\n"
        return str_history
