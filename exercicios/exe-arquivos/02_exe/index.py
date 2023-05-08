import os
print("usaremos como base a pasta 'files'")
file_name = input('digite o nome do arquivo: ')
if os.path.exists(f'files/{file_name}') :
    count = 0
    with open(f'files/{file_name}','r') as file:
        for line in file:
            count += 1
    print(f"linhas:{count}")
else:
    print("o arquivo não existe")
