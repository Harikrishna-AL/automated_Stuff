
def disInventory(Inventory):
    print("Inventory: ")
    total_objects = 0
    for objects in Inventory: 
        print(str(Inventory[objects]) + ' ' + objects )
        total_objects += Inventory[objects]
    print("Total no of items: " , total_objects)

