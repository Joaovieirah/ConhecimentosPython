Prova

par = float(input("Digite um valor?"))
if par % 2 == 0:
    print ("Esse número é par")
else:
    print ("Esse valor não é par")


positivo = float(input("Digite um valor!"))
if positivo < 0:
    print ('Esse número é negativo')
else:
    print ("Esse número é positivo")


iguais1 = float(input("Me fale o primeiro valor"))
iguais2 = float(input("Me fale o segundo valor"))

if (iguais1 == iguais2):
    print("Os valor são iguais")
else:
    print("os valores são diferentes")


valor = int(input("Digite um valor"))

if ( valor > 25 and valor < 37):
    print("Esse numero é valido")
else:
    print("Esse valor não é valido")


valor1 = float(input("Digite o primeiro valor"))
valor2 = float(input("Digite o segundo valor"))

if valor1 % valor2 == 0:
    print("Os valores são múltiplos.")

else:
    print("Os valores não são múltiplos")


valor1 = int(input("Digite um valor"))
valor2 = int(input("Digite outro valor"))
valor3 = int(input("Digite outro valor"))
valor4 = int(input("Digite outro valor"))

if (valor1 > valor2 and valor1 > valor3 and valor1 > valor4):
    print(f'{valor1} é maior que os outros números')
elif (valor2 > valor1 and valor2 > valor3 and valor2 > valor4):
    print(f'{valor2} é maior que os outros números')
elif (valor3 > valor1 and valor3 > valor2 and valor3 > valor4):
    print(f'{valor3} é maior que os outros números')
elif (valor4 > valor1 and valor4 > valor2 and valor4 > valor3):
    print(f'{valor3} é maior  que os outros números')
else:
    print("Tente novamente")


valor1 = float(input("Digite um valor"))
valor2 = float(input("Digite um valor"))
valor3 = float(input("Digite um valor"))
valor4 = float(input("Digite um valor"))

soma = (valor1 + valor2 + valor3 + valor4)
print(soma)



valor1 = int(input("Digite o primeiro valor"))
valor2 = int(input("Digite o segundo valor "))

resto = (valor1 % valor2)
print(f"O resultado dos valores  {valor1} e {valor2} é {resto}")



valor = float(input("Digite um valor"))
expoente = float(input("Digite um expoente"))

juntos = (valor ** expoente)

print(juntos)


altura1 = float(input("Qual sua altura"))
altura2 = float(input("Qual sua altura"))
altura3 = float(input("Qual sua altura"))

media = (altura1 + altura2 + altura3) / 3
print (f" Sua média é: {media}")



temperatura = float (input('Qual a temperatura?'))

converta = ((temperatura - 32) * 5/9)
print (f"A temperatura é {converta}")


def calcular():
        bruto = float(input("fale o salario bruto"))
        percentual = float(input("digite o desconto"))
        desconto = bruto * (percentual / 100)
        liquido = bruto - desconto
        print(f"O salrio liquido é {liquido}")
calcular()


def calcular():
    distancia = float(input("Digite a distancia"))
    tempo = float(input("Digite o tempo"))
    media = distancia / tempo
    print (f"Sua velocidade media é {media}")
calcular()