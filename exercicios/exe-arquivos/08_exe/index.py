preco_compras = []
with open('compras.txt',"r") as compras:
    for item in compras:
        item = item.split('-')
        preco_compras.append(int(item[1].strip()))
        
print(f"Total = {sum(preco_compras)}")