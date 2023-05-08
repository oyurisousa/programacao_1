chars = []
with open('arq.txt','a') as file:
    value = True
    while True:
        value = input("")
        if value == '0': break
        file.write(value.strip()+'\n')
        
with open('arq.txt','r') as file:
    for x in file:
        line = x.strip()
        for i in x:
            if i not in [' ','\n']:
                chars.append(i)

for x in chars:
    print(x)