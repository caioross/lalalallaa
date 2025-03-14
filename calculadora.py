executar = True
while executar :
    escolhas = '''
        [1] ou [+] para Somar
        [2] ou [-] para Subtrair
        [3] ou [/] para Dividir
        [4] ou [*] para Multiplicar
        [5] para Sair
        '''
    print(escolhas)
    operador = input("Qual sua Opção?: ")
    valor01 = input("Qual o primeiro valor?: ")
    valor02 = input("Qual o segundo valor?: ")
    valor01 = int(valor01)
    valor02 = int(valor02)

    texto_sair = '''
        [1] Não, desejo sair!
        [2] Sim, desejo realizar outro calculo
    '''

    #Soma
    if operador == "1" or operador == "+" or  operador == "Somar":
        resultado = valor01 + valor02
        print("Resultado da soma: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro calculo? ")
        if operador == "1" :
            executar = False

    #Subtração
    if operador == "2" or operador == "Subtrair" or operador == "-":
        resultado = valor01 - valor02
        print("Resultado da subtração: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro calculo? ")
        if operador == "1":
            executar = False

    if operador == "3" or operador == "/" or operador == "Dividir": 
        resultado = valor01 / valor02
        print("Resultado é: " + str(resultado))
        print(textinho02)
        operador = input("Deseja realizar outra conta?")
        if operador == "1" :
            executar = False

    # Multiplicação
    if operador == "4" or operador == "*" or operador == "Multiplicar": 
        resultado = valor01 * valor02
        print("Resultado é: " + str(resultado))
        print(textinho02)
        operador = input("Deseja realizar outra conta?")
        if operador == "1" :
            executar = False

    #sair
    if  operador == "5" or  operador == "Sair":
        print("Obrigado!")
        executar = False
