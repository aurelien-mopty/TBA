class Item:

   # Define the constructor. 
    def __init__(self, name, description, weight : float):
        self.name = name
        self.description = description
        self.weight = weight
        self.charged_room = None
        self.is_beamer = False
        
        
    def __str__(self):
        return  f"{self.name} : {self.description} ({self.weight}kg)"

    
