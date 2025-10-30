while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada de número inválida. Por favor, digite apenas números.")
        continue

    operacao = input("Digite a operação (+, -, *, /): ").strip()

    try:
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            raise ValueError
        
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break  # Sai do loop após sucesso

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Operação inválida. Use apenas +, -, *, ou /.")