#-----                       MENÚ PRINCIPAL                       -----#

#Nombre: menuPrincipal
#Entradas: No tiene
#Salidas: Retornar menu Principal
#Restricciones: No tiene


def menuPrincipal():
    print("\n"+"BIENVENIDO AL MENÚ PRINCPAL"+"\n")
    print("1- Si desea acceder al menú de opciones administrativas.")
    print("2- Si desea acceder al menu de usuario normal.")
    print("3- Si desea salir."+"\n")

    opcion=input("¿Que opcion desea elegir?"+"\n")
    if(opcion == "1"):
        abrir=open("claves.txt")
        verificar=abrir.readlines()
        claves=input("Escriba la contraseña:"+"\n")
        if (claves in verificar):
            return menuAdministrativo()
        else:
            print('Contraseña incorrecta'+"\n")
            return menuPrincipal()
    elif(opcion == "2"):
        return usuarioNormal()
    else:
        if(opcion == "3"):
            print("¡Hasta Luego!"+"\n")
            input()

#Nombre: menuAdministrativo
#Entradas: No tiene
#Salidas: Retornar menu administrativo
#Restricciones: No tiene

def menuAdministrativo():
    print("\n"+"MENÚ ADMINISTRATIVO"+"\n")
    print("1- Gestión de empresas.")
    print("2- Gestión de transporte por empresa.")
    print("3- Gestión de viaje.")
    print("4- Consultar historial de reservaciones")
    print("5- Volver al menú principal")

    opcionAdmin = input("\n"+"¿Que opcion desea elegir?"+"\n")
    
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
        print ("\n"+"opcion incorrecta"+"\n")
        return menuAdministrativo()
        



########################################################################################
########################################################################################       

#Nombre: gestionEmpresas
#Entradas: No tiene
#Salidas: Retornar un menú de opciones a elegir
#Restricciones: No tiene
       
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
        return verEmpresas()
    else:
        print ("\n"+"opcion incorrecta"+"\n")
        return menuAdministrativo()
        
#Nombre: agregarEmpresa
#Entradas: No tiene
#Salidas: guardar la cédula en una variable
#Restricciones: No tiene

def agregarEmpresa():
    Cedula = input("\n"+"Digite la cédula jurídica:"+"\n")
    if len(Cedula) == 10:
        archivo= open("Empresas.txt")
        archivo2=archivo.readlines()
        if ((Cedula + "\n") in archivo2):
            return ("\n"+"Error: Ya hay una empresa con esa cedula"+"\n")
        else:
            return EmpresaName(Cedula)        
    else:
        print("\n"+"La cédula debe contener 10 digitos"+"\n")

#Nombre: EmpresaName
#Entradas: un parámetro llamado cédula
#Salidas: guardar la Nombre en una variable
#Restricciones: No tiene

def EmpresaName(Cedula):
    Nombre = input("Escriba el nombre de la empresa:"+"\n")
    return ubicacionEmpresa(Cedula,Nombre)

#Nombre: ubicacionEmpresa
#Entradas: dos parámetros llamados: Cedula, Nombre
#Salidas: guardar la Ubicación en una variable
#Restricciones: No tiene

def ubicacionEmpresa(Cedula,Nombre):
    Ubicacion = input("Escriba la ubicación de la empresa"+"\n")
    guardarEmpresa(Cedula, Nombre, Ubicacion)
    return gestionEmpresas()

#Nombre: guardarEmpresa
#Entradas: tres parámetros llamados: Cedula, Nombre, Ubicacion
#Salidas: guardar las variables en archivo.txt
#Restricciones: No tiene

def guardarEmpresa(Cedula, Nombre, Ubicacion):
    empresas = open("Empresas.txt","a")
    empresas.write(Cedula+"\n")
    empresas.write(Nombre+"\n")
    empresas.write(Ubicacion+"\n")
    empresas.write("---------------------------------------------")
    empresas.close()
    print ("Empresa registrada exitosamente"+"\n")


#Nombre: eliminarEmpresa
#Entradas: No tiene
#Salidas: eliminar la empresa del archivo
#Restricciones: No tiene

