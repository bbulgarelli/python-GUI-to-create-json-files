import json

#carrega o arquivo .json selecionado e armazena o objeto na variável data
def get_file(filePath):
    with open(filePath) as json_file:
        data = json.load(json_file)
        return data

#navega pelos objetos para se chegar a cada fala possível
def seleciona_texto():
    actualPath = get_file('./json_repo/test.json')

    print("Selecione o capítulo:")
    print_list(actualPath) #imprime as opções de capítulo disponível no arquivo json
    chapter = input() #armazena a escolha de capítulo pelo usuario
    options = create_list(actualPath) #cria uma lista com as chaves dos capítulos impressos
    selected = options[int(chapter)] #seleciona na lista criada o capítulo escolhido pelo usuário
    actualPath = actualPath[selected] #atualiza o path para uma camada mais interna do objeto
    print("\n")

    print("Selecione o diálogo:")
    print_list(actualPath)
    dialog = input()
    options = create_list(actualPath)
    selected = options[int(dialog)]
    actualPath = actualPath[selected]
    print("\n")

    print("Selecione o estado:")
    print_list(actualPath)
    state = input()
    options = create_list(actualPath)
    selected = options[int(state)]
    actualPath = actualPath[selected]
    print("\n")

    print("Texto selecionado:")
    print(actualPath["text"])
    print("\n")

#cria um array com as chaves no caminho selecionado
def create_list(path):
        return list(path.keys())

#imprime as escolhas de chaves com um identificador do input correspondente
def print_list(path):
    i = 0;
    for element in path.keys():
        print(i, ". ", element, sep='')
        i += 1
    return

def get_object_list(filePath, *args):
    source = get_file(filePath)
    for arg in args:
        source = source[arg]
    return list(source.keys())

lista = get_object_list('./json_repo/test.json', "Capítulo 0", "Despedida", "Tchau")
print(lista)
seleciona_texto()
