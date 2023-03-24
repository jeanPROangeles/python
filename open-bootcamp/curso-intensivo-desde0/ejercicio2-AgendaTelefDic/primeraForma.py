contactos = {}
while True:
  print()
  print("Seleccione una opcion:")
  print("1. Registrar contacto")
  print("2. Buscar teléfono")
  print("3. salir")

  opcion = input("Introduce el numero de la opción deseada: ")
  if opcion == "1":
    nombre = input("ingrese el nombre del contacto: ")
    telefono = input("ingrese el telefono del contacto: ")     
    contactos[nombre] = telefono
    print(f"{nombre} a sido añadido a la agenda")
  elif opcion == "2":
    nombre2 = input("ingrese el nombre del contacto: ")
    print(f'el numero de {nombre2} es {contactos[nombre2]}')
  elif opcion == "3":
    print("¡hasta pronto!")  
    break
  else:
    print("Opción no valida. Introduce una opcion del 1 al 3")       
