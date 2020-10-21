import Module_secondary as calc
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

print("Escolha um numero para executar determinada operação com os números digitados anteriormente:\n"
      "1 - Soma\n"
      "2 - Subtrair\n"
      "3 - Multiplicação\n"
      "4 - Dividir\n")

op = int(input())
print(op)
if(op == 1):
      print(calc.add(a, b))
elif(op == 2):
      print(calc.sub(a, b))
elif(op == 3):
      print(calc.mult(a, b))
elif(op == 4):
      print(calc.div(a, b))
else:
      print("Valor digitado invalido")

