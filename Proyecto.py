#-----MENÚ PRINCIPAL-----#

def menuPrincipal():
    print("BIENVENIDO AL MENÚ PRINCPAL")
    print("1- Si desea acceder al menú de opciones administrativas.")
    print("2- Si desea acceder al menu de usuario normal.")
    print("3- Si desea salir.")

    opcion=input("¿Que opcion desea elegir?"+"\n")
    if(opcion == "1"):
        return menuAdministrativo()
    elif(opcion == "2"):
        return usuarioNormal()
    else:
        if(opcion == "3"):
            print("¡Hasta Luego!")
            input()

def menuAdministrativo():
    print("MENÚ ADMINISTRATIVO")
    print("1- Gestión de empresas.")
    print("2- Gestión de transporte por empresa.")
    print("3- Gestión de viaje.")
    print("4- Consultar historial de reservaciones")
    print("5- Volver al menú principal")

    opcionAdmin = input("¿Que opcion desea elegir?"+"\n")
    
    if opcionAdmin == "1":
        return gestionEmpresas()
    
    elif opcionAdmin == "2":
        return gestionTransporte()
    
    elif opcionAdmin == "3":
        return gestionViajes()
    
    elif opcionAdmin == "4":
        return historial()
    
    elif opcionAdmin == "5":
        return menuPrincipal()
    
    else:
        print ("opcion incorrecta")
        return menuAdministrativo()
        

########################################################################################       
        
def gestionEmpresas():
    print("1- Agregar una empresa")
    print("2- Eliminar una empresa")
    print("3- Modificar una empresa")
    print("4- Ver todas las empresas")
    print("5- Volver al menú administrativo")

    opcionGes = input("¿Que desea hacer?"+"\n")

    if opcionGes == "1":
        return agregarEmpresa()
    elif opcionGes == "2":
        return eliminarEmpresa()
    elif opcionGes == "3":
        return modificarEmpresa()
    elif opcionGes == "4":
        return verEmpresas
    else:
        print ("opcion incorrecta")
        return menuAdministrativo()
        

#--------------------------------------------------------------------------------------#
def agregarEmpresa():
    empresas = open("Empresas.txt","a")
    Cedula = input("Digite la cédula jurídica:"+"\n")
    if len(Cedula)== 10:
        return EmpresaName(Cedula)
    else:
        return ("La cédula debe contener al menos 10 dígitos")

def EmpresaName(Cedula):
    empresas = open("Empresas.txt","a")
    Nombre = input("Escriba el nombre de la empresa:"+"\n")
    return ubicacionEmpresa(Cedula,Nombre)

def ubicacionEmpresa(Cedula,Nombre):
    empresas = open("Empresas.txt","a")
    empresas.write(Cedula+"a")
    empresas.write(Nombre+"\n")
    Ubicacion = input("Escriba la ubicación de la empresa"+"\n")
    empresas.write(Ubicacion+"\n")
    print ("Empresa registrada exitosamente")
    return gestionEmpresas()
    

#--------------------------------------------------------------------------------------#

def eliminarEmpresa():
    nombre = input("Escriba el nombre de la empresa que desea borrar"+"\n")
    registro = open("Empresas.txt")
    delete = registro.readlines()
    if (nombre + "\n")in delete:
        ContarLineas = delete.index(nombre + "\n")
        BorrarLineas = deleteEmpresa(delete,ContarLineas,0)
        registro.close
        abrir = open("Empresas.txt","w")
        abrir.write(BorrarLineas)
        abrir.close()
        print ("Empresa eliminada!")
        print("\n")
        gestionEmpresas()

    else:
        print ("No existe ninguna empresa con ese nombre"+"\n")
        gestionEmpresas()

def deleteEmpresa(delete,ContarLineas,contador):
    if contador == 3:
        return transformarSTR(delete)
    else:
        print(delete[ContarLineas].rstrip())
        delete.pop(ContarLineas)
        return deleteEmpresa(delete,ContarLineas,contador+1)


#--------------------------------------------------------------------------------------#
def TransformarSTR(delete):
    if isinstance(delete,list):
        STR = ""
        for linea in delete:
            STR += linea
        return STR
    else:
        print("")



def TransformarSTR_aux(delete):
    if isinstance(empresa,list):
        STR = ""
        for linea in contacto:
            STR += linea
        return STR
    else:
        print("")



#-------------------------------------------------------------------------------------#

