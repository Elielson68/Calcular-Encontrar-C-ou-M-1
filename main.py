import os
def clear():
  return os.system('cls' if os.name == 'nt' else 'clear')
usu = "s"
while(usu=="s"):
  potencia = int(input("potência: "))
  valor = int(input ("valor: "))
  resultado = valor
  modulo = int(input("módulo: "))
  for x in range(1, potencia):
    resultado *= valor

  print("\nResultado: "+str(resultado)+"\n")
  print("Valor "+str(valor)+" elevado a "+str(potencia)+" ao modulo "+str(modulo))
  print("Algarismos: "+str(len(str(resultado))))
  print("Resultado mod: "+str(resultado%modulo)+"\n\n")
  usu = input("Reiniciar?\ns = sim, n = não\nR: ")
  clear()