def eliminarEmpresa():
    empresas = input("Escriba la cédula de la empresa que desea borrar"+"\n")
    registro = open("Empresas.txt")
    delete = registro.readlines()
    abrirTrans= open("Transportes.txt")
    abrir=abrirTrans.readlines()
    if (empresas+"\n")in delete:
        if (empresas+"\n") in abrir:
            print("Esa empresa no se puede eliminar debido a que esta aasociado a un transporte"+"\n")
            return eliminarEmpresa()
        else:
            ContarLineas = delete.index(empresas+"\n")
            BorrarLineas = deleteEmpresa(delete,ContarLineas,0)
            registro.close
            abrir = open("Empresas.txt","w")
            abrir.write(BorrarLineas)
            abrir.close()
            print ("Empresa eliminada!"+"\n")
            print("\n")
            gestionEmpresas()

    else:
        print ("No existe ninguna empresa con ese nombre"+"\n")
        gestionEmpresas()

#Nombre: deleteEmpresa
#Entradas: tres variables llamadas: delete,ContarLineas,contador
#Salidas: contar lineas 
#Restricciones: No tiene

def deleteEmpresa(delete,ContarLineas,contador):
    if contador == 4:
        return TransformarSTR(delete)
    else:
        print(delete[ContarLineas].rstrip())
        delete.pop(ContarLineas)
        return deleteEmpresa(delete,ContarLineas,contador+1)

#Nombre: TransformarSTR
#Entradas: un parámetro llamado delete
#Salidas: transformar el parámetro a una lista
#Restricciones: el parámetro debe ser una lista
    
def TransformarSTR(delete):
    if isinstance(delete,list):
        STR = ""
        for indice in delete:
            STR += indice
        return STR
    else:
        print("")

#Nombre: TransformarSTR_aux
#Entradas: Un parámetro llamado delete
#Salidas: retornar STR
#Restricciones: delete debe ser una lista

def TransformarSTR_aux(delete):
    if isinstance(delete,list):
        STR = ""
        for indice in delete:
            STR += indice
        return STR
    else:
        print("")

#Nombre: modificarEmpresa
#Entradas: No tiene
#Salidas: modificar la empresa
#Restricciones: No tiene

def modificarEmpresa():
    Cedula = input("Digite el numero de cédula de la empresa a modificar:")
    Abrir = open("Empresas.txt")
    empresas = Abrir.readlines()
    Abrir.close()
    
    if (Cedula + "\n") in empresas:
        Indice = empresas.index(Cedula+ "\n")
        modificarEmp_aux(empresas,Indice,0)
        empresaNuevo = modificarEmp3_aux(empresas,Indice+1,0)
        Abrir = open("Empresas.txt","w")
        Abrir.write(TransformarSTR_aux(empresaNuevo))
        Abrir.close()
        return gestionEmpresas()
    else:
        print ("Empresa no registrada")
    
#Nombre: modificarEmp_aux
#Entradas: 3 parámetros llamados: lista, indice,contador
#Salidas: guardar la cédula en una variable
#Restricciones: No tiene

def modificarEmp_aux(lista,Indice,contador):
    if contador > 2:
        print ("------------------------------------")
         
    else:
        if contador == 0:
            print(lista[Indice].rstrip())
            return modificarEmp_aux(lista,Indice+1,contador+1)
        
        elif contador == 1:
            print(lista[Indice].rstrip())
            return modificarEmp_aux(lista,Indice+1,contador+1)

        else:
            print(lista[Indice].rstrip())
            return modificarEmp_aux(lista,Indice+1,contador+1)



def modificarEmp3_aux(Dato,Indice,contador):
    if contador == 2:
        return Dato
    elif contador == 0:
        Dato2 = input("Escriba el nombre de la empresa:"+"\n")
        Dato[Indice]=Dato2 + "\n"
        return modificarEmp3_aux(Dato,Indice+1,contador+1)
    else:
        Dato2 = input("Escriba la ubicación de la empresa:"+"\n")
        Dato[Indice]=Dato2 + "\n"
        return modificarEmp3_aux(Dato,Indice+1,contador+1)

def verEmpresas():
    Abrir = open("Empresas.txt","r")
    OPEN = Abrir.read()
    Abrir.close()
    print ("\n")
    print(OPEN)
    gestionTransporte()

#########################################################################################
#--------------------------GESTION DE TRANSPORTE POR EMPRESA----------------------------#
#########################################################################################

