#Regra de negocio: Todo restaurante criado deve começar com o status: inativo

import os

restaurantes = [
        {"nome":"Praça", "categoria":"Japonesa", "ativo":False}, 
        {"nome":"Ventura", "categoria":"Italiana", "ativo":True},
        {"nome":"Passira", "categoria":"Geral", "ativo":False},
        {"nome":"DiretoAi", "categoria":"Geral", "ativo":True},
]


def exibir_nome_do_programa():
    """Essa função é responsável por exibir o titulo/logo/nome principal do programa"""
    print ("""

██████╗░██╗██████╗░███████╗████████╗░█████╗░░█████╗░██╗
██╔══██╗██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║
██║░░██║██║██████╔╝█████╗░░░░░██║░░░██║░░██║███████║██║
██║░░██║██║██╔══██╗██╔══╝░░░░░██║░░░██║░░██║██╔══██║██║
██████╔╝██║██║░░██║███████╗░░░██║░░░╚█████╔╝██║░░██║██║
╚═════╝░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝
       
""")
    
def exibir_opcoes():
    """Essa função é responsável por exibir as opções disponíveis no programa"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    """Essa função é responsável por finalizar a aplicação se o usuário selecionar esta opção"""
    exibir_subtitulo("Finalizar app")

def voltar_ao_menu_principal():
    """Essa função é responsável por retornar ao menu principal no fim de cada ação"""
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    """Essa função é responsável por criar um tratamento de erro caso o usuário digite um valor invalido que nao corresponda as opções"""
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Essa função é responsável por criar e exibir o subtitulo da opção selecionada"""
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante """
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restautante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria": categoria, "ativo":False}

    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Essa função é responsável por listar os restaurantes cadastrados"""
    exibir_subtitulo("Listando restaurantes")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """Essa função é responsável por alternar o estado do restaurante. Ou seja, ativar ou desativar"""
    exibir_subtitulo("Alterando o estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alterrar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]

            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")            

    voltar_ao_menu_principal()

def escolher_opcoes():
    """Essa função utiliza o match case e é responsável por escolher a opção que o usuario selecionou"""
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    """Função principal que inicia o programa"""
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__name__":
    main()

main()

