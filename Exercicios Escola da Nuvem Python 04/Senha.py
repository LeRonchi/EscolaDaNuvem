while True:
    senha = input("Crie uma senha (mínimo 8 caracteres e 1 número) ou digite 'sair': ")
    
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    tem_oito_caracteres = len(senha) >= 8
    
    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break
            
    if tem_oito_caracteres and tem_numero:
        print("\n--- Resultado ---")
        print("Senha forte criada com sucesso!")
        break
    else:
        print("\nAviso: Senha fraca. Tente novamente.")
        if not tem_oito_caracteres:
            print("- Falta ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("- Falta conter pelo menos um número.")