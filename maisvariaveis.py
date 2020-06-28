#Caracteristicas do objeto
#a = input("Digite algo:")
#print("O tipo primitivo desse valor é {}".format(type(a)))
#print("Só tem espaço?", a.isspace())
#print("É um número?", a.isnumeric())
#print("É alfabético?", a.isalpha())
#print("É alfanumérico?", a.isalnum())
#print("Está em maíúsculas?", a.isupper())
#print("Está em minúscula?", a.islower())
#print("Está capitalizada?", a.istitle()) #letra maiusculas e minusculas

#mesmo jeito de fazer só que com .format
a = input("Digite algo")
print("O tipo primitivo desse valor é {}".format(type(a)))
print("Só tem espaços?{}".format(a.isspace()))
print("É um número?{}".format(a.isnumeric()))
print("É alfabético?{}".format(a.isnumeric()))
print("É alfanumérico?{}".format(a.isalpha()))
print("É alfanumérico?{}".format(a.isalnum()))
print("Está em maiúscula?{}".format(a.isupper()))
print("Está em minúscula?{}".format(a.islower()))
print("Está capitalizado?{}".format(a.istitle()))
