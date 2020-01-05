itemsset =[]
name=''   
while name!='done':
    item={}
    name = input("Item enter \"done\" when finished: ")
    if (name == 'done'):
        break
    price = float(input("Enter Price of item "))
    quantity = int(input("Enter Quantity"))
    item["name"] = name
    item["price"] = price
    item["quantity"] = quantity
    itemsset.append(item)
#print(itemsset)
print("-"*30)
print("receipt")
print("-"*30)

total=[]

for item in itemsset:
    invoice = item["price"] * item["quantity"]
    total.append(invoice)
    print(item["quantity"],item["name"],item["price"])
print("-"*30)
grand_total = sum(total)
print("TOTAL PRICE",grand_total)