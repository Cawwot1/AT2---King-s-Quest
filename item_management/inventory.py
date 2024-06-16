class Inventory:
    # Attributes
    __inventory = None
    __equipment = None
    __consumables = None
    __capacity = None
    
    #Formatting Lists
    __inv_format = None
    __equip_format = None
    __consume_format = None

    #Formating Other
    __item_num = None
    __item_type = None

    # Constructor
    def __init__(self, capacity):
        
        #Item Lists
        self.__capacity = capacity
        self.__inventory = []
        self.__equipment = []
        self.__consumables = []

        #Formatting Lists
        self.__inv_format = []
        self.__equip_format = []
        self.__consume_format = []

        #Formating Other
        self.__item_num = 0
        self.__equipment_type = None



    # Accessors
    def getCapacity(self):
        return self.__capacity

    def getInventory(self):
        return self.__inventory

    def getEquipment(self):
        return self.__equipment

    def getConsumables(self):
        return self.__consumables

    # Mutators
    def setCapacity(self, new_capacity):
        self.__capacity = new_capacity

    def setInventory(self, new_inventory):
        self.__inventory = new_inventory

    def setEquipment(self, new_equipment):
        self.__equipment = new_equipment

    def setConsumables(self, new_consumables):
        self.__consumables = new_consumables

    #Behaviours
    def inventory_info(self):
        for item in self.__equipment: #Formatting Equipment
            self.__item_num += 1
            self.__equip_format.append(f"{self.__item_num}. {item.getName()}\n")
        self.__item_num = 0
        
        for item in self.__consumables: #Formatting Consumables
            self.__item_num += 1
            self.__equip_format.append(f"{self.__item_num}. {item.getName()}\n")
        self.__item_num = 0

        return (f"\n\033[1mEquipment:\033[0m\n{''.join(self.__equip_format)}\n"
                f"\n\033[1mConsumables:\033[0m\n{''.join(self.__consume_format)}")
    
    def add_item(self, item):
        self.__item_type = item.getItemType()
        if self.__item_type == "equipment":
            self.__equipment.append(item)
            print(f"Stored {item.getName()} in Equipment") #remove when visuals
        elif self.__item_type == "consumables":
            self.__consumables.append(item)
            print(f"Stored {item.getName()} in Consumables") #remove when visuals