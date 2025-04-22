peso = float(input("informe seu peso: "))
altura = float(input("informe sua altura: "))
imc = peso/altura**2
print(f"{imc:.2f}")
if imc <18.6:
    print("tas seco dimai") # abaixo do peso
elif imc >18.6 and imc <24.9:
    print("ta peso parabens ta show") # peso ideal
elif imc >25 and imc <29.9:
    print("alguem tem que ver isso ai") # levemente acima do peso
elif imc >30 and imc <34.9:
    print("rapaz ta gordinho viu bora ver vius") # obesidade grau 1
elif imc >35 and imc <39.9:
    print("se vc eh fã do gordão da xre parabéns ja ja ta igual ele") #obesidade grau 2(severa)
else:
    print("gordão da xre") # obesidade grau 3(morbida)