# programa que abriga as funções responsáveis por calcular a emissão de cada veículo

def consumo_co2_gasolina(qtde_veiculos, media_km_litro=8.3, 
                         preco_medio_litro=2.67, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [custo_combustivel_ano, tonelada_co2_ano, conversao_coe]

def consumo_co2_alcool(qtde_veiculos, media_km_litro=8.3, 
                         preco_medio_litro=2.67, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [custo_combustivel_ano, tonelada_co2_ano, conversao_coe]

def consumo_co2_diesel(qtde_veiculos, media_km_litro=8.3, 
                         preco_medio_litro=2.67, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [custo_combustivel_ano, tonelada_co2_ano, conversao_coe]

def consumo_co2_eletrico(qtde_veiculos, media_km_litro=8.3, 
                         preco_medio_litro=2.67, kms_rodados=38000,
                         fator_co2 = 8.3, fator_coe = 0.021):

    custo_combustivel_ano = (kms_rodados * qtde_veiculos / media_km_litro) * preco_medio_litro
    tonelada_co2_ano = (kms_rodados * qtde_veiculos * fator_co2)
    conversao_coe = tonelada_co2_ano * fator_coe

    return [custo_combustivel_ano, tonelada_co2_ano, conversao_coe]