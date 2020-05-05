import tkinter #modulo da GUI
import os #modulo para manipular arquivos
import json

#definicoes das variaveis globais
comprimento_pagina_principal = 1200
altura_pagina_principal = 700
numero_de_frames_de_navegacao = 6

#definicoes da classe principal
root = tkinter.Tk()#inicia a classe/janela principal
root.title("JSON GUI")#titulo da janela principal
root.geometry("{}x{}".format(comprimento_pagina_principal, altura_pagina_principal))#define tamanho da janela atravéz de uma string formatada


#essa funcao recebe o caminho de uma pasta e cria um frame que possui
#uma listbox para vizualizar e selecionar pastas e arquivos
def cria_frame_de_navegacao_em_pastas(caminho=""):
    if caminho != "":
        comprimento_novo_frame = comprimento_pagina_principal/numero_de_frames_de_navegacao
        altura_novo_frame = 300
        novo_frame = tkinter.Frame(root, width=comprimento_novo_frame, height=altura_novo_frame)
        novo_frame_listbox = tkinter.Listbox(novo_frame, width=25, height= 20)
        novo_frame_listbox.bind('<<ListboxSelect>>', cuida_item_selecionado)

        #esse for loop insere os conteudos do "caminho" dado na listbox
        conteudo_da_pasta = os.listdir(caminho)
        novo_frame_listbox.insert(tkinter.END, caminho)
        for index, arquivo in enumerate(conteudo_da_pasta):
            novo_frame_listbox.insert(tkinter.END ,arquivo)

        novo_frame_listbox.pack()
        return novo_frame


def cuida_item_selecionado(evento):
    listbox_selecionada = evento.widget
    index = int(listbox_selecionada.curselection()[0])
    item_selecionado = listbox_selecionada.get(index)


frame_teste = cria_frame_de_navegacao_em_pastas("../")
frame_teste.pack()
root.mainloop()
