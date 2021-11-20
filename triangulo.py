'''
pedir pro usuário digitar os valores dos lados do triângulo (3x)
verifica a condição de exitência de um triângulo
verifica se 3 lados são iguais 
    informa que é equilátero
senao, verifica se 2 lados são iguais
    informa que é isósceles
senao 
    é escaleno
'''

print("Digite 3 valores para o seu triângulo: ")

A = int(input("Digite o valor do PRIMEIRO lado: "))
B = int(input("Digite o valor do SEGUNDO lado: "))
C = int(input("Digite o valor do TERCEIRO lado: "))

#Verifica a condição de existência de um triângulo
if (((A + B) < C) or ((A + C) < B) or ((C + B) < A)):
    print("Os 3 lados não compoem um triângulo!!")
else:
    if (A == B and A == C):
        print("Triângulo Equilátero")
    
    if (A != B and A != C and B != C):
        print("Triângulo Escaleno")
        
    if ((A == B and A != C) or (B == C and B != A) or (A == C and A != B)):
        print("Triângulo Isósceles")
    
    #elif (A != B and A != C and B != C):
        #print("Triângulo Escaleno")
        
    #else:
        #print("Triângulo Isósceles")
        