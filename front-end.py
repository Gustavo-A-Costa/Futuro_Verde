# "Futuro Verde", por Gustavo, Gustavo, Paulo e Tatiane - UNIP 2022

from PySimpleGUI import PySimpleGUI as sg
# sendo o PySimpleGUI a biblioteca utilizada para fazer o front end
from time import sleep
# importei a função sleep da biblioteca time para testar o programa de forma mais lenta
import funcoes
# FUNCAO PARA TESTAR O MÓDULO COMPLEMENTAR



#________________________________________________
#____________ELEMENTOS DO FRONT END______________
#________________________________________________

#____________ELEMENTOS GERAIS____________________
fonte = "Bahnschrift" # fonte do programa
resolucao = (500, 650) # resolucao do programa
titulo = "APS UNIP - Ciência da Computação v1.0" # titulo da janela
sg.theme("Black") # paleta de cores da janela

iteracao_clique = 0 # define se é a primeira vez que o botão tá sendo apertado ou não,
                    # para exibir o popup de comparação

#____________IMAGENS DOS BOTÕES__________________
# Não é possível colocar imagens nos botões como nos layouts.
# Então, as convertemos para base 64, que os botões do sg podem ler, atraves do programa "conversor_base64.py"

# teste_botao_opcao1 = b'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'
# teste_botao_opcao2 = b'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'
# teste_botao_opcao3 = b'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'

# As strings base 64 das imagens dos botões são tão longas que preciso colocá-las num arquivo de texto.
# Aí posso fazer o Python ler esses arquivos :)

with open('relatorios_botao.txt', encoding='utf-8') as arquivo:
            relatorios_botao = arquivo.read()

with open('editar_botao.txt', encoding='utf-8') as arquivo:
            editar_botao = arquivo.read()

with open('creditos_botao.txt', encoding='utf-8') as arquivo:
            creditos_botao = arquivo.read()


#_____________LAYOUTS____________________________
# Aqui estão as "telas" do programa. Elas são guardadas em forma de lista e é o que o PySimpleGUI lê para
# montar a janelinha 
layout_titulo = [
                 [sg.Text("SELECIONE A RESOLUÇÃO DO PROGRAMA", font=fonte, size=(100,2),
                          justification='center')],
                 [sg.Image('logo2.png', pad=20)],
                 [sg.Radio('Resolução 1: 1200x700', "RADIO1", default=False,
                           size=(22, 4), font=fonte, key="RES1")],
                 [sg.Radio('Resolução 2: 1000x600', "RADIO1", default=True,
                           size=(22, 4), font=fonte, key="RES2")],
                 [sg.Button('FECHAR', font=fonte, key="FECHAR1_KEY", size=(8,1), pad=20),
                  sg.Button('INICIAR', font=fonte, key="INICIAR_KEY", size=(8,1), pad=20)],
                 [sg.Text("Por Gustavo, Gustavo, Paulo e Tatiane", font=fonte, size=(100,1), pad=10,
                          justification='center')]
                ]

layout_menu = [
                 [sg.Text("FUTURO VERDE - MENU PRINCIPAL", font=fonte, size=(100,1),
                          justification='center', pad=5)],
                 [sg.Image('banner.png', size=(600, 250), pad=40)],
                 [sg.Button('', image_data=relatorios_botao, key='RELATORIOS_BOTAO_KEY', size=(150,150), image_size=(150,150)), 
                  sg.Button('', image_data=editar_botao, key='EDITAR_BOTAO_KEY', size=(150,150), image_size=(150,150)),
                  sg.Button('', image_data=creditos_botao, key='CREDITOS_BOTAO_KEY', size=(150,150), image_size=(150,150))],
              ]
              
