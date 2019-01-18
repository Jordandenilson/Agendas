print("Bienvenido a su agenda personal")
print("Cómo me dirijo a usted?")

N = input("Digite su nombre...")

print(f"\nMuy bien {N} qué función quieres realizar?:")

print("\n1. Añardir contacto.")
print("2. Mostrar contacto")
print("3. Eliminar contacto")
print("4. Salir\n")

n = int(input("Su opción es: "))

while 0>=n or n>=5 :
	print("La opción escogida no existe")
	n = int(input("Su opción es: "))
