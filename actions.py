# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        directionpossible= [
        (["N", "NORD"], "N"),
        (["S", "SUD"], "S"),
        (["E", "EST"], "E"),
        (["O", "OUEST"], "O"),
        (["U", "HAUT","UP"], "U"),
        (["D", "BAS","DOWN"], "D"),]
        direction = list_of_words[1].upper()
        for liste in directionpossible:
            if direction in liste[0] :
                direction=liste[1]
        
        if direction not in game.valid_directions:
            print(f"\n La direction {direction} n'est pas valide. Les directions possibles sont : {', '.join(sorted(game.valid_directions))}\n")
            return False

        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print(player.get_history())

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if not player.can_back():#Verifie si la liste history  est vide , si oui
            print("Vous ne pouvez pas revenir en arriere")
            return
        if player.current_room.name=="Chambre_des_secrets":
            print("Vous ne pouvez pas sortir")
        else:
            #lorsque l'on a déjà visité une pièce, on décrémente la valeur associée à la clé du dictionnaire
            #self.visited_rooms_indexs pour ne pas supprimer la pièce de l'historique
            #lorqu'une pièce n'est visitée qu'une fois, cette dernière est bien supprimée de l'historique
            deleted_room = player.past_room.pop() 
            player.current_room = deleted_room
            player.visited_rooms_indexs[deleted_room.name]-=1 
            if player.visited_rooms_indexs[deleted_room.name]==0:
                player.visited_rooms_indexs.pop(deleted_room.name)
                player.history.remove(deleted_room)
            print(player.current_room.get_long_description())
            print(player.get_history())

    @staticmethod      
    def check(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print(player.get_inventory_player())

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False


        for item in player.inventory.items.values():
            if item.name=="Torche":
                player.current_room.dark=False
        
        if player.current_room.name=="Salle_secrete" and player.current_room.dark==False:
            print("Grace à votre torche vous y voyez mieux")   

        if player.current_room.dark is True:
            print("Il fait trop sombre pour voir quelques chose")
        else:
            print(player.current_room.get_inventory_room())

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))

        room=player.current_room
        item_name = list_of_words[1]
        if item_name not in room.inventory_room.items:
            print(f"L'objet '{item_name}' n'est pas présent ici.")
            return False
        item= room.inventory_room.items[item_name]
        current_weight=sum(item.weight for item in player.inventory.items.values())
        new_weight = current_weight + item.weight
        if new_weight>player.max_weight:
            print(f"L'objet est trop lourd !")
            return False

        
        player.inventory.add_item(item)
        room.inventory_room.remove_item(item_name)
        print(f"Vous avez pris l'objet '{item_name}' ")
        
        return True

    @staticmethod 
    def drop(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))

        room=player.current_room
        item_name = list_of_words[1].lower()
        if item_name not in player.inventory.items:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
            return False
        item= player.inventory.items[item_name]
        player.inventory.remove_item(item_name)
        room.inventory_room.add_item(item)
        print(f"vous avez déposé l'objet '{item_name}' ")
        return True
    
    @staticmethod
    def charge(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        cherche_beamer = None
        for item in player.inventory.items.values():
            if item.is_beamer:
                cherche_beamer = item
            
        if cherche_beamer is None:
            print("Vous ne disposez pas de la Poudre de cheminette pour charger cette pièce ! ")
            return False
    
        cherche_beamer.charged_room = player.current_room
        print(f"Vous avez chargé la Poudre de cheminette dans {player.current_room.name}")
        return True

    @staticmethod 
    def use(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1]
        if item_name not in player.inventory.items:
            print(f"Vous ne disposez pas de la {item_name} pour vous téléporter ! ")
            return False
        
        item = player.inventory.items[item_name]

        if not item.is_beamer:
            print(f"L'objet '{item_name}' n'est pas un beamer.")
            return False

        if item.charged_room is None:
            print("La Poudre de cheminette n'a été chargée avec aucune pièce !")
            return False
        
        player.current_room = item.charged_room
        print(f"Vous avez été téléporté dans la pièce : {item.charged_room.name}")
        print(item.charged_room.get_long_description())
        return True

    @staticmethod
    def unlock(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        direction = list_of_words[1].upper()

        if direction not in player.current_room.doors:
            print(f"Il n'y a pas de porte dans la direction {direction}.")
            return False

        door = player.current_room.doors[direction]

        if not door.locked:
            print(f"La porte vers le {direction} n'est pas verrouillée.")
            return False

        cherche_cle = None
        for item in player.inventory.items.values():
            if item.name == "clé":
                cherche_cle = item
                break

        if cherche_cle is None:
            print("Vous n'avez pas de clé pour déverrouiller cette porte.")
            return False

        door.locked = False
        print(f"Vous avez déverrouillé la porte vers le {direction} avec la clé.")
        return True

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        character_name= list_of_words[1]

        if character_name not in player.current_room.characters:
            print(f"Le personnage {character_name} n'est pas ici.")
            return False
        character = player.current_room.characters[character_name]
        msg = character.get_msg(player)
        print(f"{character_name} : {msg}") 

        return True
    
        @staticmethod
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all quests
        game.player.quest_manager.show_quests()
        return True
    
    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        # Show quest details
        game.player.quest_manager.show_quest_details(quest_title, current_counts)
        return True
    
    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        # print(f"\nImpossible d'activer la quête '{quest_title}'. \
        #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
        return False


    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True