def gestionTransporte():
    print("1- Agregar un Transporte")
    print("2- Eliminar un Transporte")
    print("3- Modificar un Transporte")
    print("4- Ver todos los transportes")
    print("5- Volver a gestión de transporte")

    opcionGes = input("¿Que desea hacer?"+"\n")

    if opcionGes == "1":
        return agregarTransporte()
    elif opcionGes == "2":
        return eliminarTransporte()
    elif opcionGes == "3":
        return modificarTransporte()
    elif opcionGes == "4":
        return verTransportes()
    else:
        print ("opcion incorrecta")
        return menuAdministrativo()


def agregarTransporte():
    Placa = input("Digite la placa del transporte:"+"\n")
    archivo = open("Transportes.txt")
    archivo2 = archivo.readlines()
    if ((Placa + "\n") in archivo2):
        return ("\n"+"Error: Ya hay un transporte con esa placa"+"\n")
    else:
        return EmpresaName(Placa)        

def marca(Placa):
    Marca = input("Ingrese la marca del transporte:"+"\n")
    return modelo(Placa,Marca)

def modelo(Placa,Marca):
    Modelo = input("¿Cual es el modelo del transporte?"+"\n")
    return año(Placa,Marca,Modelo)

def año(Placa, Marca, Modelo):
    Año = input("¿Cual es el año del transporte?"+"\n")
    return empresa(Placa,Marca,Modelo,Año)

def empresa(Placa,Marca,Modelo,Año):
    Empresa = input("¿A cual empresa quieres agregar el transporte?"+"\n")
    return guardar_transporte(Placa,Marca,Modelo,Año,Empresa)

def guardar_transporte(Placa,Marca,Modelo,Año,Empresa):
    Transporte = open("Transportes.txt","a")
    Transporte.write(Placa+"\n")
    Transporte.write(Marca+"\n")
    Transporte.write(Modelo+"\n")
    Transporte.write(Año+"\n")
    Transporte.write(Empresa+"\n")
    Transporte.write("---------------------------------------------")
    print ("Transporte registrado exitosamente")
    Transporte.close()
    return gestionTransporte()


def eliminarTransporte():
    transportes = input("Escriba la placa del transporte que desea borrar"+"\n")
    registro = open("Transportes.txt")
    delete = registro.readlines()
    if (transportes+"\n")in delete:
        ContarLineas = delete.index(transportes+"\n")
        BorrarLineas = deleteTransporte(delete,ContarLineas,0)
        registro.close
        abrir = open("Transportes.txt","w")
        abrir.write(BorrarLineas)
        abrir.close()
        print ("Trasnporte eliminado!")
        print("\n")
        gestionTransporte()

    else:
        print ("No existe ningún Transporte con esa Placa"+"\n")
        gestionTransporte()

def deleteTransporte(delete,ContarLineas,contador):
    if contador == 6:
        return TransformarSTR(delete)
    else:
        print(delete[ContarLineas].rstrip())
        delete.pop(ContarLineas)
        return deleteTransporte(delete,ContarLineas,contador+1)


def modificarTransporte():
    Placa = input("Digite el numero de placa:")
    Abrir = open("Transportes.txt")
    transportes = Abrir.readlines()
    Abrir.close()
    if (Placa + "\n") in transportes:
        Indice = transportes.index(Placa+ "\n")
        transporte2_aux(transportes,Indice,0)
        transporteNuevo = transporte3_aux(transportes,Indice+1,0)
        Abrir = open("Transportes.txt","w")
        Abrir.write(TransformarString_aux(transporteNuevo))
        Abrir.close()

        print("\n")
        return gestionTransporte()

"""
NOMBRE: Contacto2_aux
ENTRADAS: Recibe como entradas 3 parametros que son. lista, indice, contador
SALIDAS: La informacion que esta en la linea

"""
def transporte2_aux(lista,Indice,contador):
    if contador == 6:
        print("") 
    else:
        print(lista[Indice].rstrip())
        return transporte2_aux(lista,Indice+1,contador+1)

"""
NOMBRE: Contacto3_aux
ENTRADAS: Recibe como entrada 3 parámetros llamados Dato,Indice,contador
SALIDAS: Imprimir l
RESTRICCIONES: El correo tiene que llevar siempre el @
"""

