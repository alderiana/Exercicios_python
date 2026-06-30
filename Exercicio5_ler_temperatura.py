#Temperetura em gaus celsius

temperatura = float(input("Digite uma temperatura em (Cº): "))

if temperatura < 0:
   print ("Frio extremo")
elif 0 <= temperatura <= 10:
    print ("Frio")
elif 11 <= temperatura <= 25:
    print("Ameno")
elif 26 <= temperatura <=35:
    print ("Quente")
else:
    print("Muito quente")
