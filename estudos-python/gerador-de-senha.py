import string
import random
print('Password: ', ''.join(random.choice(string.ascii_letters + string.digits) for _ in range (8)))

#EXPLICAÇÃO:
#"string.ascii_letters + string.digits" entrega todas as letras e números, ele basicamente diz:
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
#---------------------------------------------------------------------------------------------
#"random.choice" diz: "vou pegar algum caractere aleatório disso tudo"
#"for _ in range (8)" isso limita o número de caracteres até '8'
#---------------------------------------------------------------------------------------------
# " ''.join " e´a cola, sem ela vocÊ teria uma lista feia, com ela você tem uma senha arrumada
