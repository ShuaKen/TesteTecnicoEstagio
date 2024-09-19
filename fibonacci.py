numero = input("Informe um número: ")

# Verificar se o input é um numero
if numero.isdigit():
    numero = int(numero)
    
    # Inicializar a sequência de Fibonacci
    a, b = 0, 1
    fib_sequence = []

    # Gerar a sequência de Fibonacci até o número informado
    while a <= numero:
        fib_sequence.append(a)
        a, b = b, a + b

    # Verificar se o número pertence à sequência
    if numero in fib_sequence:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
else:
    print("Por favor, informe um número válido.")
