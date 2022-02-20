valor_total_conta = float(input("Quanto deu a conta no total? "))

chosen_percentage = float(int(input("Qual a porcentagem? 10, 12 ou 15? ")) / 100)

valor_final = valor_total_conta + (valor_total_conta * chosen_percentage)

qtd_pessoas = int(input("A conta será dividida para quantos? "))

valor_dividido = valor_final / qtd_pessoas

print(f"Valor da conta: R$ {valor_total_conta}\nValor final: R$ {valor_final}\nDivido para {qtd_pessoas} "
      f"fica {valor_dividido} para cada pessoa")
