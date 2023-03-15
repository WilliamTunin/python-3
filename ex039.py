print("Comparados de números \n")
n1 = int(input("Digite um número inteiro: \n"))
n2 = int(input("Digite outro número inteiro: \n"))

if n1 > n2:
    print("O primeiro valor é maior, pois {} > {}.".format(n1, n2))
elif n2 > n1:
    print("O segundo valor é maior, pois {} > {}.".format(n2, n1))
else:
    print("Não existe valor maior; os números digitados são iguais.")
