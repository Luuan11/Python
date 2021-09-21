import random 

letra = 'abcdefghijklmnopqrstuvwxyz'
LETRA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
números = '0123456789'
simbolos = '[]{}()*#;/,-_%'
quantidade = input('Digite qual tamanho da senha: ')
qI = int(quantidade)
l = qI
a = letra + LETRA + números + simbolos
passwordAll = "".join(random.sample(a,l))
print ('passwordAll = ' + passwordAll) 