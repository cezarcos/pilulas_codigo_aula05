def validarSenha(s): 
    if len(s) < 8:
        return 'Senha inválida, muito curta.'
    
    temNumero = False
    temMaiuscula = False
    simbolos = '!@#$%&'
    temSimbolo = False 
    
    for c in s: 
        if c == ' ':
            return 'Senhainválida, não pode ter espaços'
        if c >= '0' and c <= '9':
            temNumero = True 
        if c >= 'A' and c<= 'Z':
            temMaiuscula = True 
        if c in simbolos:  
            temSimbolo = True     
        
            
    if temNumero == False:
        return 'Senha inválida, precisa de um num. pelo menos' 
    if not temMaiuscula: 
        return 'Senha inválida, precisa de uma letra maiscula' 
    return 'Senha válida'       
                      
#main
senha = input('Digite a senha:')
r = validarSenha(senha)
print(r)