import time
import os
from Clases_1 import *
#Variables iniciales
MenuLoguear=0
MenuPrincipal=0
SubMenu=0
MenuGraduarse=0
MenuForos=0
MenuNoticias=0
Dia=""
Mes=""
Año=""
Fecha=""
Eliminar=""
rta=""
while True:
    print("Bienvenido")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    #Por si insertan mal la entrada
    try: MenuLoguear = int(input("Ingrese una opción: "))
    except ValueError: print("Ingresa el numero de la opcion que deseas escojer"); continue
    #Iniciar Sesion
    if  MenuLoguear == 1:
        Usuario=input("Inserta tu usuario:  ")
        Contraseña=input("Inserta tu contraseña:  ")
        #Informacion del usuario
        UsInfo=Login_register.login(Usuario,Contraseña)
        #Acceso Concedido
        if UsInfo:
            NombreUsuario=UsInfo['Nombre']
            print("Accediendo...")
            time.sleep(3)
            print("Acceso exitoso")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            #Diferenciar entre Admin y Usuario
            #ADMINISTRADOR
            if UsInfo['Admin']:
                print(
                    "Eres Administrador\n",
                    "Tienes permisos que los demas no tienen\n",
                    "Puedes eliminar cualquier foro, añadir y eliminar noticias\n",
                    "Añadir informacion sobre los grados\n",
                    "Puedes eliminar cualquier usuario"
                )
                time.sleep(10)
                os.system('cls' if os.name == 'nt' else 'clear')
                #Menu Principal
                while True:
                    print("Que deseas realizar?")
                    print("1. Cuanto falta para graduarme?") #Falta
                    print("2. Foros")
                    print("3. Noticias") #Falta
                    print("4. Eliminar cuenta")
                    print("5. Cerrar sesion")
                    #Por si insertan mal la entrada
                    try: MenuPrincipal = int(input("Ingrese una opción: "))
                    except ValueError: print("Ingresa el numero de la opcion que deseas escojer");continue
                    #Menu de Graduarse
                    if MenuPrincipal == 1:
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while True:
                            print("Que deseas hacer?")
                            print("1. Registrar una carrera")
                            print("2. Acceder a una carrera")
                            print("3. Eliminar una carrera")
                            print("4. Volver")
                            #Por si insertan mal la entrada
                            try:  SubMenu = int(input("Ingrese una opción: "))
                            except ValueError: print("Ingresa el numero de la opcion que deseas escojer"); continue
                            #Registrar una carrera
                            if SubMenu == 1:
                                time.sleep(5)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                #Insertar datos de la carrera
                                try: Facultad = str(input("Ingrese la facultad: "))
                                except ValueError: continue
                                try: Carrera = str(input("Inserta el nombre de la carrera: "))
                                except ValueError: continue
                                try: Semestre = int(input("Inserta la cantidad total de semestre en la carrera: "))
                                except ValueError: print("Ingresa un numero");continue
                                try: Creditos = int(input("Inserta la cantidad de creditos totales en la carrera: "))
                                except ValueError: print("Ingresa un numero");continue
                                try: Hlibres =  int(input("Inserta la cantidad de horas libres en la carrera: "))
                                except ValueError: print("Ingresa un numero");continue
                                Grados.RegistrarCarrera(Facultad,Carrera,Semestre,Creditos,Hlibres)
                                time.sleep(5)
                                os.system('cls' if os.name == 'nt' else 'clear')
                            #Acceder a la carrera
                            elif SubMenu == 2:
                                time.sleep(5)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                CarreraInfo=Grados.BuscarCarrera(input("Inserta la facultad: "),input("Inserta el nombre de tu carrera: "))
                                if CarreraInfo:
                                    CarreraTot=CarreraInfo["Carrera"]
                                    SemestreTot=int(CarreraInfo["Semestre"])
                                    CreditosTot=int(CarreraInfo["Creditos"])
                                    HorasLibresTot=int(CarreraInfo["Horas Libres"])
                                    while True:
                                        print("Que deseas ver?")
                                        print("1. Cantidad de Creditos que me faltan")
                                        print("2. Cantidad de Horas libres que me faltan")
                                        print("3. Cantidad de Semestres que me faltan")
                                        print("4. Grafica general")
                                        print("5. Promedio general")
                                        print("6. Cerrar sesion")
                                        #Por si insertan mal la entrada
                                        try: MenuGraduarse = int(input("Ingrese una opción: "))
                                        except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                                        #Menu de Creditos
                                        if MenuGraduarse == 1:
                                            time.sleep(5)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            try: CreditosFaltan = int(input("Inserta la cantidad de creditos que ya has obtenido: "))
                                            except ValueError: print("Ingresa un numero");continue
                                            print(f"Te faltan: {CreditosTot-CreditosFaltan} creditos")
                                            input("Pulsa Cualquier tecla para continuar...")
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        #Menu de Horas libres
                                        elif MenuGraduarse == 2:
                                            time.sleep(5)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            try:  Horas = int(input("Inserta la cantidad de horas libres que llevas: "))
                                            except ValueError: print("Ingresa un numero");continue
                                            print(f"Te faltan {HorasLibresTot-Horas} horas libres")
                                            input("Pulsa Cualquier tecla para continuar...")
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        #Menu de Semestres
                                        elif MenuGraduarse == 3:
                                            time.sleep(5)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            try: SemestreActual=int(input("Ingresa el semestre actual: "))
                                            except ValueError: print("Ingresa un numero") ; continue
                                            print(f"Te faltan: {SemestreTot - SemestreActual} Semestres")
                                            input("Pulsa Cualquier tecla para continuar...")
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        #Grafica de Graduarse
                                        elif MenuGraduarse == 4:
                                            time.sleep(5)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print("Antes de mostrarte la grafica necesito que me des la siguiente informacion")
                                            try: Creditos=int(input("Inserta el numero de creditos que llevas completados: "))
                                            except ValueError: print("Ingresa un numero") ; continue
                                            try: HorasLibres=int(input("Inserta el numero de horas libres que llevas completados: "))
                                            except ValueError: print("Ingresa un numero") ; continue
                                            try: SemestreActual=int(input("Inserta el semestre en el que te encuentras: "))
                                            except ValueError: print("Ingresa un numero") ; continue
                                            Grados.Grafica(CarreraTot,CreditosTot,HorasLibresTot,SemestreTot,Creditos,HorasLibres,SemestreActual)
                                        #Promedio General
                                        elif MenuGraduarse == 5:
                                            time.sleep(2)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            #Creditos
                                            print("Haciendo calculos matematicos")
                                            print("Espere un poco...")
                                            time.sleep(5)
                                            Total = Grados.PromedioTotalCarrerra(CreditosTot,SemestreTot)
                                            Año = Grados.PromedioAño(Total)
                                            Semestre = Grados.PromedioSemestre(Año)
                                            Meses = Grados.PrimedioMes(Semestre)
                                            PromedioCreditos=Grados.GuardarPromedios(Total,Año,Semestre,Meses)
                                            #Horas Libres
                                            Total = Grados.PromedioTotalCarrerra(HorasLibresTot,SemestreTot)
                                            Año = Grados.PromedioAño(Total)
                                            Semestre = Grados.PromedioSemestre(Año)
                                            Meses = Grados.PrimedioMes(Semestre)
                                            PromedioHorasLibres=Grados.GuardarPromedios(Total,Año,Semestre,Meses)
                                            print(f"El promedio de creditos por carrera es: {PromedioCreditos[0]}")
                                            print(f"El promedio de creditos por Año es: {PromedioCreditos[1]}")
                                            print(f"El promedio de creditos por Semestre es: {PromedioCreditos[2]}")
                                            print(f"El promedio de creditos por carrera es: {PromedioCreditos[3]}")
                                            print("_"+40)
                                            print(f"El promedio de Horas Libres por carrera es: {PromedioHorasLibres[0]}")
                                            print(f"El promedio de Horas Libres por Año es: {PromedioHorasLibres[1]}")
                                            print(f"El promedio de Horas Libres por Semestre es: {PromedioHorasLibres[2]}")
                                            print(f"El promedio de Horas Libres por carrera es: {PromedioHorasLibres[3]}")
                                            input("Pulsa Cualquier tecla para continuar...")
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        #Volver al Menu Principal
                                        elif MenuGraduarse == 6: print("Volviendo al Sub Menu...") ; time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear');break
                                        #Opcion no valida
                                        else: print("Opcion no valida")
                            #Eliminar la carrera
                            elif SubMenu == 3:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                try: Carrera = str(input("Inserta el nombre de la carrera que deseas eliminar: "))
                                except ValueError: continue
                                Grados.EliminarCarrera(Carrera)
                                time.sleep(5)
                                os.system('cls' if os.name == 'nt' else 'clear')
                            #Volviendo al Menu Principal
                            elif SubMenu == 4: print("Volviendo al Menu Principal...") ; time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear') ; break
                            #Opcion no valida
                            else: print("Opcion no valida")
                    #Menu de Foros
                    elif MenuPrincipal ==2:
                        print("Accediendo al Menu de foros")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while True:
                            print("Que deseas realizar?")
                            print("1. Crear foro")
                            print("2. Ver foros")
                            print("3. Eliminar foro")
                            print("4. Volver")
                            #Por si insertan mal la entrada
                            try: MenuForos = int(input("Ingrese una opción: "))
                            except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                            #Apartado de Crear Foro
                            if  MenuForos == 1:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                while True:
                                    Contenido=input("Inserta el contenido de tu foro: ")
                                    Foro.CrearForo(NombreUsuario,Contenido)
                                    time.sleep(1)
                                    print("Foro creado con exito")
                                    #Por si insertan mal la entrada
                                    try: rta=str(input("Quieres crear  otro foro? (Y/N): "))
                                    except ValueError: print("Responde con 'Y' o 'N'") ; continue
                                    if  rta.upper() == "N": time.sleep(2); os.system('cls' if os.name == 'nt' else 'clear');break
                                    elif rta.upper() == "Y": continue
                                    else: print("Opción no valida")
                            #Apartado de Ver foros
                            elif MenuForos == 2:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Estos son los foros que hay")
                                time.sleep(1)
                                Foro.VerForo()
                                #Por si insertan mal la entrada
                                try: rta=str(input("Quieres salir? (Y/N): "))
                                except ValueError: print("Responde con 'Y' o 'N'") ; continue
                                if  rta.upper() == "N": continue
                                elif rta.upper() == "Y": time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear');break
                                else: print("Opción no valida")
                            #Apartado de Eliminar Foro
                            elif MenuForos == 3:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                while True:
                                    print("Que deseas eliminar?")
                                    print("1. Eliminar foro propio")
                                    print("2. Eliminar foro de otro usuario")
                                    print("3. Volver")
                                    #Por si insertan mal la entrada
                                    try: rta=int(input("Ingrese una opción: "))
                                    except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                                    #Eliminar Foro propio
                                    if rta == 1:
                                        time.sleep(2)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Para eliminar un foro que hayas subido necesito que insertes la fecha")
                                        Dia=str(input("Inserta el numero del dia: "))
                                        Mes=str(input("Inserta el numero del mes: "))
                                        Año=str(input("Inserta el año: "))
                                        Fecha=Dia+"/"+Mes+"/"+Año
                                        Foro.EliminarForo(NombreUsuario,Fecha)
                                        time.sleep(5)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    #Eliminar otro Foro
                                    elif rta == 2:
                                        time.sleep(2)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Para eliminar un foro de otro usuario necesito que insertes el nombre del usuario y la fecha")
                                        NombreUs=input("Inserta el nombre del usuario: ")
                                        Dia=str(input("Inserta el numero del dia: "))
                                        Mes=str(input("Inserta el numero del mes: "))
                                        Año=str(input("Inserta el año: "))
                                        Fecha=Dia+"/"+Mes+"/"+Año
                                        Foro.EliminarForo(NombreUs,Fecha)
                                        time.sleep(5)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    #Volver
                                    elif rta == 3: print("Regresando al Menu de MenuForos...");time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear'); break
                                    #Opcion no valida
                                    else: print("Opción no valida")
                            #Volver al Menu Principal
                            elif MenuForos == 4: print("Volviendo al Menu Principal...");time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear'); break
                            #opcion invalida
                            else: print("Opción no válida")
                    #Menu de Noticias
                    elif  MenuPrincipal == 3:
                        print("Accediendo al menu de Noticias")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while True:
                            print("Que deseas hacer?")
                            print("1. Ver Noticias")
                            print("2. Crear Noticia")
                            print("3. Eliminar Noticia")
                            print("4. Volver")
                            #Por si insertan mal la entrada
                            try: MenuNoticias=int(input("Ingrese una opción: "))
                            except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                            #Ver Noticias
                            if MenuNoticias == 1:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Estos son las Noticias que hay")
                                time.sleep(1)
                                Noticias.VerNoticia()
                                #Por si insertan mal la entrada
                                try: rta=str(input("Quieres salir? (Y/N): "))
                                except ValueError: print("Responde con 'Y' o 'N'") ; continue
                                if  rta.upper() == "N": continue
                                elif rta.upper() == "Y": time.sleep(2); os.system('cls' if os.name == 'nt' else 'clear'); break
                                else: print("Opción no valida")
                            #Crear Noticia
                            elif MenuNoticias == 2:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                while True:
                                    Titulo=input("Inserta el Titulo de la Noticia: ")
                                    Autor=input("Inserta el autor de la Noticia: ")
                                    Contenido=input("Inserta el contenido de la noticia: ")
                                    Noticias.CrearNoticia(Titulo,Autor,Contenido)
                                    time.sleep(1)
                                    print("Noticia creada con exito")
                                    #Por si insertan mal la entrada
                                    try: rta=str(input("Quieres crear  otra Noticia? (Y/N): "))
                                    except ValueError: print("Responde con 'Y' o 'N'") ; continue
                                    if  rta.upper() == "N": time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear');break
                                    elif rta.upper() == "Y": continue
                                    else: print("Opción no valida")
                            #Eliminar Noticia
                            elif MenuNoticias == 3:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Para eliminar una noticia necesitamos los siguientes datos")
                                Titulo=input("Inserta el Titulo de la Noticia que deseas eliminar: ")
                                Autor=input("Inserta el autor de la Noticia que deseas eliminar: ")
                                Dia=  input("Inserta el numero del dia de la Noticia que deseas eliminar: ")
                                Mes=  input("Inserta el numero del mes de la Noticia que deseas eliminar: ")
                                Año=  input("Inserta el numero del año de la Noticia que deseas eliminar: ")
                                Fecha=  Dia + "/" + Mes + "/" + Año
                                Noticias.EliminarNoticia(Titulo,Autor,Fecha)
                                time.sleep(5)
                                os.system('cls' if os.name == 'nt' else 'clear')
                            #Volver al Menu Principal
                            elif MenuNoticias == 4: print("Regresando al Menu Principal...");time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear'); break
                            #Opción no valida
                            else: print("Opción no válida")
                    #Menu de Eliminar Usuario
                    elif MenuPrincipal  == 4:
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Que usuario deseas eliminar?")
                        print("1. Eliminar esta cuenta")
                        print("2. Eliminar otra cuenta")
                        print("3. Volver al Menu Principal")
                        try: rta=int(input("Inserta la opción: "))
                        except ValueError: print("Ingresa el numero de la opcion que deseas escoger") ; continue
                        #Eliminar la cuenta actual
                        if rta == 1:
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Accediendo a Eliminar cuenta propia...")
                            time.sleep(2)
                            Recontraseña=input("Inserta nuevamente tu contraseña: ")
                            #Por si insertan mal la entrada
                            try: Eliminar=str(input("Estas seguro de eliminar tu cuenta? (Y/N): "))
                            except ValueError: print("Responde con 'Y' o 'N'") ; continue
                            if Eliminar.upper() == "Y": Login_register.eliminarpropio(Usuario,Contraseña,Recontraseña);time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear'); break
                            elif  Eliminar.upper() == "N": print("Cancelando") ;time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear') ; break
                            else: print("Respuesta invalida")
                        #Eliminar otra cuenta
                        elif rta == 2:
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Accediendo a Eliminar otra cuenta...")
                            time.sleep(2)
                            print("Para eliminar una cuenta necesito que me insertes el nombre de usuario\n","Y la contraseña con la que te volviste administrador")
                            Usuario=input("Inserta el nombre de usuario: ")
                            AdminContraseña=input("Inserta la contraseña de Administrador: ")
                            try: Eliminar=str(input("Estas seguro de eliminar la cuenta? (Y/N): "))
                            except ValueError: print("Responde con 'Y' o 'N'") ; continue
                            if Eliminar.upper() == "Y": Login_register.eliminarOtro(Usuario,AdminContraseña);time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear'); break
                            elif Eliminar.upper() == "N": print("Cancelando");time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear') ; break
                            else: print("Respuesta invalida")
                    #Cerrar Sesion
                    elif  MenuPrincipal == 5: print("Cerrando sesion...");time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear'); break
                    #Opcion no valida
                    else: print("Opción no válida")
            #USUARIO
            else:
                print(
                    "Eres Usuario\n",
                    "Puedes crear foros, ver foros, eliminar foros, ver noticias, ver grados\n",
                    "Puedes ver tu perfil y modificarlo"
                    )
                time.sleep(10)
                os.system('cls' if os.name == 'nt' else 'clear')
                #Menu Principal
                while True:
                    print("Que deseas realizar?")
                    print("1. Cuanto falta para graduarme?") #Falta
                    print("2. Foros")
                    print("3. Noticias") #Falta
                    print("4. Eliminar cuenta")
                    print("5. Cerrar sesion")
                    #Por si insertan mal la entrada
                    try: MenuPrincipal = int(input("Ingrese una opción: "))
                    except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                    #Menu de Graduarse
                    if MenuPrincipal == 1:
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        CarreraInfo=Grados.BuscarCarrera(input("Inserta la facultad: "),input("Inserta el nombre de tu carrera: "))
                        if CarreraInfo:
                            CarreraTot=CarreraInfo["Carrera"]
                            SemestreTot=int(CarreraInfo["Semestre"])
                            CreditosTot=int(CarreraInfo["Creditos"])
                            HorasLibresTot=int(CarreraInfo["Horas Libres"])
                            while True:
                                print("Que deseas ver?")
                                print("1. Cantidad de Creditos que me faltan")
                                print("2. Cantidad de Horas libres que me faltan")
                                print("3. Cantidad de Semestres que me faltan")
                                print("4. Grafica general")
                                print("5. Promedio general")
                                print("6. Cerrar sesion")
                                #Por si insertan mal la entrada
                                try: MenuGraduarse = int(input("Ingrese una opción: "))
                                except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                                #Menu de Creditos
                                if MenuGraduarse == 1:
                                    time.sleep(5)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    try: CreditosFaltan = int(input("Inserta la cantidad de creditos que ya has obtenido: "))
                                    except ValueError: print("Ingresa un numero");continue
                                    print(f"Te faltan: {CreditosTot-CreditosFaltan} creditos")
                                    input("Pulsa Cualquier tecla para continuar...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                #Menu de Horas libres
                                elif MenuGraduarse == 2:
                                    time.sleep(5)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    try:  Horas = int(input("Inserta la cantidad de horas libres que llevas: "))
                                    except ValueError: print("Ingresa un numero");continue
                                    print(f"Te faltan {HorasLibresTot-Horas} horas libres")
                                    input("Pulsa Cualquier tecla para continuar...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                #Menu de Semestres
                                elif MenuGraduarse == 3:
                                    time.sleep(5)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    try: SemestreActual=int(input("Ingresa el semestre actual: "))
                                    except ValueError: print("Ingresa un numero") ; continue
                                    print(f"Te faltan: {SemestreTot - SemestreActual} Semestres")
                                    input("Pulsa Cualquier tecla para continuar...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                #Grafica de Graduarse
                                elif MenuGraduarse == 4:
                                    time.sleep(5)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Antes de mostrarte la grafica necesito que me des la siguiente informacion")
                                    try: Creditos=int(input("Inserta el numero de creditos que llevas completados: "))
                                    except ValueError: print("Ingresa un numero") ; continue
                                    try: HorasLibres=int(input("Inserta el numero de horas libres que llevas completados: "))
                                    except ValueError: print("Ingresa un numero") ; continue
                                    try: SemestreActual=int(input("Inserta el semestre en el que te encuentras: "))
                                    except ValueError: print("Ingresa un numero") ; continue
                                    Grados.Grafica(CarreraTot,CreditosTot,HorasLibresTot,SemestreTot,Creditos,HorasLibres,SemestreActual)
                                #Promedio General
                                elif MenuGraduarse == 5:
                                    time.sleep(2)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    #Creditos
                                    print("Haciendo calculos matematicos")
                                    print("Espere un poco...")
                                    time.sleep(5)
                                    Total = Grados.PromedioTotalCarrerra(CreditosTot,SemestreTot)
                                    Año = Grados.PromedioAño(Total)
                                    Semestre = Grados.PromedioSemestre(Año)
                                    Meses = Grados.PrimedioMes(Semestre)
                                    PromedioCreditos=Grados.GuardarPromedios(Total,Año,Semestre,Meses)
                                    #Horas Libres
                                    Total = Grados.PromedioTotalCarrerra(HorasLibresTot,SemestreTot)
                                    Año = Grados.PromedioAño(Total)
                                    Semestre = Grados.PromedioSemestre(Año)
                                    Meses = Grados.PrimedioMes(Semestre)
                                    PromedioHorasLibres=Grados.GuardarPromedios(Total,Año,Semestre,Meses)
                                    print(f"El promedio de creditos por carrera es: {PromedioCreditos[0]}")
                                    print(f"El promedio de creditos por Año es: {PromedioCreditos[1]}")
                                    print(f"El promedio de creditos por Semestre es: {PromedioCreditos[2]}")
                                    print(f"El promedio de creditos por carrera es: {PromedioCreditos[3]}")
                                    print("_"+40)
                                    print(f"El promedio de Horas Libres por carrera es: {PromedioHorasLibres[0]}")
                                    print(f"El promedio de Horas Libres por Año es: {PromedioHorasLibres[1]}")
                                    print(f"El promedio de Horas Libres por Semestre es: {PromedioHorasLibres[2]}")
                                    print(f"El promedio de Horas Libres por carrera es: {PromedioHorasLibres[3]}")
                                    input("Pulsa Cualquier tecla para continuar...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                #Volver al Menu Principal
                                elif MenuGraduarse == 6: print("Volviendo al Sub Menu...") ; time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear');break
                                #Opcion no valida
                                else: print("Opcion no valida")
                    #Menu de Foros
                    elif MenuPrincipal ==2:
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Accediendo al Menu de foros")
                        time.sleep(2)
                        while True:
                            print("Que deseas realizar?")
                            print("1. Crear foro")
                            print("2. Ver foros")
                            print("3. Eliminar foro")
                            print("4. Volver")
                            #Por si insertan mal la entrada
                            try: MenuForos = int(input("Ingrese una opción: "))
                            except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                            #Apartado de Crear Foro
                            if  MenuForos == 1:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                while True:
                                    Contenido=input("Inserta el contenido de tu foro: ")
                                    Foro.CrearForo(NombreUsuario,Contenido)
                                    time.sleep(1)
                                    print("Foro creado con exito")
                                    #Por si insertan mal la entrada
                                    try: rta=str(input("Quieres crear  otro foro? (Y/N): "))
                                    except ValueError: print("Responde con 'Y' o 'N'") ; continue
                                    if  rta.upper() == "N": time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear');break
                                    elif rta.upper() == "Y": continue
                                    else: print("Opción no valida")
                            #Apartado de Ver MenuForos
                            elif MenuForos == 2:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Estos son los foros que hay")
                                time.sleep(1)
                                Foro.VerForo()
                                #Por si insertan mal la entrada
                                try: rta=str(input("Quieres salir? (Y/N): "))
                                except ValueError: print("Responde con 'Y' o 'N'") ; continue
                                if  rta.upper() == "N": continue
                                elif rta.upper() == "Y": time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear');break
                                else: print("Opción no valida")
                            #Apartado de Eliminar Foro
                            elif MenuForos == 3:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Para eliminar un foro que hayas subido necesito que insertes la fecha")
                                Dia=str(input("Inserta el numero del dia: "))
                                Mes=str(input("Inserta el numero del mes: "))
                                Año=str(input("Inserta el año: "))
                                Fecha=Dia+"/"+Mes+"/"+Año
                                Foro.EliminarForo(NombreUsuario,Fecha)
                                time.sleep(5)
                                os.system('cls' if os.name == 'nt' else 'clear')
                            #Volver al Menu Principal
                            elif MenuForos == 4: print("Volviendo al Menu Principal"); time.sleep(5);os.system('cls' if os.name == 'nt' else 'clear'); break
                            #opcion invalida
                            else: print("Opción no válida")
                    #Menu de Noticias
                    elif  MenuPrincipal == 3:
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Accediendo al menu de Noticias...")
                        time.sleep(2)
                        while True:
                            print("Que deseas hacer?")
                            print("1. Ver Noticias")
                            print("2. Volver")
                            #Por si insertan mal la entrada
                            try: MenuNoticias=int(input("Ingrese una opción: "))
                            except ValueError: print("Ingresa el numero de la opcion que deseas escojer") ; continue
                            #Ver Noticias
                            if MenuNoticias == 1:
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Estos son las Noticias que hay")
                                time.sleep(1)
                                Noticias.VerNoticia()
                                #Por si insertan mal la entrada
                                try: rta=str(input("Quieres salir? (Y/N): "))
                                except ValueError: print("Responde con 'Y' o 'N'") ; continue
                                if  rta.upper() == "N": continue
                                elif rta.upper() == "Y": time.sleep(2); os.system('cls' if os.name == 'nt' else 'clear');break
                                else: print("Opción no valida")
                            #Volver al Menu Principal
                            elif  MenuNoticias == 2: print("Regresando al Menu Principal...") ;time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear') ; break
                            #Opción no valida
                            else: print("Opción no válida")
                    #Menu de Eliminar Usuario
                    elif MenuPrincipal  == 4:
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        Recontraseña=input("Inserta nuevamente tu contraseña: ")
                        #Por si insertan mal la entrada
                        try: Eliminar=str(input("Estas seguro de eliminar tu cuenta? (Y/N): "))
                        except ValueError: print("Responde con 'Y' o 'N'") ; continue
                        if Eliminar.upper() == "Y": Login_register.eliminarpropio(Usuario,Contraseña,Recontraseña);time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear');break
                        elif  Eliminar.upper() == "N": print("Cancelando") ;time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear');break
                        else: print("Respuesta invalida")
                    #Cerrar Sesion
                    elif  MenuPrincipal == 5: print("Cerrando sesion...") ; time.sleep(3);os.system('cls' if os.name == 'nt' else 'clear'); break
                    #Opcion no valida
                    else: print("Opción no válida")
    #Nuevo Registro
    elif MenuLoguear == 2:
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ClaveAdmin=input("Ingresa la clave maestra (si la tienes): ")
        Nombre=input("Ingresa tu Nombre: ")
        Apellido=input("Ingresa tu Apellido: ")
        Usuario=input("Ingresa tu Usuario: ")
        Contraseña=input("Ingresa tu Contraseña: ")
        Login_register.register(ClaveAdmin,Nombre,Apellido,Usuario,Contraseña)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
    #Despedida del programa
    elif MenuLoguear == 3: Despedida.respuesta() ; break ; time.sleep(5)
    #Opcion no valida
    else: print("Opción no válida") ; continue
quit()
