from random import choice
import datetime
import matplotlib.pyplot as plt
import numpy as np

class General:
    def ObtenerFechayHora():
        FyH=datetime.datetime.today()
        return f"{FyH.strftime('%w/%m/%Y')}"

    def EliminarLineaLogin(filename, usuario, contraseña):
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(filename, 'w') as file:
            for line in lines:
                linea = line.strip().split(";")
                if linea[3] != usuario or linea[4] != contraseña:
                    file.write(line)
    
    def EliminarLineaForos(filename, Nombre, Fecha):
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(filename, 'w') as file:
            for line in lines:
                linea = line.strip().split(";")
                if linea[1] != Nombre or linea[0] != Fecha:
                    file.write(line)

    def EliminarLineaNoticias(filename,Titulo,Autor,Fecha):
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(filename, 'w') as file:
            for line in lines:
                linea = line.strip().split(";")
                if linea[0] != Titulo or linea[2] != Fecha or linea[1] != Autor:
                    file.write(line)
    
    def EliminarLineaGrados(filename,Facultad, Carrera):
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(filename, 'w') as file:
            for line in lines:
                linea = line.strip().split(";")
                if linea[0] != Facultad or linea[1] != Carrera:
                    file.write(line)

class Despedida:
    def respuesta():
        Respuestas_genericas=["Hasta luego","Adios","Hasta pronto","Bye bye~","Hasta la proxima","Nos vemos pronto"]
        print(choice(Respuestas_genericas))

class Login_register:
    #Programa de Registros
    def register(ClaveAdmin,Nombre,apellido,usuario,Contraseña):
        ClaveMaestra="JDNSJSSDLFAPNJASSABG"
        if not usuario or not Contraseña:
            print("Usuario o contraseña vacios")
            return
        with open('Login.csv', 'a') as Login:
            if ClaveAdmin==ClaveMaestra:
                Login.write(f"True;{Nombre};{apellido};{usuario};{Contraseña}\n")
                print("Usuario creado con exito")
            else:
                Login.write(f"False;{Nombre};{apellido};{usuario};{Contraseña}\n")
                print("Usuario creado con exito")
    #Programa de Login
    def login(usuario,contraseña):
        if not usuario or not contraseña:
            print("Usuario o contraseña vacios")
            return False
        with open('Login.csv', 'r') as archivo_login:
            for linea in archivo_login:
                datos = linea.strip().split(";")
                if len(datos) >= 5 and datos[3] == usuario and datos[4] == contraseña:
                    print(f"Bienvenido {datos[1]} , {datos[2]}")
                    return {
                        'Nombre':datos[1],
                        'Admin':datos[0]=="True"}
            print("Usuario o contraseña incorrectos")
        return False
    #Programa de Eliminar
    def eliminarpropio(usuario,contraseña,recontraseña):
        if not usuario or not contraseña or not recontraseña:
            print("Usuario o contraseña vacios")
            return
        if contraseña!=recontraseña:
            print("Contraseña no coincide")
            return
        if contraseña==recontraseña:
            General.EliminarLineaLogin("Login.csv",usuario,contraseña)
            print(f"Usuario eliminado {usuario}")
    def eliminarOtro(usuario,claveAdmin):
        clave="JDNSJSSDLFAPNJASSABG"
        if not usuario or not claveAdmin:
            print("Usuario o clave vacios")
            return
        if claveAdmin==clave:
            with open('Login.csv', 'r') as file:
                lines = file.readlines()
            with open('Login.csv', 'w') as file:
                for line in lines:
                    linea = line.strip().split(";")
                    if linea[3] != usuario:
                        file.write(line)
        else:
            print("Clave incorrecta")
        print(f"Usuario Eliminado {usuario}")

class Foro:
    #Programa de foros
    def CrearForo(Nombre,Contenido):
        Fecha = General.ObtenerFechayHora()
        with open('Foros.csv', 'a') as Foro:
            Foro.write(f"{Fecha};{Nombre};{Contenido}\n")
    #Programa leer foros
    def VerForo():
        try:
            with open('Foros.csv', 'r') as Foro:
                for linea in Foro:
                    print(linea)
        except FileNotFoundError:
            print("No hay foros")
    #Programa de eliminar foro
    def EliminarForo(Nombre,Fecha):
        General.EliminarLineaForos("Foros.csv",Nombre,Fecha)
        print("Foro Eliminado")

