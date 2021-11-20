L = [1, 6, 8, 11, 9, 23, 5, 2]   
H = []
maior = -99999

for e in range(len(L)):
    if (L[e] > maior): 
        maior = L[e]
        H.append(maior)
        
print(H)        
print(H[-1])