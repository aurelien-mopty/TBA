"""Game class"""

# Import modules


from quest import Quest,QuestManager
from item import Item
from room import Room
from player import Player
from command import Command
from actions import Actions
from door import Door
from character import Character

DEBUG=False
class Game:
    """The Game class manages the overall game state and flow."""


    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.valid_directions = set()

    # Setup the game
    def setup(self, player_name=None):
        """Initialize the game with rooms, commands, and quests."""
        self._setup_commands()
        self._setup_rooms()
        self._setup_player(player_name)
        self._setup_quests()


    def _setup_commands(self):
        """Initialize all game commands."""
        self.commands["help"] = Command("help"
                                        , " : afficher cette aide"
                                        , Actions.help
                                        , 0)
        self.commands["quit"] = Command("quit"
                                        , " : quitter le jeu"
                                        , Actions.quit
                                        , 0)
        self.commands["go"] = Command("go"
                                      , "<N|E|S|O> : se déplacer dans une direction cardinale"
                                      , Actions.go
                                      , 1)
        self.commands["quests"] = Command("quests"
                                          , " : afficher la liste des quêtes"
                                          , Actions.quests
                                          , 0)
        self.commands["quest"] = Command("quest"
                                         , " <titre> : afficher les détails d'une quête"
                                         , Actions.quest
                                         , 1)
        self.commands["activate"] = Command("activate"
                                            , " <titre> : activer une quête"
                                            , Actions.activate
                                            , 1)
        self.commands["rewards"] = Command("rewards"
                                           , " : afficher vos récompenses"
                                           , Actions.rewards
                                           , 0)
        self.commands["history"] = Command("history"
                                           , " : afficher l'historique"
                                           , Actions.history
                                           , 0)
        self.commands["back"] = Command("back"
                                           , " : retourner en arrière "
                                           , Actions.back
                                           , 0)
        self.commands["check"] = Command("check"
                                           , " : afficher l'inventaire "
                                           , Actions.check
                                           , 0)

        self.commands["look"] = Command("look"
                                           , " : afficher l'inventaire de la piece"
                                           , Actions.look
                                           , 0)
        self.commands["take"] = Command("take"
                                           , " : prendre un item"
                                           , Actions.take
                                           , 1)
        self.commands["drop"] = Command("drop"
                                           , " : Jeter un item"
                                           , Actions.drop
                                           , 1)
        self.commands["charge"] = Command("charge"
                                           , " : Charger une pièce avec un beamer  "
                                           , Actions.charge
                                           , 0)
        self.commands["use"] = Command("use"
                                           , " : Utiliser le beamer pour vous téléporter dans la pièce chargée "
                                           , Actions.use
                                           , 1)
        self.commands["unlock"] = Command("unlock"
                                           , " : Dévérouiller une porte "
                                           , Actions.unlock
                                           , 1)
        self.commands["talk"] = Command("talk"
                                           , " : Intéragir avec un PNJ "
                                           , Actions.talk
                                           , 1)
        
    def _setup_rooms(self):
        Hall_d_entree = Room("Hall_d_entree", "Le hall d'entrée de la fameuse école de magie Poudlard. Un elève pressé d'aller manger vous bouscule.")

        Hall_d_entree.add_character(Character("McGonagall", "La directrice de Gryffondor",Hall_d_entree, ["Vous êtes en retard, dépêchez-vous !!"]))


        Grotte= Room("Grotte", "Une grotte etrange. Il fait très sombre. .")


        Toilettes = Room("Toilettes", "les toilettes .Vous remarquez qu'une odeur se dégage des escaliers menant vers une pièce sombre.")

        Toilettes.inventory_room.add_item(Item("baguette","Cette baguette vous permet de lancer des sorts ",2))
       
        Couloir = Room("Couloir", "le couloir . Un surveillant vous presse pour que vous ne restiez pas oisif dans le couloir. Il est à peine 13h mais étant fatigué vous avez envie monté aux dortoirs pour faire une sieste.")

        Couloir.add_character(Character("Mimi_Geignarde", "Un fantome qui se balade dans poudlard ",Couloir, ["Tu es nouveau toi?"]))


        Dortoirs = Room("Dortoirs", "les dortoirs .Une petite fée malicieuse se trouve sur votre lit , vous vous demandez comment ce petit etre vicieux à pu rentrer dans votre chambre.")

        Dortoirs.add_character(Character("Dobby", "Un petit elfe de maison",Dortoirs, ["Dobby a été très vilain avec Harry Potter."],  required_items=["baguette"]))

        
        Salle_secrete = Room("Salle_secrete", "la salle secrete.Peu d'eleves connaissent l'existence de cette endroit, mais les habitués du lieu s'y cachent pour consommer leur poudre de mandragore ou pour acceder rapidement aux dortoirs.",True)

        Salle_secrete.inventory_room.add_item(Item("Poudre_de_cheminette","Cette substance permet de vous téléporter dans une des pièces pièce que vous connaissez",1))
        Salle_secrete.inventory_room.items["Poudre_de_cheminette"].is_beamer = True

        Salle_a_manger = Room("Salle_a_manger", " la salle à manger.La delicieuse odeur de poulet roti vous donnes faim . Vous remarquer un petit passage dérobé derriere le buffet.")

        Salle_a_manger.inventory_room.add_item(Item("clé", "une clé rouillée qui semble ancienne", 1))
        Salle_a_manger.add_character(Character("Crabbe", "Un élève gourmand qui ne devrait pas ête là",Salle_a_manger, ["Tu vas finir ton cookie ?"]))

        Jardin = Room("Jardin", " le jardin. Il y'a des plantes magiques provenant des quatres coins du monde.Des domestiques gobelins taillent les haies .")
        Jardin.inventory_room.add_item(Item("Mandragore","Cette racine pousse un cri strident , bouchez vous les oreilles",2))
        
        Terrain_de_quidditch = Room("Terrain_de_quidditch", " sur le terrain de quidditch .L'équipe de serpentard s'entraine pour la finale de la coupe de Poudelard. Vous avez failli vous prendre la balle en pleine tete.")
        Terrain_de_quidditch.inventory_room.add_item(Item("balai","Ce balai vous permet de vous envoler dans les cieux",3))
        
        Cabane_d_hagrid = Room("Cabane_d_hagrid", "la cabane d'Hagrid.Cette maisonnette est petite mais le feu de bois vous rechauffe . Vous remarquez que le coffre d'Hagrid est ouvert")
        Cabane_d_hagrid.inventory_room.add_item(Item("Oeuf_de_dragon","Attention , il va bientot éclore ",5))
        Cabane_d_hagrid.add_character(Character("Hagrid", "Un sorcier de renomée à Poudlard",Cabane_d_hagrid, ["Vous n'auriez pas vu Harry Potter ?"]))
        
        Foret_interdite = Room("Foret_interdite", "la foret interdite. Vous entendez un loup garou au loin , mieux vaut ne pas s'impatienter ici.")
        Foret_interdite.inventory_room.add_item(Item("Torche","Cela pourrait vous guider ",2))
        Chambre_des_Secrets=Room("Chambre_des_Secrets","la chambre des secrets. Une odeur putride émane du sol.")
        
        for room in [Hall_d_entree,Grotte,Toilettes,Couloir,Dortoirs,Salle_secrete,Salle_a_manger,Jardin,Terrain_de_quidditch,Cabane_d_hagrid,Foret_interdite,Chambre_des_Secrets]:
            self.rooms.append(room)

        Hall_d_entree.exits = {"N" : Couloir, "E" : None, "S" : Jardin, "O" :None , "U":None,"D":None}
        Grotte.exits = {"N" : None, "E" : None, "S" : None, "O" : Chambre_des_Secrets,"U":None,"D":None}
        Toilettes.exits = {"N" : None, "E" : Couloir, "S" : None, "O" : None ,"U":None,"D":Grotte}
        Couloir.exits = {"N" : Salle_a_manger, "E" :None, "S" : Hall_d_entree, "O" : Toilettes,"U":Dortoirs,"D":None}
        Dortoirs.exits = {"N" : None, "E" : None, "S" : None, "O" :None,"U":None,"D":Couloir}
        Salle_secrete.exits = {"N" : None, "E" : None, "S" : Dortoirs, "O" : None,"U":None,"D":None}
        Salle_a_manger.exits = {"N" : None, "E" : Salle_secrete, "S" : Couloir, "O" :None,"U":None,"D":None}
        Jardin.exits = {"N" : Hall_d_entree, "E" :Foret_interdite , "S" : None, "O" : Terrain_de_quidditch,"U":None,"D":None}
        Terrain_de_quidditch.exits = {"N" : None, "E" : Jardin, "S" : Cabane_d_hagrid, "O" :None,"U":None,"D":None }
        Cabane_d_hagrid.exits = {"N" : Terrain_de_quidditch, "E" : None, "S" : None, "O" :None,"U":None,"D":None }
        Foret_interdite.exits = {"N" : None, "E" : None, "S" : None, "O" :Jardin,"U":None,"D":None}
        Chambre_des_Secrets.exits= {"N" : None, "E" : None, "S" : None, "O" : None,"U":None,"D":None}
        Toilettes.doors = {"D": Door(Grotte, "D", locked=True)}
        """Grotte.doors = {"U": Door(Toilettes, "U")}"""#porte de la chambre des secrets vers les toilettes    

       

        
    


    def _setup_player(self, player_name=None):
        
        if player_name is None:
            player_name = input("\nEntrez votre nom: ")

        self.player = Player(player_name)
        
        self.player.current_room = self.rooms[0]  # swamp
        self.valid_directions = set()
        for room in self.rooms:
            self.valid_directions.update(room.exits.keys())

    def _setup_quests(self):
        """Initialize all quests."""
        exploration_quest = Quest(
            title="Explorateur de Poudlard",
            description="Atteindre la chambre des secrets.",
            objectives=["Visiter Chambre des Secrets"],
            reward="Titre d'explorateur de Poudlard"
        )

        item_quest = Quest(
            title="Petit collectionneur",
            description="Obtenir les 6 objets",
            objectives=["Obtenir balai", "Obtenir Oeuf de Dragon","Obtenir Mandragore","Obtenir Baguette","Obtenir Torche","Dent de Basilic"],
            reward="Titre de petit collectionneur"
        )

        meet_quest = Quest(
            title="Bavardeur magique",
            description="Interagir avec Dobby",
            objectives=["Parler avec Dobby"],
            reward="Titre de Bavardeur magique"
        )

        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(item_quest)
        self.player.quest_manager.add_quest(meet_quest)

    def win(self):
        return all(quest.is_completed for quest in self.player.quest_manager.quests)
    
    def lose(self):
        if self.player.current_room.name == "Grotte":
            required_items = ["baguette", "Mandragore", "Oeuf_de_dragon", "Torche", "balai"]
            has_required_items = all(any(item.name == required_item for required_item in required_items) for item in self.player.inventory.items.values())
            return not has_required_items
        return False
    
    # Play the game
    def play(self):
        if DEBUG:
            print("DEBUG: Début de la partie.")
        

        self.setup()
        self.print_welcome()
        while not self.finished:
            # Obtenir la commande du joueur
            command_input = input("> ")
            list_of_words = command_input.split(" ")
            command_word = list_of_words[0]

            # Exécuter la commande
            if command_word in self.commands.keys():
                command = self.commands[command_word]
                command.action(self, list_of_words, command.number_of_parameters)

                # Déplacer les PNJ uniquement si la commande est 'go'
                if command_word == "go":
                    for room in self.rooms:
                        for character in list(room.characters.values()):
                            if character.name == "Mimi_Geignarde":
                                if DEBUG:
                                    print(" message debug, position de mimi:")
                                    print(character.current_room.name)
                                character.move()

            if self.win():
                print("\n🎉 Félicitations ! Vous avez complété toutes les quêtes et gagné la partie !\n")
                self.finished = True

            if self.lose():
                print("\n❌ Vous avez perdu la partie ! Vous n'aviez pas les obejts nécessaires pour vaincre le Basilic.\n")
                self.finished = True
   
    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """Process the command entered by the player."""
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
        """Print the welcome message."""

        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")

        print(self.player.current_room.get_long_description())


def main():
    """Create a game object and play the game"""
    Game().play()


if __name__ == "__main__":
    main()