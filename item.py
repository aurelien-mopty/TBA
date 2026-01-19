class Item:
    """
    Module définissant la classe Item.
    Ce module permet de gérer les objets transportables et leurs caractéristiques.
    """
    def __init__(self, name, description, weight : float):
        """
        Représente un objet interactif dans le jeu.

        Attributes:
            name (str): Le nom de l'objet.
            description (str): Une courte description de l'objet.
            weight (float): Le poids de l'objet en kilogrammes.
        """
        self.name = name
        self.description = description
        self.weight = weight
        self.charged_room = None
        self.is_beamer = False

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.
        """
        return  f"{self.name} : {self.description} ({self.weight}kg)"
