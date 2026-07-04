import sys

def display_inventory(inventory):
    print("\nInventory:")
    item_total = 0
    for k, v in inventory.items():
        try:
            item_total += int(v)
        except ValueError:
            pass
        print(f"{k}: {v}")
    print("Total number of items: " + str(item_total))

# Start with an empty inventory dictionary so the user populates it
my_inventory = {}

while True:
    print("\nWelcome to the inventory management system\n")
    print("PRESS 1 TO UPDATE INVENTORY \n")
    print("PRESS Q TO QUIT PROGRAM:")
    
    x = input('>>> ').strip()
    
    if x.lower() == 'q':
        break
        
    else:
        try:
            choice = int(x)
            if choice == 1:
                # Prompting user to enter their key-value pairs
                stuff = input("Enter keys and values respectively (e.g., gold coin:42, arrows:12):\n")
                
                try:
                    # Clear or update based on pairs split by commas
                    pairs = stuff.split(',')
                    for pair in pairs:
                        if ':' in pair:
                            k, v = pair.split(':')
                            # Strip whitespace and update the inventory
                            my_inventory[k.strip()] = int(v.strip())
                        else:
                            raise ValueError("Missing colon separator between key and value.")
                    
                    # Display the freshly updated inventory
                    display_inventory(my_inventory)
                    
                except ValueError:
                    print("Error: Please format input exactly as 'item:quantity, item2:quantity' using numbers for quantities.")
            else:
                print("You didn't choose a valid operation.")
                sys.exit()
                
        except ValueError:
            print("Invalid input! Please enter 1 to update or Q to quit.")