def transporte3_aux(Dato,Indice,contador):
    if contador > 4:
        return Dato
    elif contador == 1:
        Dato2 = input("Escriba la nueva marca del transporte:"+"\n")
        Dato[Indice]=Dato2 
        return transporte3_aux(Dato,Indice+1,contador+1)
    else:
        if contador == 2:
            Dato2 = input("Escriba el nuevo modelo del transporte:"+"\n")
            Dato[Indice]=Dato2 
            return transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 3:
            Dato2 = input("Escriba el nuevo año del transporte:"+"\n")
            Dato[Indice]=Dato2 
            return transporte3_aux(Dato,Indice+1,contador+1)
        else:
            Dato2 = input("Escriba la nueva empresa del transporte:"+"\n")
            Dato[Indice]=Dato2 
            return transporte3_aux(Dato,Indice+1,contador+1)
        

def verTransportes():
    Abrir = open("Transportes.txt","r")
    OPEN = Abrir.read()
    Abrir.close()
    print ("\n")
    print(OPEN)
    gestionTransporte()
    

#########################################################################################
#------------------------------GESTIÓN DE VIAJE-----------------------------------------#

def gestionViajes():
    print("1- Incluir un viaje")
    print("2- Eliminar un viaje")
    print("3- Modificar un viaje")
    print("4- Ver todos los viajes")
    print("5- Volver a gestión de viajes")

    opcionGes = input("¿Que desea hacer?"+"\n")

    if opcionGes == "1":
        return agregarViaje()
    elif opcionGes == "2":
        return eliminarViaje()
    elif opcionGes == "3":
        return modificarViaje()
    elif opcionGes == "4":
        return verViajes()
    else:
        print ("opcion incorrecta"+"\n")
        return menuAdministrativo()


def agregarViaje():
    Numero = input("Digite la placa del transporte:"+"\n")
    return salidaCity(Numero)

def salidaCity(Numero):
    Salida = input("Cual es la Ciudad de salida:"+"\n")
    return fecha_hora_salida(Numero,Salida)

def fecha_hora_salida(Numero,Salida):
    FechaS = input("¿Cual es la fecha de salida?"+"\n")
    HoraS = input("¿Cual es la hora de salida?"+"\n")
    return llegadaCity(Numero,Salida,FechaS,HoraS)

def llegadaCity(Numero,Salida,Fecha,Hora):
    Llegada = input("¿Cual es la ciudad de llegada?"+"\n")
    return fecha_hora_llegada(Numero,Salida,FechaS,Hora,Llegada)

def fecha_hora_llegada(Numero,Salida,FechaS,Hora,Llegada):
    FechaL = input("¿Cual es la fecha de llegada?"+"\n")
    HoraL = input("¿Cual es la hora de llegada?"+"\n")
    return asociar_empresa(Numero,Salida,FechaS,Hora,Llegada,FechaL,HoraL)

def asociar_empresa(Numero,Salida,FechaS,Hora,Llegada,FechaL,HoraL):
    empresa = input("¿A que empresa quieres asociar el viaje"+"\n")
    return asociar_trans(Numero,Salida,FechaS,Hora,Llegada,FechaL,HoraL,empresa)

def asociar_trans(Numero,Salida,FechaS,Hora,Llegada,FechaL,HoraL,empresa):
    transporte = input("¿Que transporte desea usar?"+"\n")
    return guardar_viajes(Numero,Salida,FechaS,HoraS,Llegada,FechaL,HoraL,empresa,transporte)

def guardar_viajes(Numero,Salida,FechaS,HoraS,Llegada,FechaL,HoraL,empresa,transporte):
    viajes = open("Viajes.txt","a")
    viajes.write(Numero)
    viajes.write(Salida)
    viajes.write(FechaS)
    viajes.write(HoraS)
    viajes.write(Llegada)
    viajes.write(FechaL)
    viajes.write(HoraL)
    viajes.write(empresa)
    viajes.write(transporte)
    viajes.write("------------------------------------------------------------------")
    viajes.close()
    print ("Viaje registrado exitosamente"+"\n")
    return gestionTransporte()


def eliminar_viaje():
    viajes = input("Escriba el numero de viaje"+"\n")
    registro = open("Viajes.txt")
    delete = registro.readlines()
    if (viajes+"\n")in delete:
        ContarLineas = delete.index(viajes+"\n")
        BorrarLineas = deleteViaje(delete,ContarLineas,0)
        registro.close
        abrir = open("Viajes.txt","w")
        abrir.write(BorrarLineas)
        abrir.close()
        print ("Viaje eliminado exitósamente!"+"\n")
        gestionViajes()

    else:
        print ("No existe ningún Viaje con esa numero"+"\n")
        gestionViajes()

