# ACTIVIDAD INDIVIDUAL 2

'''

Familiarizado ya con estos componentes debemos prepararnos en realizar las siguientes acciones, para
simular la compra a través de una página web

● En base al contexto: Piensa en una aplicación web que busque solucionar una problemática.
● Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
● Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
● Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
● Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.
● ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente
su nombre? ¿Cómo solucionarías este problema?
● Convierte tu string en una lista, en la cual cada elemento es un usuario.
● Imprima en pantalla la cantidad usuarios que tiene tu aplicación.
● Imprima en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar
para realizar esto?


'''

# Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
from pickle import FALSE, TRUE


user = 'user1 user2 user3 user4 user5 user6 user7'

# Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.
searchedUser = input("Insert username: ")

if searchedUser in user:
    print(f'Hello {searchedUser}')
else:
    print('User Not Found')
    
# ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente su nombre? ¿Cómo solucionarías este problema?
'''
Que ingrese uno de los caracteres en mayuscula o minuscula y en la base de datos se encuentre en un formato distinto al buscado
Se puede solucionar implementando un metodo para que el dato buscado quede completamente en mayuscula, minuscula o capitalizado, dependiendo de lo que se requiera
'''

# Convierte tu string en una lista, en la cual cada elemento es un usuario.
userList = user.split(" ")
print(f'La cantidad de usuarios es de: {len(userList)}')

# Imprima en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar para realizar esto?

for usu in userList:
    print(f'Saludos {usu}!')

