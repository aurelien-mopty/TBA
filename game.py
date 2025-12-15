# Description: Game class
# Import modules

from item import Item
from room import Room
from player import Player
from command import Command
from actions import Actions
from door import Door
from character import Character

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.valid_directions = set()
        
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique ", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : retourner en arrière ", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check", " : afficher l'inventaire ", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : afficher l'inventaire de la piece ", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un item ", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : Jeter un item ", Actions.drop, 1)
        self.commands["drop"] = drop
        charge = Command("charge", " : Charger une pièce avec un beamer ", Actions.charge, 0)
        self.commands["charge"] = charge
        use = Command("use <item>", " : Utiliser le beamer pour vous téléporter dans la pièce chargée ", Actions.use, 1)
        self.commands["use"] = use
        unlock = Command("unlock", " : Dévérouiller une porte ", Actions.unlock, 1)
        self.commands["unlock"] = unlock
        """open = Command("open", " : Ouvrir une porte dévérouillée ", Actions.open, 1)
        self.commands["open"] = open"""
        

        # Setup rooms

        Hall_d_entree = Room("Hall_d_entree", "Le hall d'entrée de la fameuse école de magie Poudlard. Un elève pressé d'aller manger vous bouscule.")
        self.rooms.append(Hall_d_entree)

        Chambre_des_secrets= Room("Chambre_des_secrets", "la chambre des secrets. Une odeur putride émmane du sol . Vous vous cachez derrière un mur pour échapper à la vision du Basilic.")
        self.rooms.append(Chambre_des_secrets)

        Toilettes = Room("Toilettes", "les toilettes .Vous remarquez qu'une odeur se dégage des escaliers menant vers une pièce sombre.")
        self.rooms.append(Toilettes)
        Toilettes.inventory_room.add_item(Item("baguette","Cette baguette vous permet de lancer des sorts ",2))
       
        Couloir = Room("Couloir", "le couloir . Un surveillant vous presse pour que vous ne restiez pas oisif dans le couloir. Il est à peine 13h mais étant fatigué vous avez envie monté aux dortoirs pour faire une sieste.")
        self.rooms.append(Couloir)

        Dortoirs = Room("Dortoirs", "les dortoirs .Une petite fée malicieuse se trouve sur votre lit , vous vous demandez comment ce petit etre vicieux à pu rentrer dans votre chambre.")
        self.rooms.append(Dortoirs)
        
        Salle_secrete = Room("Salle_secrete", "la salle secrete.Peu d'eleves connaissent l'existence de cette endroit, mais les habitués du lieu s'y cachent pour consommer leur poudre de mandragore ou pour acceder rapidement aux dortoirs.",True)
        self.rooms.append(Salle_secrete)
        Salle_secrete.inventory_room.add_item(Item("Poudre_de_cheminette","Cette substance permet de vous téléporter dans une des pièces pièce que vous connaissez",1))
        Salle_secrete.inventory_room.items["Poudre_de_cheminette"].is_beamer = True

        Salle_a_manger = Room("Salle_a_manger", " la salle à manger.La delicieuse odeur de poulet roti vous donnes faim . Vous remarquer un petit passage dérobé derriere le buffet.")
        self.rooms.append(Salle_a_manger)
        Salle_a_manger.inventory_room.add_item(Item("clé", "une clé rouillée qui semble ancienne", 1))
        
        Jardin = Room("Jardin", " le jardin. Il y'a des plantes magiques provenant des quatres coins du monde.Des domestiques gobelins taillent les haies .")
        self.rooms.append(Jardin)
        
        Terrain_de_quidditch = Room("Terrain_de_quidditch", " sur le terrain de quidditch .L'équipe de serpentard s'entraine pour la finale de la coupe de Poudelard. Vous avez failli vous prendre la balle en pleine tete.")
        self.rooms.append(Terrain_de_quidditch)
        Terrain_de_quidditch.inventory_room.add_item(Item("balai","Ce balai vous permet de vous envoler dans les cieux",3))
        
        Cabane_d_hagrid = Room("Cabane_d_hagrid", "la cabane d'Hagrid.Cette maisonnette est petite mais le feu de bois vous rechauffe . Vous remarquez que le coffre d'Hagrid est ouvert")
        self.rooms.append(Cabane_d_hagrid)
        Cabane_d_hagrid.inventory_room.add_item(Item("oeuf de dragon","Attention , il va bientot éclore ",5))
        Cabane_d_hagrid.add_character(Character("Hagrid", "Un sorcier de renomée à Poudlard",Cabane_d_hagrid, ["Vous n'auriez pas vu Harry Potter ?"]))
        
        Foret_interdite = Room("Foret_interdite", "la foret interdite. Vous entendez un loup garou au loin , mieux vaut ne pas s'impatienter ici.")
        self.rooms.append(Foret_interdite)
        Foret_interdite.inventory_room.add_item(Item("Torche","Cela pourrait vous guider ",2))
        # Create exits for rooms

        Hall_d_entree.exits = {"N" : Couloir, "E" : None, "S" : Jardin, "O" :None , "U":None,"D":None}
        Chambre_des_secrets.exits = {"N" : None, "E" : None, "S" : None, "O" : None,"U":None,"D":None}
        Toilettes.exits = {"N" : None, "E" : Couloir, "S" : None, "O" : None ,"U":None,"D":Chambre_des_secrets}
        Couloir.exits = {"N" : Salle_a_manger, "E" :None, "S" : Hall_d_entree, "O" : Toilettes,"U":Dortoirs,"D":None}
        Dortoirs.exits = {"N" : None, "E" : None, "S" : None, "O" :None,"U":None,"D":Couloir}
        Salle_secrete.exits = {"N" : None, "E" : None, "S" : Dortoirs, "O" : None,"U":None,"D":None}
        Salle_a_manger.exits = {"N" : None, "E" : Salle_secrete, "S" : Couloir, "O" :None,"U":None,"D":None}
        Jardin.exits = {"N" : Hall_d_entree, "E" :Foret_interdite , "S" : None, "O" : Terrain_de_quidditch,"U":None,"D":None}
        Terrain_de_quidditch.exits = {"N" : None, "E" : Jardin, "S" : Cabane_d_hagrid, "O" :None,"U":None,"D":None }
        Cabane_d_hagrid.exits = {"N" : Terrain_de_quidditch, "E" : None, "S" : None, "O" :None,"U":None,"D":None }
        Foret_interdite.exits = {"N" : None, "E" : None, "S" : None, "O" :Jardin,"U":None,"D":None}

        #doors
        Toilettes.doors = {"D": Door(Chambre_des_secrets, "D", locked=True)}
        """Chambre_des_secrets.doors = {"U": Door(Toilettes, "U")}"""   #porte de la chambre des secrets vers les toilettes 

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room =Hall_d_entree

        self.valid_directions = set()
        for room in self.rooms:
            self.valid_directions.update(room.exits.keys())

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        if not command_string.strip():
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")    


        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
