from inteligente import *

velocidade = 50
au = + 10
dim = - 10


opcao = input("Digite A para quando quiser aumentar a velocidade, ou digite D para diminuir a velocidade")

if(opcao =="A"):
    velocidade = Aumentar(velocidade)
    print(f"Sua velocidade atual é de {velocidade}")
elif(opcao =="D"):
    velocidade = Diminuir(velocidade)
    print(f"Sua velocidade atual é de {velocidade}")
else:
    print("Digete algo valido")