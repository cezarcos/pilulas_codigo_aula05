def verificarValores(): 
    anterior = float(input('Leitura 1: '))
    for i in range(4):
        atual = float(input(f'Leitura {i+2}: '))
        if atual <= anterior:
            return False 
        anterior = atual 
    return True 

#main 
if verificarValores():
    print('crescente')   
else:
    print('instável')  
           