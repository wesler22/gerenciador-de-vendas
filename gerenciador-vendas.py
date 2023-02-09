print("=======LOJA DO WES========")
preco= float(input('Preço das compras: R$'))
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao=int(input('Escolha sua opção:'))
desconto= preco - (preco * 10/100)
desconto1= preco - (preco * 5/100)
juros = preco + (preco * 20/100)
if opcao == 1:
    print('O valor da sua compra com o DESCONTO será de {}'.format(desconto))
elif opcao == 2:
    print('O valor da sua compra com o DESCONTO de 5% será de {}'.format(desconto1))
elif opcao==3:
    parc1=preco / 2
    print('O valor de sua compra será de {} no total e parcelado será 2x de {}:'.format(preco,parc1))
elif opcao==4:
    parcela=int(input('Quantidade de parcelas:'))
    juros1= juros/parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela,juros1))
    print('Sua compra de R${} terá o valor final de R${:.2f}'.format(preco,juros))
else:
    print('ERRO! escolha uma opção entre 1 e 4')
