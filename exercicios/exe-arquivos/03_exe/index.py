import os
print("usaremos como base a pasta 'files'")

file_name1 = input('digite o nome do arquivo 1: ')
file_name2 = input('digite o nome do arquivo 2: ')

if os.path.exists(f'files/{file_name1}') and os.path.exists(f'files/{file_name2}'):
    with open(f'files/{file_name1}|{file_name2}','a') as file:
        with open(f'files/{file_name1}','r') as file1:
            content1 = file1.read()
        with open(f'files/{file_name2}','r') as file2:
            content2 = file2.read()
        if os.path.exists(f'files/{file_name1}|{file_name2}'):
            print("essa mesclagem já foi feita anteriormente!")
        else:
            file.write(content1+content2)
else:
    print("um ou mais arquivos não existe")
