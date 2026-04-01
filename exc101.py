def calculadora_simples():
    print("--- Calculadora em Python ---")
    
    
    try:
        # 1. Pedir o primeiro número
        num1 = int(input("\nDigite o primeiro número: "))

        # 2. Pedir o operador
        operador = input("Escolha a operação (+, -, *, /) ou digite 'sair' para finalizar: ").strip()

        if operador.lower() == "sair":
            print("Fechando a calculadora... até logo!")
            

        # 3. Pedir o segundo número
        num2 = int(input("Digite o segundo número: "))

        # 4. Realizar a operação 
        if operador == "+":
            resultado = num1 + num2

        elif operador == "-":
            resultado = num1 - num2

        elif operador == "*":
            resultado = num1 * num2

        elif operador == "/":
            if num2 == 0:
                print("Erro: Não é possível dividir por zero!")
                
            
            # Usando // para divisão inteira conforme o código original
            resultado = num1 // num2
        else:
            print("Operador inválido!")
            

        print(f"Resultado: {num1} {operador} {num2} = {int(resultado)}")
        

    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")

    print("--- Fim da operação ---")


calculadora_simples()