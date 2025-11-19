from repository.banco_de_dados import BancoDados
from models.conta import Conta
from models.conta_corrente import ContaCorrente

db = BancoDados()

def listar(contas):
    print("\n--- LISTA DE CONTAS ---")
    for c in contas:
        print(f"{c.numero} - saldo: {c.saldo}")

def criar_conta(contas):
    tipo = input("Tipo [1] conta | [2] Conta Corrente: ")

numero = input("Número da conta: ")
titular = input("Titular: ")
saldo = float(input("Saldo inicial: "))

if tipo == "2":
    limite = float(input("Limite:  "))
    contas.append(ContaCorrente(numero, titular, saldo, limite))
else:
    contas.append(Conta(numero, titular, saldo))

print("Conta criada com sucesso!")

def editar(contas):
    numero = input("Número da conta para editar: ")
    