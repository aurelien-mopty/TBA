"""
Module contenant la classe Inventory pour gérer les objets dans le jeu.

Cette classe permet de gérer une collection d'objets (items) dans un inventaire,
que ce soit pour un joueur ou une pièce du jeu.
"""

class Inventory:
    """
    Une classe représentant un inventaire d'objets dans le jeu.

    Cette classe permet de stocker, ajouter, supprimer et afficher les objets
    contenus dans un inventaire. Elle est utilisée à la fois pour l'inventaire
    des joueurs et pour les objets présents dans les différentes pièces du jeu.

    Attributes:
        items (dict): Un dictionnaire associant le nom des objets (str) à leurs
                      instances (Item).
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        """
        Ajoute un objet à l'inventaire.

        Args:
            item (Item): L'objet à ajouter à l'inventaire.

        Examples:
            >>> inventory = Inventory()
            >>> baguette = Item("baguette", "Une baguette magique", 1)
            >>> inventory.add_item(baguette)
            >>> "baguette" in inventory.items
            True
        """
        self.items[item.name] = item

    def remove_item(self,item_name):
        """
        Supprime un objet de l'inventaire.

        Args:
            item_name (str): Le nom de l'objet à supprimer.

        Returns:
            bool: True si l'objet a été supprimé, False sinon.

        Examples:
            >>> inventory = Inventory()
            >>> baguette = Item("baguette", "Une baguette magique", 1)
            >>> inventory.add_item(baguette)
            >>> inventory.remove_item("baguette")
            True
            >>> inventory.remove_item("inexistant")
            False
        """
        if item_name in self.items:
            del self.items[item_name]
            return True
        return False

    def get_inventory(self,ch1,ch2):
        """
        Génère une chaîne de caractères représentant le contenu de l'inventaire.

        Args:
            ch1 (str): Le message à afficher si l'inventaire est vide.
            ch2 (str): Le préfixe pour la liste des objets si l'inventaire n'est pas vide.

        Returns:
            str: Une chaîne de caractères décrivant le contenu de l'inventaire.

        Examples:
            >>> inventory = Inventory()
            >>> print(inventory.get_inventory("Vide", "Contenu:"))
            Vide
            >>> baguette = Item("baguette", "Une baguette magique", 1)
            >>> inventory.add_item(baguette)
            >>> print(inventory.get_inventory("Vide", "Contenu:"))
            Contenu:
               - baguette : Une baguette magique (1kg)
        """
        if len(self.items)==0:
            return ch1
        str_inventory=ch2
        for items in self.items.values():
            str_inventory+=f"   - {items}\n"
        return str_inventory
