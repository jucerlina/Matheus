preco= float(input("digite seu preço:"))
desconto=float(input("digite seu desconto:"))
valor_desconto =( desconto * preco) / 100

preco_final = preco - valor_desconto
print( preco_final)