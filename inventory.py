from item import Item

class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def get_inventory(self,ch1,ch2):   
        if len(self.items)==0:
            return ch1
        else:
            str_inventory=ch2
            for items in self.items.values():
                str_inventory+=f"   - {items}\n"
            return str_inventory