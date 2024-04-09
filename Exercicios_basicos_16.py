# Exercício 16
'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados.
A tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
valor_lata_tinta_em_reais = 80

cobertura_de_m2_por_litro = 3

volume_lata_tinta_em_litros = 18

cobertura_em_m2_por_lata = cobertura_de_m2_por_litro * volume_lata_tinta_em_litros

tamanho_area_em_m2 = int(input("Digite, em metros quadrados, o tamanho da área a ser pintada: "))

qtde_latas_a_serem_compradas =  tamanho_area_em_m2 / cobertura_em_m2_por_lata

preco_total = valor_lata_tinta_em_reais * qtde_latas_a_serem_compradas

print(f"Para sua área, você precisará comprar {qtde_latas_a_serem_compradas:.2f} latas de tinta.")
print(20*"===")
print(f"O valor total de sua compra será de {preco_total:.2f} reais.")



