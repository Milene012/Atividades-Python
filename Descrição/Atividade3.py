"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

nome = input("Escreva F - Feminin, M - Masculino, Sexo Inválido").upper()

if nome == "F":
print("É Feminino")

elif nome == "M":
print("É Masculino")

else:
    print("Sexo é inválido")