"""Faça um Programa que leia três números e mostre o maior deles."""

valor1 = int(input("Digite o 1° valor que você deseja comparar: "))
valor2 = int(input("Digite o 2° valor que você deseja comparar: "))
valor3 = int(input("Digite o 3° valor que você deseja comparar: "))
if(valor1 > valor2 and valor1 > valor3):
  print("O maior valor digitado é o:",valor1)
elif(valor1 < valor2 and valor3 < valor2):
  print("O maior valor digitado é o:",valor2)
elif(valor3 > valor1 and valor3 > valor2):
  print("O maior valor digitado é o:",valor3)
else:
  print("Os valores digitados são iguais!")