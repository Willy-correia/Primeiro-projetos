import os 
#biblioteca para finalizar programa

restaurantes = [{"nome":"Paulistano", "categoria":"Pizzaria", "ativo":False}, 
                {"nome":"Bolo no pote", "categoria":"Doceria", "ativo":True},
                {"nome":"Massa e cia", "categoria":"Italiano", "ativo":False}]
#Restaurantes que já estão no banco de dados do programa

def exibir_subtitulo(texto):
    #Esta função ela primeiramente apaga tudo o que está na tela (os.system("cls"))
    #Ela usa * para colocar em cima e em baixo do texto que veio de outra função
    #outputs:
    #Asteriscos + texto + asteriscos

    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha + "\n")

def voltar_para_menu_principal():
    #Esta função serve para que o usuário consiga voltar para a tela inicial e consiga escolher outra opção
    #Então ele apaga toda a tela e chama a função principal(main)

    input("\nDigite uma tecla para voltar para o menu principal ")
    os.system("cls")
    main()

def exibir_nome_do_programa():
    #Está função é onde fica o nome do aplicativo para poder ser usado onde quiser

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    #Esta função serve para que o usuario saiba as opções que pode/quer escolher
    #output:
    #cadastrar restaurante
    #lista de restaurante
    #ativar/desativar restaurante
    #sair

    print("1. 𝐶𝐴𝐷𝐴𝑆𝑇𝑅𝐴𝑅 𝑅𝐸𝑆𝑇𝐴𝑈𝑅𝐴𝑁𝑇𝐸")
    print("2. 𝐿𝐼𝑆𝑇𝐴 𝐷𝐸 𝑅𝐸𝑆𝑇𝐴𝑈𝑅𝐴𝑁𝑇𝐸𝑆")
    print("3. 𝐴𝑇𝐼𝑉𝐴𝑅/𝐷𝐸𝑆𝐴𝑇𝐼𝑉𝐴𝑅 𝑂 𝑅𝐸𝑆𝑇𝐴𝑈𝑅𝐴𝑁𝑇𝐸")
    print("4. 𝑆𝐴𝐼𝑅\n")

def finalizar_app():
    #apagar tudo o que está na tela principal e aparecer (finalizando app)
    exibir_subtitulo("Finalizando o app")

def opcao_invalida():
    #Serve para quando o usuário digita algo que não é esperado pelo programa
    #Mostra que a opção que el escolheu não é válida e chama a função "volta_para_menu_principal"
    exibir_subtitulo("opção inválida!")
    voltar_para_menu_principal()

def cadastrar_novo_restaurante():
    #Essa função é responsável por cadastrar um novo restaurante
    #Imputs:
    #- nome do restaurante
    #- Categoria
    
    #Output:
    #- Adicionar um novo restaurante a lista de restaurantes

    exibir_subtitulo("Cadastro de novos restaurantes:")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome" : nome_do_restaurante, "categoria" : categoria, "ativo" : False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    
    voltar_para_menu_principal()

def Listar_restaurantes():
    #Esta função serve para listar os restaurantes para o usuario
    #ele primeiramente chama a função para exibir o subtitulo
    #depois exemplifica o que cada nome la escrito significa (nome do restaurante/ categoria/ status)
    #ele como uma lista exemplifica cada restaurante com a sequencia (nome/ categoria/ status)
    #chama a função para voltar para o menu principal

    exibir_subtitulo("Lista dos restaurantes:")

    print (f"{"Nome do restaurante".ljust(22)} |{"Categoria".ljust(22)} |Status")
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativo" if restaurante["ativo"] else "Desativo"
        print(f"- {nome_do_restaurante.ljust(20)} |- {categoria.ljust(20)} |- {ativo}")
    
    voltar_para_menu_principal()

def alternar_estado_do_restaurante ():
    #essa função serve para alternar o status do restaurante (se for ativo fica inativo e se for inativo fica ativo)
    #primeiro ele exibe o subtitulo
    #Ele verifica se aquele restaurante esta dentro do nosso dicionário
    #Se ele estiver ele troca o seu estado e se não tiver ele mostra uma mensagem de "restaurante não encontrado"
    #Chama a função para voltar para o menu principal
    
    #Input:
    #nome do restaurante]

    #Output:
    #O restaurante {nome_restaurante} foi ativado com sucesso
    #O restaurante {nome_restaurante} foi desativado com sucesso
    #O restaurante {nome_restaurante} não foi encontrado

    exibir_subtitulo("Alternando o estado do restaurante:")

    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f" O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante ["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print (f"O restaurante {nome_restaurante} não foi encontrado")

    voltar_para_menu_principal()

def escolher_opcao():
    #escolher e executar exatamente o que é pedido e chamar a função específica para cada opção escolhida
    #se a opção não for nenhuma das que existem, leva para a funcão da opção inválida

    try:
        opcao_escolhida = int (input ("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            Listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante ()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    #A função main é a função principal
    #Primeiro ela limpa a tela

    #Depois chama 3 funções:
    # exibir nome do programa 
    # exibir opções
    # escolher opções

    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
    main ()
    #Esta função permite controlar a execução de código em módulos
    #permitindo que você escreva códigos que podem ser utilizados 
    #tanto de forma independente quanto como parte de um programa maior
