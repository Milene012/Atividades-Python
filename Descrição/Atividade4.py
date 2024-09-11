"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input ("digite uma letra:").upper()
if letra in"AEIOU":
    print ("a letra",letra, "é vogal")
else:
    print("a letra", letra "é consoante")