print("Comparados de números \n")
num1 = int(input("Digite um número inteiro: \n"))
num2 = int(input("Digite outro número inteiro: \n"))

if num1 > num2:
    print("O primeiro valor é maior, pois {} > {}.".format(num1, num2))
elif num2 > num1:
    print("O segundo valor é maior, pois {} > {}.".format(num2, num1))
else:
    print("Não existe valor maior; os números digitados são iguais.")