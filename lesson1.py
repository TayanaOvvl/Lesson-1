a = '54321'
b = '123'
print(a)
print(b)

a1 = list(a)
b1 = list(b)

contained = False  

for i in range (len(a)-len(b)+1):
    if b1[0] == a1[i]: 
        contained = True   
        for j in range (1, len(b)):
            if b1[j] != a1[i + j]: 
                contained = False
                break
    if contained:
        break
            
if contained == False:
    print ("Не содержится.")
else: 
    print("Содержится.")
