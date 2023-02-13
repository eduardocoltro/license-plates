import os
from threading import Timer
import time
import unicodedata
import Veiculo
from tqdm import tqdm


class Operações:
    def __init__(self):
        self.vector = [None, None, None, None]

    def Hash(self, value):

        determinante = value[:3]

        if determinante >= "AAA" and determinante <= "BEZ":
            return 0
        elif determinante >= "GKJ" and determinante <= "HOK":
            return 1
        elif determinante >= "IAQ" and determinante <= "JDO":
            return 2
        elif determinante >= "JKS" and determinante <= "JSZ":
            return 3
        else:
            return None

    
    def Put(self, value):

        estados = ["PR", "MG", "RS", "BA"]
        posicao = self.Hash(value.placa)
        item, contagem = self.Get(value.placa)

        lista = [value.placa, value.marca, value.modelo, value.proprietario]
        for i in lista:
            if i == "" or i == None:
                return "\nPreencha todos os campos!"

        if posicao != None:
            if self.vector[posicao] != None:
                if(item != None): 
                    return "Valor já inserido"
                self.vector[posicao] = [self.vector[posicao], (value.placa, value.lista(estados[posicao]))]    
            else:
                self.vector[posicao] = (value.placa, value.lista(estados[posicao]))
        else:
            return "Registro não pode ser inserido"
        return "Registro inserido com sucesso"

    def Get(self, key):
        contagem = 0
        valor = self.Hash(key)
        if valor != None and self.vector[valor] != None:
            if(self.vector[valor][0] == key):
                return self.vector[valor], contagem
            else:
                for item in self.vector[valor]:
                    if key == item[0]:
                        return item, contagem
                    else:
                        contagem +=1
            return None, None
        else:
            return None, None
    
    def Delete(self, key):
        item, contagem = self.Get(key)
        valor = self.Hash(key)
        if valor != None:
            if self.vector[valor] != None and item != None:
                if self.vector[valor] == item:
                    self.vector.pop(valor)
                    return "Registro removido com sucesso"
                else:
                    self.vector[valor].pop(contagem)
                    return "Registro removido com sucesso"
        else:
            return "Registro não existe na lista"
    
    def DadosFormatados(self, key, tipo=None):

        valor, contagem = self.Get(key)
        lista = ["placa", "modelo", "marca", "proprietario", "estado"]
        
        if tipo != None:
            tipo = unicodedata.unidecode(tipo).lower()

        if tipo != None and tipo not in lista:
            return "Campo escolhido inválido"

        if valor != None:

            placa = valor[0]
            marca = valor[1][0] 
            modelo = valor[1][1]
            proprietario = valor[1][2]
            estado = valor[1][3]

            if tipo == None:
                return " placa: {}\n marca: {}\n modelo: {}\n proprietario: {}\n estado: {}".format(placa, marca, modelo, proprietario, estado)
            else:
                if tipo == 'placa':
                    return placa
                elif tipo == 'marca':
                    return marca
                elif tipo == 'modelo':
                    return modelo
                elif tipo == 'estado':
                    return estado
                else:
                    return proprietario
        else:
            return "Registro não encontrado"
    
    def MenuPrincipal(self):
        cnt = True
        while cnt == True:
            os.system('cls')
            print("Menu:\n (1) Buscar Registro\n (2) Inserir Registro\n (3) Excluir Registro\n (4) Sair")
            answer = input("R: ")
            for i in tqdm(range(100)):
                time.sleep(0.01)

            if answer == "1":
                answer1 = input("Insira a placa: ")
                os.system('cls')
                print("Opções:\n (1) Buscar todas as informações\n (2) Buscar informação unica")
                answer3 = input("R: ")

                if answer3 == "1":
                    os.system('cls')
                    print(self.DadosFormatados(answer1))
                    time.sleep(6)

                elif answer3 == "2":
                    os.system('cls')
                    print("Digite a opção desejada:\n Placa\n Marca\n Modelo\n Proprietario\n Estado")
                    answer4 = input("R: ")
                    os.system('cls')
                    print(self.DadosFormatados(answer1, answer4))
                    time.sleep(3)

                else:
                    os.system('cls')
                    print("Opção inválida")
                    time.sleep(1)

            elif answer == "2":
                os.system('cls')
                print("Cadastre as informações a seguir:\n")
                placa = input("Placa do Veiculo: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                proprietario = input("Proprietario: ")
                os.system('cls')              
                print(self.Put(Veiculo.Veiculo(placa, marca, modelo, proprietario)))
                time.sleep(8)

            elif answer == "3":
                os.system('cls')
                answer5 = input("Cadastre o registro a ser removido (Placa do veiculo): ")
                os.system('cls')
                print(self.Delete(answer5))
                for i in tqdm(range(100)):
                    time.sleep(0.01)
            
            elif answer == "4":
                break
            else:
                print("Opção inválida")
                time.sleep(2)
