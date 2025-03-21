print("Este programa es para ayudarte a la entrega de termos a las ciudades:")
print("0)Universidad\n1)Cajica\n2)Villavicencio\n3)Soacha\nTunja\nToca\nLa Calera\nLa Vega")
# Definir funciones para cada ciudad
def universidad(destino):
    rutas = {
        0: "Ya estás en la U",
        1: "por autopista Nte. y Auto. Norte = 49min-32.4km",
        2: "rapida = por Via Bogota/Villavicencio y carretera 40 = 3.13hrs-121km\noptima = por carretera 40c via Bogota/Villavicencio y carretera 40 = 3.15hrs-114",
        3: "por autopista Sur = 1hr-24.5km",
        4: "por Briceno/Tunja/Sogamoso = 2.24hrs-144km",
        5: "por Briceno/Tunja/Sogamoso = 3.1hrs-167km",
        6: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega = 1.33hrs-66.3km",
        7: "Via Bogota/La Calera = 37min-18km"
    }
    mostrar_ruta(destino, rutas)

def cajica(destino):
    rutas = {
        0: "Por autopista norte = 1.2hrs-31.7km",
        1: "Ya estás en Cajicá",
        2: "Por via Bogota/Villavicencio y carretera 40 = 3.53hrs-149km",
        3: "Por av Cdad de Quito = 1.42hrs-56.6km",
        4: "Por Briceno/Tunja/Sogamoso = 1.56hrs-117km",
        5: "Por Briceno/Tunja/Sogamoso = 2.33hrs-140km",
        6: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega = 1.50hrs-78.1km\noptima = por Subachoque-El Rosal y Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega - Villeta = 1.57hrs-74.9km",
        7: "por Perimetral de Ote. de Cundinamarca y Bogota-Guatavita = 54min-37.7km"
    }
    mostrar_ruta(destino, rutas)

def villavicencio(destino):
    rutas = {
        0: "Rapida = por Via Bogota/Villavicencio \noptima = av 40, Via Bogota/Villavicencio y Carretera 40C = 3.33hrs-115km",
        1: "Via Bogota/Villavicencio y Autopista Nte = 4.18hrs-150km",
        2: "Ya estás en Villavicencio",
        3: "Via Bogota/Villavicencio y Autopista Sur = 2.56hrs-114km",
        4: "Via Bogota/Villavicencio y Briceno/Tunja = 5.44hrs-262km",
        5: "Via Bogota/Villavicencio y Briceno/Tunja = 6.16hrs-282km",
        6: "Via Bogota/Villavicencio y Siberia = 4.39hrs-180km",
        7: "por Vía Bogotá - Villavicencio = 3.57hrs-136km"
    }
    mostrar_ruta(destino, rutas)

def soacha(destino):
    rutas = {
        0: "Por autopista Sur y Av cdad de Quito/avNQS = 1.1hrs-24.7km",
        1: "Por autopista Sur = 1.46hrs-53.7km",
        2: "Via Bogota/Villavicencio y Carretera 40 = 2.49hrs-114km",
        3: "Ya estás en Soacha",
        4: "Por Briceno/Tunja/Sogamoso = 3.17hrs- 165km",
        5: "Por Briceno/Tunja/Sogamoso = 3.54hrs-188km",
        6: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega = 2.7hrs-83.1km",
        7: "Autopista Sur y Bogota/La Calera = 1.26hrs-39.4km"
    }
    mostrar_ruta(destino, rutas)

def tunja(destino):
    rutas = {
        0: "Por villapinzon/Tunja/Briceno y autopista nte = 2.38hrs-144km",
        1: "Por villapinzon/Tunja/Briceno = 1.57hrs-119km",
        2: "Por villapinzon/Tunja/Briceno y Via Bogota/Villavicencio = 5.44hrs-261km",
        3: "Por villapinzon/Tunja/Briceno y Autopista Sur = 3.34hrs-165km",
        4: "Ya estás en Tunja",
        5: "Por chivata = 49min-28.3km",
        6: "Por villapinzon/Tunja/Briceno y Siberia = 3.33hrs-197km",
        7: "Por villapinzon/Tunja/Briceno = 2.18hrs-138km"
    }
    mostrar_ruta(destino, rutas)

