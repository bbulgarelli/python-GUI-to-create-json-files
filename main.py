import tkinter

#definicoes das variaveis globais
comprimento = 600
altura = 450

#definicoes da classe principal
root = tkinter.Tk()#inicia a classe/janela principal
root.title("JSON GUI")#titulo da janela principal
root.geometry("{}x{}".format(comprimento, altura))#define tamanho da janela atravéz de uma string formatada
              


root.mainloop()
