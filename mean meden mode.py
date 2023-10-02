set1 = open("mean-median-mode-frequency.csv",'r')
total = 0
for lin in set1:
    lin= lin.strip()
    lin= lin.split(",")
    print(lin)
set1.close()
for x in lin:
        total = total + lin[x - 1]
print(total)



'''
lin= lin.strip()

lin= lin.split(",")

for x in lin:
        total = total + lin[x - 1]
print(total)
'''