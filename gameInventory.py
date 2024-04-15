def displayInventory(inventory):
  #show itens on inventory
  total_items = 0
  print('Inventory:')
  for item, quantity in inventory.items():
    print(str(quantity) + ' ' + item)
    total_items += quantity
  print("Total number of itens: " + str(total_items))

def addToInventory(inventory, addedItems):
  for item, quantity in addedItems.items():
    inventory[item] = inventory.get(item, 0) + quantity
  return inventory
  
inventory = {}

while True:
  print('Type item name (or type "done" to finish): ')
  item_name = input()
  if item_name == 'done' or item_name == '':
    break
  print('Quantity: ')
  quantity = int(input())
  inventory[item_name] = quantity

dragonLoot = {'gold coin': 50, 'rope': 1, 'ruby': 1}
inv = addToInventory(inventory, dragonLoot)

displayInventory(inv)