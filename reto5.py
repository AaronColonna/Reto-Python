import platform
import os
import random
from math import asin, cos, sin, sqrt, radians, degrees
os.system("cls")


print("Bienvenido al sistema de ubicación para zonas públicas WIFI") #Mensaje de bienvenida al sistema

us = "51590" #Usuario predefinido: código de grupo del curso fundamentos de programación
clv = "09515" #Contraseña predefinidida: código de grupo del curso fundamentos de programación inverso
#suma = 0

us_Entrada = input("Nombre de usuario : ") #Usuario ingresa nombre de usuario
if us_Entrada == "Tripulante2022":
    print("Este fue mi primer programa y vamos por más")

elif us_Entrada != us and us_Entrada != "Tripulante2022": #Validación del nombre de usuario
    print("Error") #Nombre de usuario incorrecto

else : #contraseña
    clv_Entrada = input("Contraseña: ") #Usuario ingresa contraseña

    if clv_Entrada == "m1s10nt1c":
        cantidad = int(input("¿Cuántas latitudes vas a ingresar?"))
        for i in range(0,cantidad):
            latitudes = float(input(f"Ingrese latitud {i+1}: "))
            suma = 0 + latitudes
        promerdio_Latitud = suma/cantidad
        print(f"El promedio es: {promerdio_Latitud}")

    elif clv_Entrada!= clv and clv_Entrada != "m1s10nt1c": #Validación de contraseña
        print("Error") #Contraseña incorrecta

    else : #captcha de seguridad 
        captcha1 = 590 #ultimos 3 digitos código de grupo del curso fundamentos de programación
        captcha2 = 5-1+5-0 #penultimo número del código de grupo obtenido con operaciones usando los números restantes
        result = int(input(f"{captcha1} + {captcha2} = ")) #suma de 590 + 9, el usuario ingresará el resultado
        if result != captcha1 + captcha2 : #Validación de captcha
            print("Error") #Captcha incorrecto
        else :
            os.system("cls")
            print("Sesión iniciada") #Confirmación de ingreso.
            
            opcion1 = "Cambiar contraseña"
            opcion2 = "Ingresar coordenadas actuales"
            opcion3 = "Ubicar zona wifi más cercana"
            opcion4 = "Guardar archivo con ubicación cercana"
            opcion5 = "Actualizar registros de zonas wifi desde archivo"
            opcion6 = "Elegir opción de menú favorita"
            opcion7 = "Cerrar sesión"

            opcion1Copy = opcion1
            opcion2Copy = opcion2
            opcion3Copy = opcion3
            opcion4Copy = opcion4
            opcion5Copy = opcion5
            opcion6Copy = opcion6
            opcion7Copy = opcion7

            adivinanza_primera = 9
            adivinanza_segunda = 0

            error = 0
            ErrorCoordenada = "Error"

            lista_Coordenadas = []

            radio = 6372.795477598
            lista_Distancia=[]
            wifi_Actual=None
            distancia_Tiempo=None
            coordenadas_Predeterminada = [[6.632,-72.984,285],[6.564,-73.061,127],[6.531,-73.002,15],[6.623,-72.978,56]]

            informacion = {"actual": ["latitud","longitud"],
		                    "zonawifi1": ["latitud", "longitud", "usuarios"],
		                    "recorrido": ["distancia", "mediotransporte","tiempopromedio"]}
            
            alistamiento=False

            def ingresar_Coordenadas(lista_Original):
                lista_Copy = list(lista_Original)
                for i in range(0,3):
                    lista_Copy.append([])
                    latitud = input("Ingrese la latitud:")
                    while latitud == "":
                        exit("Error")
                    latitud = float(latitud)
                    if latitud >= 6.532 and latitud <= 6.690:
                        longitud = input("Ingrese la longitud: ")
                        while longitud == "":
                            exit("Error")
                        longitud = float(longitud)
                        if longitud >= -73.120 and longitud <= -72.872:
                            lista_Copy[i].insert(0,latitud)
                            lista_Copy[i].insert(1,longitud)
                        else:
                            lista_Copy = "Error"
                            print("Error coordenada")
                            return lista_Copy
                    else:
                        lista_Copy = "Error"
                        print("Error coordenada")
                        return lista_Copy
                return lista_Copy

            def ordenar_Latitud_Norte(lista_Original):
                print(f"La coordenada {lista_Original.index(max(lista_Original, key=lambda posicion: posicion[0])) + 1} es la que está más al norte")
            
            def ordenar_Latitud_Sur(lista_Original):
                print(f"La coordenada {lista_Original.index(min(lista_Original, key=lambda posicion: posicion[0])) + 1} es la que está mas al sur")

            def imprimir_Coordenads(lista_Original):
                lista_Copy=list(lista_Original)

                for x in range(0,len(lista_Copy)):
                    print(f"coordenada [Latitud,longitud] {x+1}: {lista_Copy[x]}")
                ordenar_Latitud_Norte(lista_Copy)
                ordenar_Latitud_Sur(lista_Copy)
                coordenada_Modificada=int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada.Presione 0 para regresar al menú:"))
                if coordenada_Modificada !=1 and coordenada_Modificada !=2 and coordenada_Modificada !=3:
                    print("Error actualización")
                    exit()
                else:
                    actualizar_Coordenadas(coordenada_Modificada,lista_Original)

            def actualizar_Coordenadas(coordena_Modificada ,lista_Original):
                lista_Copy =list(lista_Original)
                coordena_Modificada = coordena_Modificada-1
                latitud = input("Ingrese la latitud: ")
                while latitud == "":
                    exit("Error")
                latitud=float(latitud)
                if latitud >= 6.532 and latitud <= 6.690:
                    longitud=input("Ingrese la longitud: ")
                    while longitud == "":
                        exit("Error")
                    longitud=float(longitud)
                    if longitud >= -73.120 and longitud <= -72.872:
                        lista_Copy[coordena_Modificada][0]=latitud
                        lista_Copy[coordena_Modificada][1]=longitud
                    else:
                        lista_Copy = "Error"
                        print("Error")
                        return lista_Copy
                else:
                    lista_Copy = "Error"
                    print("Error")
                    return lista_Copy
                
                return lista_Copy

            def wifi_Favorito(lista_Original):
                if lista_Original==[]:
                    print("Error sin registro de coordenadas")
                    exit()
                else:
                    imprimir_Wifi_Favorito(lista_Original)
        
            def imprimir_Wifi_Favorito(lista_Original):
                lista_Copy=list(lista_Original)

                for x in range(0,len(lista_Copy)):
                    print(f"coordenada [latitud,lingitud] {x+1} :{lista_Copy[x]}")
                    
                wifi=int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión:"))
                if wifi == 1 or wifi ==2 or wifi ==3:
                    global wifi_Actual
                    wifi_Actual=lista_Coordenadas[wifi-1]
                    informacion["actual"]=wifi_Actual #Guardamos la información del restaurante actual en el diccionario
                    preparar_Datos(wifi,lista_Copy,coordenadas_Predeterminada)
                else:
                    print("Error ubicación")
                    exit()

            def preparar_Datos(indicaciones_Wifi_Actual,lista_Original,coordenadas_Fijas):
                lista_Copy=list(lista_Original)
                lista_Coordenadas_Fijas_Duplicadas=list(coordenadas_Fijas)
                latitud_1=lista_Copy[indicaciones_Wifi_Actual-1][0]
                longitud_1=lista_Copy[indicaciones_Wifi_Actual-1][1]
                latitud_1=convertir_A_Radianes(latitud_1)
                longitud_1=convertir_A_Radianes(longitud_1)
                
                for x in range(0,len(lista_Coordenadas_Fijas_Duplicadas)):
                    for y in range (0,2):
                    
                        lista_Coordenadas_Fijas_Duplicadas[x][y]=convertir_A_Radianes(lista_Coordenadas_Fijas_Duplicadas[x][y])
                
                Aplicar_Formula_Distancia(latitud_1,longitud_1,lista_Coordenadas_Fijas_Duplicadas)
                
                pass

            def convertir_A_Radianes(valor_A_Convertir):
                return radians(valor_A_Convertir)

            def Aplicar_Formula_Distancia(latitud_1, longitud_1, lista_En_Radianes):
                
                for x in range(0,4):
                    latitud_2=lista_En_Radianes[x][0]
                    longitud_2=lista_En_Radianes[x][1]
                    latitud_Delta=latitud_2-latitud_1
                    longitud_Delta=longitud_2-longitud_1

                    auxiliar_De_Calculo=sin(longitud_Delta/2)**2
                    auxiliar_De_Calculo=auxiliar_De_Calculo*(cos(latitud_1)*cos(latitud_2))
                    auxiliar_De_Calculo=(sin(latitud_Delta/2)**2)+auxiliar_De_Calculo
                    auxiliar_De_Calculo=sqrt(auxiliar_De_Calculo)
                    auxiliar_De_Calculo=asin(auxiliar_De_Calculo)
                    auxiliar_De_Calculo=(2*radio)*auxiliar_De_Calculo

                    auxiliar_De_Calculo=auxiliar_De_Calculo*1000
                    auxiliar_De_Calculo=round(auxiliar_De_Calculo)
                
                    lista_Distancia.append(auxiliar_De_Calculo)

                Ordenar_Distancia(lista_Distancia)

            def Ordenar_Distancia(distancias):
                distancias_Duplicadas=list(distancias)
                min1=distancias_Duplicadas.index(min(distancias_Duplicadas)) 
                distancias_Duplicadas.pop(min1)
            
                min2=distancias.index(min(distancias_Duplicadas))
                        
                
                ImprimirMensajeCercanias(min1,min2,coordenadas_Predeterminada,distancias)

            def ImprimirMensajeCercanias(min1,min2, base_De_Datos,lista_Distancia ):
                for x in range (0,4):
                    base_De_Datos[x][0]=degrees(base_De_Datos[x][0])
                    base_De_Datos[x][1]=degrees(base_De_Datos[x][1])
                

                for x in range (0,len(coordenadas_Predeterminada)):
                    if coordenadas_Predeterminada[min1][0]==coordenadas_Predeterminada[x][0] and coordenadas_Predeterminada[min1][1] == coordenadas_Predeterminada[x][1]:
                        if coordenadas_Predeterminada[x][2]>coordenadas_Predeterminada[min1][2]:
                            min1=coordenadas_Predeterminada.index(coordenadas_Predeterminada[x])
                            

                global distancia_Tiempo 
                if base_De_Datos[min1][2] > base_De_Datos[min2][2]:
                    
                    print(f"La zona wifi 1: ubicada en {base_De_Datos[min1]} a {lista_Distancia[min1]} metros, tiene en promedio {base_De_Datos[min1][2]} usuarios")
                    print(f"La zona wifi 2: ubicada en {base_De_Datos[min2]} a {lista_Distancia[min2]} metros, tiene en promedio {base_De_Datos[min2][2]} usuarios")
                    opciones_De_Destino=int(input("Por favor seleccione el wifi al cual desea ir, para recibir indicaciones: "))
                    if opciones_De_Destino==1: 
                        distancia_Tiempo = lista_Distancia[min1] 
                        dar_Indicaciones(wifi_Actual,base_De_Datos[min1])
                    elif opciones_De_Destino==2:
                        distancia_Tiempo = lista_Distancia[min2]
                        dar_Indicaciones(wifi_Actual,base_De_Datos[min2])
                    else:
                        print("Error: Restaurante destino inválido.111")
                    
                else:
                    print(f"La zona wifi 1: ubicada en {base_De_Datos[min1]} a {lista_Distancia[min1]} metros, tiene en promedio {base_De_Datos[min1][2]} usuarios")
                    print(f"La zona wifi 2: ubicada en {base_De_Datos[min2]} a {lista_Distancia[min2]} metros, tiene en promedio {base_De_Datos[min2][2]} usuarios")
                    opciones_De_Destino=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                    if opciones_De_Destino==1:
                        distancia_Tiempo= lista_Distancia[min2]
                        dar_Indicaciones(wifi_Actual,base_De_Datos[min2])
                    elif opciones_De_Destino==2:
                        distancia_Tiempo= lista_Distancia[min1]
                        dar_Indicaciones(wifi_Actual,base_De_Datos[min1])
                    else:
                        print("Error zona wifi")
                        exit()

            def dar_Indicaciones(wifi_Actual,wifi_Destino):

                latitud_Origen=wifi_Actual[0]
                longitud_Origen=wifi_Actual[1]
                latitud_Destino=wifi_Destino[0]
                longitud_Destino=wifi_Destino[1]

                if latitud_Origen>latitud_Destino:
                    texto_1="el sur"
                elif latitud_Origen<latitud_Destino:
                    texto_1="el norte"

                else:
                    texto_1=""
                
                if longitud_Origen>longitud_Destino:
                    texto_2="el occidente"
                elif longitud_Origen<longitud_Destino:
                    texto_2="el oriente"
                else:
                    texto_2=""

                if texto_1=="" and texto_2!="": 
                    print(f"Debe ir hacia {texto_2}")

                elif texto_2=="" and texto_1!="": 
                    print(f"Debe ir hacia {texto_1}")

                elif texto_1=="" and texto_2=="":
                    print("Usted ya está en el destino")
                    

                else:
                    print(f"Debe dirigirse primero hacia {texto_1} y luego hacia {texto_2}")
                    
                    calcular_Tiempo_Recorrido()    
   
            def calcular_Tiempo_Recorrido():
                tiempo_1="segundos" 
                tiempo_2="segundos"
                
                if distancia_Tiempo==0: 
                    pass
                    
                else:
                    bus=distancia_Tiempo/16.67
                    moto=distancia_Tiempo/19.44
                    
                    if bus > 60: 
                        bus=bus/60
                        tiempo_1="minutos"
                    
                    
                    if moto > 60:
                        moto=moto/60
                        tiempo_2="minutos"
                    
                    moto=round(moto,2) 
                    bus=round(bus,2)
                    
                
                    print(f"Se tardará aproximadamente {bus} {tiempo_1} en bus; y {moto} {tiempo_2} en moto")

                    temporal_1=distancia_Tiempo
                    temporal_2="En bus tardarías "
                    temporal_3=f"{bus} {tiempo_1}"
                    temporal_4="moto"
                    temporal_5=moto

                    informacion["recorrido"]=[temporal_1,temporal_2,temporal_3,temporal_4,temporal_5]

                    global alistamiento

                    alistamiento=True

                    opcion = int(input("Presione 0 para salir"))
                    if opcion == 0:
                        return
                    else:
                        print("Error")
                        exit()

            def leer_Archivo(archivo):

                try:
                    archivo_Por_Linea=open(archivo).readline()
                    archivo_Por_Linea=archivo_Por_Linea.split(";")
                    lista_Coordenada_Temporal=[]

                    for x in range(0,4):
                        lista_Coordenada_Temporal.append([])
                        temporal=archivo_Por_Linea[x].split(",")

                        for y in range(0,3):
                            lista_Coordenada_Temporal[x].append(temporal[y])

                    for x in range(len(lista_Coordenada_Temporal)):
                        for y in range(0,len(lista_Coordenada_Temporal[x])):
                            lista_Coordenada_Temporal[x][y]=float(lista_Coordenada_Temporal[x][y])
                            if y==2:
                                lista_Coordenada_Temporal[x][y]=int(lista_Coordenada_Temporal[x][y])

                    print("Coordenadas actualizadas")

                    return lista_Coordenada_Temporal
                #en caso de errores simulamos la creación de la lista mostrando un error
                #y mandando los datos al return
                except IOError:
                    print("Error en creacion de fichero")
                    return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]

                except FileNotFoundError:
                    print("Error el archivo no existe")
                    return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]
                except ValueError:
                    print("Dato Inválido")
                    return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]
                except:
                    print("Error.")
                    return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]
            
            #creamos la función que permite crear el archivo.        
            def CrearArchivo():
                #revisamos si la variable alistamiento nos permite continuar.
                if alistamiento:
                    #de nuevo trabajamos con un try para evitar problemas
                    try:
                        #creamos un archivo en modo escritura (se crea siempre, se sobre escribe lo anterior)
                        #cambiamos la codificacion a utf-8 para latino.
                        archivo=open("archivoescritura.txt","w",encoding="utf-8")
                        #escribimos el diccionar que creamos durante la ejecución del programa
                        archivo.write(str(informacion))
                        print(informacion)
                        opcion = int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal"))
                        if opcion == 1:
                            print("Exportando archivo")
                            exit()
                        elif opcion == 0:
                            return
                        return
                    except:
                        exit()
                else:
                    print("Error de alistamiento")
                    exit()
            
            while error < 4:

                for i in range(1,8):
                    if i == 1:
                        print(f"{i}. {opcion1}")
                    elif i == 2:
                        print(f"{i}. {opcion2}")
                    elif i == 3:
                        print(f"{i}. {opcion3}")
                    elif i == 4:
                        print(f"{i}. {opcion4}")
                    elif i == 5:
                        print(f"{i}. {opcion5}")
                    elif i == 6:
                        print(f"{i}. {opcion6}")
                    elif i == 7:
                        print(f"{i}. {opcion7}")

                opcionMenu = int(input("Elija una opción"))

                if opcionMenu == 1:
                    print("Usted ha elegido la opción 1")
                    clv_Actual = input("Ingrese contraseña actual: ")
                    if clv_Actual!= clv: #Validación de contraseña
                        print("Error") #Contraseña incorrecta
                        break
                    else:
                        print("Contraseña actual confirmada")
                        clv_Nueva = input("Ingrese nueva contraseña: ")
                        if clv_Nueva == clv:
                            print("La nueva contraseña debe ser diferente a la actual")
                        else:
                            clv = clv_Nueva
                elif opcionMenu == 2:
                    print("Usted ha elegido la opción 2")
                    if lista_Coordenadas == []:
                        lista_Coordenadas = ingresar_Coordenadas(lista_Coordenadas)
                        if lista_Coordenadas != "Error":
                            lista_Coordenadas == True
                        else:
                            break
                    else:
                        imprimir_Coordenads(lista_Coordenadas)                 
                elif opcionMenu == 3:
                    wifi_Favorito(lista_Coordenadas)
                elif opcionMenu == 4:
                    print("Usted ha elegido la opción 4")
                    CrearArchivo()
                elif opcionMenu == 5:
                    print("Usted ha elegido la opción 5")
                    coordenadas_Predeterminada = (leer_Archivo("archivolectura.txt"))
                elif opcionMenu == 6:
                    
                    for i in range(1,6):
                        if i == 1:
                            print(f"{i}. {opcion1}")
                        elif i == 2:
                            print(f"{i}. {opcion2}")
                        elif i == 3:
                            print(f"{i}. {opcion3}")
                        elif i == 4:
                            print(f"{i}. {opcion4}")
                        elif i == 5:
                            print(f"{i}. {opcion5}")

                    opcionFavorita = int(input("Seleccione opción favorita"))
                    if opcionFavorita > 0 and opcionFavorita < 6:
                        
                        adivinanza_primera_string = int(input("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es =\n "))
                        if adivinanza_primera_string != adivinanza_primera :
                            os.system("cls")
                            print("Error")
                        else:
                            adivinanza_segunda_string =int(input("Redondo soy y es cosa anunciada. Si estoy a la derecha algo valgo, pero a la izquierda soy nada, la respuesta es =\n "))
                            if adivinanza_segunda_string != adivinanza_segunda :
                                os.system("cls")
                                print("Error")
                        if opcionFavorita == 2:
                            opcion1 = opcion2Copy
                            opcion2 = opcion1Copy
                        elif opcionFavorita == 3:
                            opcion1 = opcion3Copy
                            opcion2 = opcion1Copy
                            opcion3 = opcion2Copy
                        elif opcionFavorita == 4:
                            opcion1=opcion4Copy
                            opcion2=opcion1Copy
                            opcion3=opcion2Copy
                            opcion4=opcion3Copy
                        elif opcionFavorita == 5:
                            opcion1=opcion5Copy
                            opcion2=opcion1Copy
                            opcion3=opcion2Copy
                            opcion4=opcion3Copy
                            opcion5=opcion4Copy

                    else:
                        print("Error")
                        break
            
                elif opcionMenu == 7:
                    print("Hasta pronto")
                    break
                else:
                    print("Error")
                    error = error + 1