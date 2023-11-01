#Se inporta la librerias
import datetime

#Se define una variable donde se guarda el valor de la fecha actual
fecha_actual = datetime.date.today()

print("================================================")
print("Bienvenido al programa para calcular la edad")
print("================================================")

#Se crean un bucle
while True:
    # En este bloque se define el:
    # 1) input que va a ingresar la persona
    # 2) Que la variable "año, mes, dia" tome el valor de fecha_nacimiento la mapee y que la separe con "/"
    # 3) Ahora esta variable "fecha_nacimiento" toma el valor de "año, mes, dia" crea un objeto donde se va a llamar mas adelante
    # y si se asignan los valores bien se rompe el ciclo para que siga con la siguiente intruccion y si no se cumple se sigue ejecutanto el bucle pero ahora con el mensaje de error de "Por favor, ingresa una fecha válida en el formato YYYY/MM/DD."
    try:
        fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY/MM/DD): ") #1
        año, mes, dia = map(int, fecha_nacimiento.split('/')) #2
        fecha_nacimiento = datetime.date(año, mes, dia) #3
        break 
    except ValueError:
        print("Por favor, ingresa una fecha válida en el formato YYYY/MM/DD.")


#Aqui la variable "diferencia" toma los valores de "fechaActual" y fechaNaciemiento para calcular los años que tiene el usuario 
# La variable "edad", se toma el componente de días de la diferencia calculada (accesible mediante diferencia.days) y se divide entre 365. pero en algunos casos no es muy presisa porque no tiene la capacidad de tomar los años biciestos pero en la mayoria de casos es presisa
diferencia = fecha_actual - fecha_nacimiento
edad = diferencia.days // 365  

#Y por ultimo se imprime el mensaje con los años que tiene el usuario
print("================================================")
print(f"Tienes aproximadamente {edad} años de edad.")
