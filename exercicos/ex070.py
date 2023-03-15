from time import sleep
totalPreco = barato = maisDe100 = 0
print('-='* 20)
print(f"{'SUPERMERCADO DO ZÉ':^40}")
print('-=' * 20)
print("Informe suas compras!!!")
while True:
    print('--' * 20)
    produtos = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    print('--' * 20)
    continuar = ' '
    produtoBarato = ' '
    while continuar not in "SN":
        continuar = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if preco > 0:
        totalPreco += preco
        barato = preco
        produtoBarato = produtos
    if preco < barato:
        barato = preco
        produtoBarato = produtos
    if preco > 100:
        maisDe100 += 1
    if continuar == "N":
        break
sleep(0.5)
print(f"O total gasto nas compras foi de {totalPreco:.2f}R$.")
sleep(0.5)
print(f"Custaram mais de 100R$ {maisDe100} produtos.")
sleep(0.5)
print(f"O produto mais bararo foi {produtoBarato} que custou {barato}R$.")
sleep(0.25)
print("Obrigado pela preferencia.\nVolte sempre.")

