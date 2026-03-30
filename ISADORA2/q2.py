gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)


print(f"Total de gastos do João: R$ {total_joao}")
print(f"Total de gastos do Pedro: R$ {total_pedro}")

if total_joao > total_pedro:
    print("João gastou mais dinheiro ao longo do mês.")
elif total_pedro > total_joao:
    print("Pedro gastou mais dinheiro ao longo do mês.")
else:
    print("João e Pedro gastaram a mesma quantia.")