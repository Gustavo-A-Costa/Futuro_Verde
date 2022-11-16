# programa que abriga as funções responsáveis por calcular a emissão de cada veículo

def consumo_co2_gasolina(qtde_veiculos, media_km_litro=10.8, 
                         preco_medio_litro=4.69, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [int(custo_combustivel_ano), int(tonelada_co2_ano), int(conversao_coe)]

def consumo_co2_alcool(qtde_veiculos, media_km_litro=6.7, 
                         preco_medio_litro=3.49, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [int(custo_combustivel_ano), int(tonelada_co2_ano), int(conversao_coe)]

def consumo_co2_diesel(qtde_veiculos, media_km_litro=7.9, 
                         preco_medio_litro=5.32, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [int(custo_combustivel_ano), int(tonelada_co2_ano), int(conversao_coe)]

def consumo_co2_eletrico(qtde_veiculos, media_km_litro=6.93, 
                         preco_medio_litro=0.16, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [int(custo_combustivel_ano), int(tonelada_co2_ano), int(conversao_coe)]

def comparacao(lista1, lista2):
    lista_retorno = []
    for i in range(0, len(lista1)):
        variacao = int(lista1[i]) - int(lista2[i]) 
        if int(lista1[i]) > int(lista2[i]):
            porcentagem = int(- 100 * variacao / int(lista1[i]))
        else:
            porcentagem = int(100 * variacao / int(lista1[i]))
        
        texto = f"""{variacao} ({porcentagem}%)"""
        
        lista_retorno.append(texto)

    retorno = f"""{lista_retorno[0]} / {lista_retorno[1]} /\n {lista_retorno[2]} / {lista_retorno[3]}"""
    
    return retorno



