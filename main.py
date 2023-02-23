expression = "2+5-7/2*6/2"


components = expression.split("+")

result = 0
i = 0

for component in components:
    if "*" in component:
        flag = 0
        currentflag = 0
        if "-" in component:
            flag = 1
            
            templist = component.split("-")
            if "*" in templist[0]:
                factors = templist[0]
                currentflag=1
            else:
                
                currentflag = 0
                factors = templist[1]
        
        value1 =0
        value2 =0
        factors = factors.split("*")
        if "/" in factors[0]:
            numerator, denominator = factors[0].split("/")
            value1 = float(numerator) / float(denominator)
        if "/" in factors[1]:
            numerator, denominator = factors[1].split("/")
            print(factors[1])
            value2 = float(numerator) / float(denominator)
        if(value1 == 0):
            value1=factors[0]
        if(value2 == 0):
            value2= factors[1]
       
        value = float(value1) * float(value2)
        print(value)
        if(currentflag == 1 and flag == 1):
            components[i] = str(value)+"-" + str(templist[currentflag]) 
        elif currentflag == 0 and flag == 1:
            components[i] = str(templist[currentflag])+ "-"  +str(value)
    i+=1
ans = 0
print(components)
for component in components:
    if "-" in component:
        factors = component.split("-")
        ans += float(factors[0]) - float(factors[1])
    else:
        ans += float(component)
        


print(ans)  
