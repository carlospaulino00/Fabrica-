def mult(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print(mult(n1, n2))
