import tkinter
import json

#definicoes das variaveis globais
comprimento = 600
altura = 450

#definicoes da classe principal
root = tkinter.Tk()#inicia a classe/janela principal
root.title("JSON GUI")#titulo da janela principal
root.geometry("{}x{}".format(comprimento, altura))#define tamanho da janela atravéz de uma string formatada

root.mainloop()

with open('test.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print("Texto: ", data['Capitulo1']['Boas-vindas']['Bem-vindo']['Texto'])
