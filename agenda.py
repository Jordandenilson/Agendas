##################################################
############## F U N C I O N E S #################

def Opcion() :
	n = int(input("Su opción es: "))
	print("\n")
	return n
	
def Opciones() :
	print("\n1. Añardir contacto.")
	print("2. Mostrar contacto")
	print("3. Eliminar contacto")
	print("4. Salir\n")

def Añadir() :
	x = str(input("Ingrese el número: "))
	return x
	
def Verificar_validacion(x) :
	if len(x)==9 and x[0]=='9':
		return True
	else :
		return False
		
#def Verificar_repiticion(x) :
	


##################################################
##################################################

Contactos = {"Presi":"986541237", "Pepito":"986751324", "Emma":"978563421"}

print("Bienvenido a su agenda personal")
print("Cómo me dirijo a usted?")

N = input("Digite su nombre... ")

print(f"\nMuy bien {N} qué función quieres realizar?: ")

Opciones()

#n = int(input("Su opción es: "))
n = Opcion()

while 0>=n or n>=5 :
	print("La opción escogida no existe")
	n = Opcion()
while 3>=n and n>=1 :
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::	
	if n == 1 :
		x = Añadir()
		v = Verificar_validacion(x)
		while v == False :
			print("El número ingresado es incorrecto")
			x = Añadir()
			v = Verificar_validacion(x)
		if v == True :
			print("El número es correcto")
			l = str(input("Cómo quiere guardar el número? "))
			Contactos[l] = x 
			print("Contacto agregado!")
		Opciones()
		n = Opcion()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	if n == 2 :
		print(Contactos)
		Opciones()
		n = Opcion()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	if n == 3 :
		print(Contactos)
		d = str(input("Qué contaco desea eliminar?"))
		del Contactos[d]
		print("Contacto eliminado")
		Opciones()
		n = Opcion()
	
if n == 4 :
	print("Gracias por usar BESTO_AGENDA, que tenga buen día n.n")