class Noticias:
    #Programa de Noticias
    def CrearNoticia(Titulo, Autor,Contenido):
        Fecha = General.ObtenerFechayHora()
        with open('Noticias.csv', 'a') as Noticia:
            Noticia.write(f"{Titulo};{Autor};{Fecha};{Contenido}\n")
    #Programa leer Noticias
    def VerNoticia():
        try:
            with open('Noticias.csv', 'r') as Noticia:
                for linea in Noticia:
                    print(linea)
        except FileNotFoundError:
            print("No hay Noticias")
    #Programa de eliminar Noticia
    def EliminarNoticia(Titulo,Autor,Fecha):
        General.EliminarLineaNoticias("Noticias.csv",Titulo,Autor,Fecha)
        print("Noticia Eliminada")

class Grados:
    #Registrar carreras
    def RegistrarCarrera(Facultad,Carrera,Semestre,Creditos,Hlibres):
        if not Carrera or not Semestre or not Creditos or not Hlibres:
            print("No se puede registrar la carrera")
            return
        with open('Grados.csv', 'a') as Grado:
            Grado.write(f"{Facultad};{Carrera};{Semestre};{Creditos};{Hlibres}\n")
    #Buscar Carrera
    def BuscarCarrera(Facultad,Carrera):
        if not Carrera or not Facultad:
            print("Debes llenar el campo")
            return False
        with open('Grados.csv', 'r') as Grado:
            for linea in Grado:
                datos = linea.strip().split(";")
                if len(datos) >= 5 and datos[0] == Facultad and datos[1] == Carrera: 
                    return {
                        "Carrera": datos[1],
                        "Semestre": datos[2],
                        "Creditos": datos[3],
                        "Horas Libres": datos[4]}
            print("Carrera no Encontrada")
        return False
    #Eliminar carrera
    def EliminarCarrera(Facultad,Carrera):
        General.EliminarLineaGrados("Grados.csv",Facultad,Carrera)
        print("Carrera Eliminada")

    #Promedio De Todo
    def PromedioTotalCarrerra(Total,semestre):
        return (Total+(semestre/2))/2
    def PromedioAño(Total):
        return (Total+1)/2
    def PromedioSemestre(Total):
        return (Total+1)/2
    def PromedioMes(Total):
        return (Total+1)/2
    def GuardarPromedios(Total,Año,Semestre,Mes):
        Guardar=[]
        Guardar.append(Total)
        Guardar.append(Año)
        Guardar.append(Semestre)
        Guardar.append(Mes)
        return Guardar

    #Grafica Total Carrera
    def Grafica(Carrera,CreditosTotales,HoraslibresTotales,SemestreTotal,Creditos,Horaslibres,Semestre):
        # Datos para la gráfica
        categorias = ['Creditos', 'Horas Libres', 'Semestres']
        SinCompletar = [CreditosTotales, HoraslibresTotales, SemestreTotal]
        Completado = [Creditos, Horaslibres, Semestre]
        # Convertir a array numpy para facilitar los cálculos
        datos = np.array([SinCompletar, Completado])
        # Calcular los porcentajes
        totales = np.sum(datos, axis=0)
        porcentajes = datos / totales[np.newaxis, :] * 100
        # Crear la gráfica
        fig, ax = plt.subplots(figsize=(10, 6))
        # Crear las barras apiladas horizontales
        base = np.zeros(len(categorias))
        nombres_grupos = ['Sin Completar','Completado']
        colores = ['#008000', '#FF0000']  # Verdes y rojos
        for i, fila in enumerate(porcentajes):
            ax.barh(categorias, fila, left=base, label=nombres_grupos[i], color=colores[i])
            base += fila
        # Personalizar la gráfica
        ax.set_title(f'Gráfica de la carrera {Carrera}', fontsize=16)
        ax.set_xlabel('Porcentaje', fontsize=12)
        ax.legend(loc='upper right')
        ax.set_xlim(0, 100)
        # Añadir etiquetas de porcentaje en cada sección
        for i, fila in enumerate(porcentajes):
            ax.bar_label(ax.containers[i], fmt='%.1f%%', label_type='center')
        # Ajustar el espaciado
        plt.tight_layout()
        # Mostrar la gráfica
        plt.show()