layout_relatorios = [
                     [
                     sg.Image('bannerpeq.png', size=(300, 150), pad=1),
                     sg.Text("DADOS DA FROTA ATUAL", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("FROTA PROPOSTA", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("COMPARAÇÃO", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     ],
                     [
                     sg.Text("INSIRA OS DADOS CORRESPONDENTES À FROTA:", font=fonte, size=(25,2),
                            justification='left', pad=5),                     
                     sg.Text("", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     ],
                     [
                     sg.Text("GASOLINA:", font=fonte, size=(25,2),
                            justification='left', pad=5),                     
                     sg.Text("GASOLINA", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("GASOLINA", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("GASOLINA", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     ],
                     [
                     sg.Input("", font=fonte, size=(25,2),
                            justification='left', pad=5),                     
                     sg.Text("GASOLINA", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("GASOLINA", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     sg.Text("GASOLINA", font=fonte, size=(25,1),
                          justification='center', pad=5),
                     ],


                    ]

layout_editar =  [
                 [sg.Text("FUTURO VERDE - EDITAR / CADASTRAR EMPRESA", font=fonte, size=(100,1),
                          justification='center', pad=5)],
                 [sg.Image('banner.png', size=(600, 250), pad=40)]
                 ]

creditos = """
            Software "FUTURO VERDE" e empresa fictícia "VEMLOGO" por:

            Gustavo Costa - RA: 
            Gustavo Silva - RA: 
            Paulo Cruz - RA: 
            Tatiane Cruz - RA: 

            Turma CC1Q07 / CC2Q07 - UNIP - 2022
            """

layout_creditos = [
                    [sg.Text("FUTURO VERDE - CRÉDITOS", font=fonte, size=(100,1),
                              justification='center', pad=5)],
                    [sg.Image('logo2.png', size=(300, 300)), sg.Text(creditos, font=fonte, size=(100,10),
                                                                               justification='center', pad=5)],
                    [sg.Image('unip.png')]
                  ]

#______________JANELA E LOOP LÓGICO______________
janela = sg.Window(titulo, layout_titulo,
                   element_justification='c', size=resolucao)

while True:
    # mecanismo para ler as keys dos botões e verificar o que acontece na tela.
    # O "While True" serve para que o programa leia as informações da tela a todo momento
    eventos, valores = janela.read()
    # a variavel valores é a variável que recebe a key de um botão quando o mesmo é apertado

    # sleep(1)
    print(eventos, valores) # coloquei essa linha só para ver se tá tudo funcionando certinho

    # _________________________________ LEITURA DE BOTÕES _____________________________
    # leitura do botao de fechar na primeira tela
    if eventos == "FECHAR1_KEY":
        janela.close() # fecha a janela

    # leitura do botão de iniciar que leva para ao menu principal
    if eventos == "INICIAR_KEY":

        # ifs para a troca de resolução da tela___________________________________________

        if valores["RES1"] is True:
            resolucao = (1200, 700)

        if valores["RES2"] is True:
            resolucao = (1000, 600)

        # elif valores["RES3"] is True:
        #    resolucao = (1600, 900)

        #__________________________________________________________________________________

        janela.close() # fecha a janela
        layout = layout_menu # troca o layout para o layout desejado
        janela = sg.Window(titulo, layout,
                           element_justification='c', size=resolucao) # abre uma nova janela


    if eventos == "RELATORIOS_BOTAO_KEY":
        janela.close() # fecha a janela
        layout = layout_relatorios # troca o layout para o layout desejado
        janela = sg.Window(titulo, layout,
                           element_justification='c', size=resolucao) # abre uma nova janela

    if eventos == "EDITAR_BOTAO_KEY":
        janela.close() # fecha a janela
        layout = layout_editar # troca o layout para o layout desejado
        janela = sg.Window(titulo, layout,
                           element_justification='c', size=resolucao) # abre uma nova janela

    if eventos == "CREDITOS_BOTAO_KEY":
        janela.close() # fecha a janela
        layout = layout_creditos # troca o layout para o layout desejado
        janela = sg.Window(titulo, layout,
                           element_justification='c', size=resolucao) # abre uma nova janela

    if eventos == "GERAR_RESULTADO_KEY":
        if iteracao_clique == 0:
            print('Primeiro clique!')
            sg.Popup(
                """
                DESEJA [...]
                """
                    )
            iteracao_clique = 1

        else:
            sg.Popup(
                """
                DESEJA [...]
                """
                    )
    if eventos == "EXIBIR_NUMEROS_KEY":
            sg.Popup(
                """
                NUMEROS ATUAIS [...]
                """
                    )

    # ________________________________________________________________________________

    # Essas duas linhas servem para que o programa encerre o loop While quando o programa é fechado
    if eventos == sg.WINDOW_CLOSED:
        break