def deleteViaje(delete,ContarLineas,contador):
    if contador == 10:
        return TransformarSTR(delete)
    else:
        print(delete[ContarLineas].rstrip())
        delete.pop(ContarLineas)
        return deleteViaje(delete,ContarLineas,contador+1)



def modificarViaje():
    Numero = input("Digite el numero de viaje:")
    Abrir = open("Viajes.txt")
    viajes = Abrir.readlines()
    Abrir.close()
    if (Numero + "\n") in viajes:
        Indice = viajes.index(Placa+ "\n")
        viajes2_aux(viajes,Indice,0)
        viajesNuevo = viajes3_aux(viajes,Indice+1,0)
        Abrir = open("Viajes.txt","w")
        Abrir.write(TransformarString_aux(viajesNuevo))
        Abrir.close()

        print("\n")
        return gestionViajes()

"""
NOMBRE: Contacto2_aux
ENTRADAS: Recibe como entradas 3 parametros que son. lista, indice, contador
SALIDAS: La informacion que esta en la linea

"""
def viajes2_aux(lista,Indice,contador):
    if contador == 8:
        print("") 
    else:
        print(lista[Indice].rstrip())
        return viajes2_aux(lista,Indice+1,contador+1)

"""
NOMBRE: Contacto3_aux
ENTRADAS: Recibe como entrada 3 parámetros llamados Dato,Indice,contador
SALIDAS: Imprimir l
RESTRICCIONES: El correo tiene que llevar siempre el @
"""

def viajes3_aux(Dato,Indice,contador):
    if contador > 8:
        return Dato
    elif contador == 1:
        Dato2 = input("Escriba la nueva Ciudad de salida:"+"\n")
        Dato[Indice]=Dato2 
        return viajes3_aux(Dato,Indice+1,contador+1)
    else:
        if contador == 2:
            Dato2 = input("Escriba la nueva fecha de salida:"+"\n")
            Dato[Indice]=Dato2 
            return viajes3_aux(Dato,Indice+1,contador+1)
        elif contador == 3:
            Dato2 = input("Escriba la nueva hora de llegada:"+"\n")
            Dato[Indice]=Dato2 
            return viajes3_aux(Dato,Indice+1,contador+1)
        elif contador == 4:
            Dato2 = input("Escriba el nuevo Ciudad de llegada:"+"\n")
            Dato[Indice]=Dato2 
            return viajes3_aux(Dato,Indice+1,contador+1)
        elif contador == 5:
            Dato2 = input("Escriba la nueva fecha de llegada:"+"\n")
            Dato[Indice]=Dato2 
            return viajes3_aux(Dato,Indice+1,contador+1)
        elif contador == 6:
            Dato2 = input("Escriba la nueva hora de llegada:"+"\n")
            Dato[Indice]=Dato2 
            return viajes3_aux(Dato,Indice+1,contador+1)
        elif contador == 7:
            Dato2 = input("Escriba la nueva empresa:"+"\n")
            Dato[Indice]=Dato2 
            return viajes3_aux(Dato,Indice+1,contador+1)
        else:
            Dato2 = input("Escriba el nuevo transporte:"+"\n")
            Dato[Indice]=Dato2 
            return viajes3_aux(Dato,Indice+1,contador+1)
        

def verViajes():
    Abrir = open("Viajes.txt","r")
    OPEN = Abrir.read()
    Abrir.close()
    print ("\n")
    print(OPEN)
    gestionTransporte()
    
#########################################################################################
#########################################################################################

def usuarioNormal():
    print(">>>>>>>>>>*****MENÚ*****<<<<<<<<<<"+"\n")
    print("1- Consulta de viajes.")
    print("2- Reservación de viaje.")
    print("3- Cancelación de reservación")
    print("4- Salir")
    
    opcionAdmin = input("¿Que opcion desea elegir?"+"\n")
    
    if opcionAdmin == "1":
        return consultar_viaje()
    
    elif opcionAdmin == "2":
        return reservar_viaje()
    
    elif opcionAdmin == "3":
        return cancelar_reservacion()
    
    elif opcionAdmin == "4":
        return menuPrincipal()
    
    else:
        print ("opcion incorrecta")
        return usuarioNormal()
        
#########################################################################################
#########################################################################################

def consultar_viaje():
    Abrir = open("Viajes.txt","r")
    for Agregar in Abrir:
        print(Agregar)
    Abrir.close()

    print("\n")
    gestionViajes()



































    
menuPrincipal()




































