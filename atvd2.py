opcao = ""
print("Escolha uma opção: ")
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando... \n algo mais?")
    elif opcao == 2:
        print("Exibindo o extrato \n algo mais?")

else: print("Obrigado, até a proxima.")