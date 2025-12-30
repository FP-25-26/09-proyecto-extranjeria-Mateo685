from extranjeria import *


def test_lee_datos_extranjeria(ruta_fichero):
    print("TEST de lee_datos_extranjeria")
    print(lee_datos_extranjeria(ruta_fichero))

def test_numero_nacionalidades_distintas(registros):
    print("TEST de 'numero_nacionalidades_distintas'")
    print(numero_nacionalidades_distintas(registros))

def test_secciones_distritos_con_extranjeros_nacionalidades(registros):
    print("TEST de 'secciones_distritos_con_extranjeros_nacionalidades'")
    paises = {'ITALIA', 'ALEMANIA'}
    print(secciones_distritos_con_extranjeros_nacionalidades(registros, paises)[:3])

def test_total_extranjeros_por_pais(registros):
    print("Mostrando el número de residentes para algunos países de procedencia:")
    paises = total_extranjeros_por_pais(registros)
    for pais in paises:    
        if pais == "ALEMANIA" or pais == "ITALIA" or pais == "MARRUECOS":
            print(f"{pais} : {paises[pais]}")

def test_top_n_extranjeria(registros):
    print("TEST de 'secciones_distritos_con_extranjeros_nacionalidades'")
    print("Mostrando los 5 países de los que proceden más residentes:")
    print(top_n_extranjeria(registros, 5))

def test_barrio_mas_multicultural(registros):
    print("TEST de 'barrio_mas_multicultural'")
    print(f"El barrio más multicultural de sevilla es {barrio_mas_multicultural(registros)}")

def test_barrio_con_mas_extranjeros(registros):
    print("TEST de 'barrio_con_mas_extranjeros'")
    print(f"El barrio con más  residentes extranjeros es {barrio_con_mas_extranjeros(registros)}")
    print(f"El barrio con más hombres residentes extranjeros es {barrio_con_mas_extranjeros(registros, "Hombres")}")
    print(f"El barrio con más mujeres residentes extranjeros es {barrio_con_mas_extranjeros(registros, "Mujeres")}")


if __name__ == "__main__":
    datos = lee_datos_extranjeria("data\extranjeriaSevilla.csv")

   
    test_barrio_con_mas_extranjeros(datos)