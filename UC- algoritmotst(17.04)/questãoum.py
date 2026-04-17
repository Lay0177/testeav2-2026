#Questão um

print("Hello, Word!")

#Questão dois

idade = int(input("Quantos anos você tem?"))

if idade >= 16:
    print("Pode votar!")

else:
    print("Ainda não pode voltar!")

#Questão três

total = 0

while True:
    itens = float(input("Qual o valor dos itens?"))
    if itens == 0:
      break

total += itens

print(f"Total da compra: R$", {itens})

#Questão 4

def imc(peso,altura):

try:
     peso =float(input("Digite seu peso"))
     altura = float(input("Digite sua altura"))

     imc = peso / (altura ** 2)

    print(f"Seu IMC é: {imc:.2f}")
        
    if imc < 18.5:
        print("Categoria: Magro")
    elif imc <= 29.9:
       print("Categoria: Normal")
    else:
        print("Categoria: Obesidade")

except TypeError:
    print("Entrada inválida")
    
imc()

#Questão onze

lista =["Lívia-15, Layane-16, Baptysta-17, Letícia-18,Professor-19"]
print("A lista é ", lista) 

#Questão 10

frase = input("Digite uma frase: ")
vogais = "aeiou"
print(f"A frase possui {len(frase)} vogais.")

#Questão 5
amigos = ["Ana", "Carlos", "João"]

quantidade = len(amigos) 

print(f"Quantidade de amigos: {quantidade}")

if quantidade % 2 == 0:
    print("O número de amigos é PAR.")
else:
    print("O número de amigos é ÍMPAR.")