def toca(destino):
    rutas = {
        0: "Por villapinzon/Tunja/Briceno y Autopista Nte = 3.11hrs-165km",
        1: "Por villapinzon/Tunja/Briceno = 2.32hrs-140km",
        2: "Por villapinzon/Tunja/Briceno y Bogota/Villavicencio = 6.21hrs-282km ",
        3: "Por villapinzon/Tunja/Briceno y Autopista Sur = 4.8hrs-186km",
        4: "Por chivata = 47min-26.4km",
        5: "Ya estás en Toca",
        6: "Por villapinzon/Tunja/Briceno y Siberia = 4.8hrs-219km",
        7: "Por villapinzon/Tunja/Briceno y Sopo/La calera = 2.53hrs-159km"
    }
    mostrar_ruta(destino, rutas)

def la_vega(destino):
    rutas = {
        0: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega = 1.51hrs-67.1km",
        1: "La Punta - El Vino - La Vega - Tabio = 1.56hrs-73.2km",
        2: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega - Villeta y Vía Bogotá - Villavicencio = 4.43hrs-180km",
        3: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega - Villeta y Carretera 21 = 2.5hrs-79.3km",
        4: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega y Por villapinzon/Tunja/Briceno = 3.34hrs-194km",
        5: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega y Por villapinzon/Tunja/Briceno = 4.5hrs-214km",
        6: "Ya estás en La Vega",
        7: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega y Bogota/La Calera = 2.25hrs-84.6km"
    }
    mostrar_ruta(destino, rutas)

def la_calera(destino):
    rutas = {
        0: "por Bogota-Guatavita y Bogotá - La Calera = 38min-17.9km",
        1: "por Bogota-Guatavita y Perimetral de Ote. de Cundinamarca = 1hr-39.1km",
        2: "Bogota/La Calrea y Via Bogota/Villavicencio = 3;32hrs-134km",
        3: "Por Bogota/Guatavita y Autopista Sur = 1.37hrs-40km",
        4: "LaCalera\Sopo y Tunja/Briceno = 2.18hrs-137km",
        5: "Por Sopo/La Calera y Por villapinzon/Tunja/Briceno = 2.51hrs-158km",
        6: "por Santafé de Bogotá (Puente el Cortijo) - Siberia - La Punta - El Vino - La Vega - Villeta = 2.13hrs-84.4km",
        7: "Ya estás en La Calera"
    }
    mostrar_ruta(destino, rutas)

# Función para mostrar la ruta
def mostrar_ruta(destino, rutas):
    if destino in rutas:
        if "Ya estás en" in rutas[destino]:
            print(rutas[destino])
        else:
            print(f"{rutas[destino]}")
            print("0)Universidad\n1)Cajica\n2)Villavicencio\n3)Soacha\n4)Tunja\n5)Toca\n6)La Calera\n7)La Vega")
    else:
        print("Ciudad no válida.")

# Diccionario de ciudades con sus funciones
ciudades = {
    0: universidad,
    1: cajica,
    2: villavicencio,
    3: soacha,
    4: tunja,
    5: toca,
    6: la_vega,
    7: la_calera
}

# Inicio en la Universidad (0)
ubicacion_actual = 0  

while True:
    print(f"\nEstás en la ciudad {ubicacion_actual}")
    destino = int(input("Ingresa un número del 0 al 7 para encontrar la ruta optima hacia el pueblo del numero que dijitaste: "))

    if destino == 0:
        print("Volviste a la universidad")
        break  # Finaliza el bucle

    if ubicacion_actual in ciudades:
        ciudades[ubicacion_actual](destino)  # Llama a la función de la ciudad actual con el destino
        ubicacion_actual = destino  # Actualiza la ubicación actual
    else:
        print("Ciudad no válida.")
