import math
number1 = int(input("escreva o coeficiente de a "));
number2 = int(input("escreva o coeficiente de b "));
number3 = int(input("escreva o coeficiente de c "));

raiz_negativa = math.sqrt(number2**-(4*number1*number2));
raiz  = math.sqrt(number2**-(4*number1*number2));

print("Minha raiz é:", raiz,raiz_negativa);