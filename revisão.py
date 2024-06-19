#python é uma linguagem que conversa com a maquina 
#algoritimo -> sequencia de passos para  executar uma tarefa

#3 Estruturas possiveis no algoritmo
#-estrutural (sequencia de passos continuos)
#-condicinal (DESISAO- vou executar um scrip se acontecer X e outro se y)
#-repetição (permita executar varias vezes o mesmo codigo)

#variaveis
#espaços no armazenamento que pode armazenar dados para executar

#Int, Float, String e Boolean
#Int : Armazena valores  inteiros
#Float : Numeros decimais
#String : cadeia de caracteres -> (não vou fazer calculo)
#Bollean : é o poligrafo que aceita dois valores true e false

#Regras -> uma String deve ser entre "", '', -> (ex:"house's fer")
#Regras -> tem que tem um valor e um ponto (ex:1.--)
#Regras -> existe somento um valor (ex:100)

#o pyhon tem tipagem dinamica, ou seja ele entende apartir do valor o tipo da variavel

# curso = "Manufatura digital"
#A  variavel "curso" recebe o valor ("Manufatura Digital")

# print(type(curso))
# #type mostra o tipo da classificação da variavel

# #exibir no terminal -> comando print
# print ("olá eu sou o print, estou executando seu py")

# #para conversar com o usuario eu uso o input
# altura = float(input("Me fale sua altura"))
# #a variavel altura recebe um valor quebrado de altura
# print (f"Sua altura é {altura}")
# #exibe pra mim a "FORMATAÇÃO" do texto com o valor de uma variavel

# #nome = input("digite seu nome")
# #print(nome)

# nome = input("digite seu nome")
# sobrenome = input("digite seu sobrenome")
# print(nome + sobrenome)
#Quando colocaos o sinal de "+" em um string ele junta os dois nome, enquanto em calculo ele soma

# print ("Cadastro de uma pessoa")
# nome = input("Digite seu nome")
# idade = input("Digite sua idade")
# endereco = input("Digite seu endereço")
# distancia = input("Digite a distância percorrida")
# nascimento = input("Digite seu nascimento")
# cpf = input("Digite seu cpf")
# print(nome, idade, endereco, cpf, distancia, nascimento)




#Estruturas de algoritmo condicional
#Executo alguma instrução e acordo com os dados que tenho (ex: só posso me alistar no exercito "se" for maior de idade)

#Para usar o "if" e "else", eu tenho que saber quais as opções que eu tenho!

# if (idade >= 18):
# #se a idade for maior ou igual a 18 ENTAO(:) exiba a mensagem
#     print("Você já pode se alistar")
# else:
# #se a idade não for maior ou igual a 18 ENTÃO(:) exiba a mensagem
#     print("Você é menor de idade")


# nota = float(input("Digite a sua nota:"))

# if (nota > 5):
#     print("Você passou")
# elif (nota == 5):
#     print("Você está no conselho")
# else:
#     print("Você está reprovado")

#Exercicios
#se o salário for maior que 1500 adicione 500
#se o salário for maior do que 2000 some 400
#se o salário for maior que 3000 some 30

valor = float(input("Digite seu salario"))

if(valor < 1500):
    print("Você é pobre, não merece nada")

elif(valor > 1500 and valor < 2000):
    soma = (valor + 500)
    print(soma)

elif(valor > 2000 and valor < 3000):
    soma = (valor + 400)
    print (soma)

elif(valor > 3000 and valor < 5000):
    soma = (valor + 300)
    print(soma)

elif(valor < 5000):
    print("tabom de dinheiro né, você nem estudou pra ter tudo isso")

else:
    print("Pra que você quer mais dinheiro??")