from collections import OrderedDict
n=int(input())
items = OrderedDict()

for i in range(n):
    lt=input().split()
    item_name = " ".join(lt[:-1])
    net_price = int(lt[-1])
    
    if item_name not in items:
        items[item_name] = net_price
    else:
        items[item_name] += net_price

for i,j in items.items():
    print(i,j)
