# Exercício 17
'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math

valor_lata_em_reais = 80
valor_galao_em_reais = 25
cobertura_de_m2_por_litro = 6
volume_lata_em_litros = 18
volume_galao_em_litros = 3.6

tamanho_area_em_m2 = float(input("Digite o tamanho da área a ser pintada, em metros quadrados: "))

cobertura_de_m2_por_lata = cobertura_de_m2_por_litro * volume_lata_em_litros
cobertura_de_m2_por_galao = cobertura_de_m2_por_litro * volume_galao_em_litros

qtde_latas_a_serem_compradas = tamanho_area_em_m2 / cobertura_de_m2_por_lata
qtde_galoes_a_serem_comprados = tamanho_area_em_m2 / cobertura_de_m2_por_galao

valor_total_lata = qtde_latas_a_serem_compradas * valor_lata_em_reais
valor_total_galao = qtde_galoes_a_serem_comprados * valor_galao_em_reais

print(f"Se sua área tem {tamanho_area_em_m2} metros quadrados, te trago duas opções:\n{20*"==="}")
print(f"Podes levar {qtde_latas_a_serem_compradas:.2f} latas, por um valor de R${valor_total_lata:.2f}.")
print(f"Podes levar {qtde_galoes_a_serem_comprados:.2f} galões, por um valor de R${valor_total_galao:.2f}.")
