
def addToInventory(inventory, addItems):
    for i in range(len(addItems)):
        if addItems[i] in inventory:
            inventory[addItems[i]] += 1
        else:
            inventory.setdefault(addItems[i], 1)
            
    return inventory

def disInventory(Inventory):
    print("Inventory: ")
    total_objects = 0
    for objects in Inventory: 
        print(str(Inventory[objects]) + ' ' + objects )
        total_objects += Inventory[objects]
    print("Total no of items: " , total_objects)

#disInventory(addToInventory(inv, dragonLoot))


