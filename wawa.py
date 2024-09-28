#print negative, print positive 
age = [-12,13,-14,15,-15]

#for loop
for dataage in age:
    if dataage > 0:
     print(str(dataage) + "positive")
    elif dataage < 0:
     print(str(dataage) + "negative")
     break
#if james exist in the array print jame cure or james none  
username = ["juan", "pedero", "james", "sagad", "feugo"]

#for loop
for datausername in username:
    if "james" == username:
        print("james cute")
    else:
        print("none")
    break