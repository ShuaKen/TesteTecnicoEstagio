string = input("Informe uma string: ")

# Contar a quantidade de a
contador = string.lower().count('a')

# Verificar se 'a' existe na string
if contador > 0:
    print(f"A letra a aparece {contador} vez na string.")
elif contador >=1:
    print(f"A letra a aparece {contador} vezes na string.")
else:
    print("A letra a não está aparece na string.")
