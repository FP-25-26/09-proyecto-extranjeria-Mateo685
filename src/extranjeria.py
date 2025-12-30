from typing import NamedTuple
import csv

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)



def lee_datos_extranjeria(ruta_fichero:str)->list[RegistroExtranjeria]:
    registros = []
    with open(ruta_fichero, encoding = 'utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            distrito = distrito.strip()
            seccion = seccion.strip()
            barrio = barrio.strip()
            pais = pais.strip()
            hombres = int(hombres)
            mujeres = int(mujeres)
            tupla_aux = RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres)
            registros.append(tupla_aux)
    return registros

def numero_nacionalidades_distintas(registros:list[RegistroExtranjeria])->int:
    nacionalidades = []
    for registro in registros:
        if registro.pais not in nacionalidades:
            nacionalidades.append(registro.pais)
    return len(nacionalidades)         

def secciones_distritos_con_extranjeros_nacionalidades(registros:list[RegistroExtranjeria], paises:set[str])->list[(str, str)]:
    filtrado = [registro for registro in registros if registro.pais in paises ]
    filtrado_sin_repeticion = set((distrito, seccion) for distrito, seccion, barrio, pais, hombres, mujeres in filtrado)
    print(len(filtrado_sin_repeticion))
    return sorted(list(filtrado_sin_repeticion))

def total_extranjeros_por_pais(registros:list[RegistroExtranjeria])->dict[str,int]:
    res = dict()
    for registro in registros:
        if registro.pais in res:
            res[registro.pais] += registro.mujeres + registro.hombres
        else:
            res[registro.pais] = registro.mujeres + registro.hombres
    return res             

def top_n_extranjeria(registros:list[RegistroExtranjeria], n:int=3)-> list[(str, int)]:
    listado = total_extranjeros_por_pais(registros)
    return sorted(listado.items(), key = lambda x: x[1] , reverse = True)[:n]

def barrio_mas_multicultural(registros:list[RegistroExtranjeria])->str:
    barrios = dict()
    for registro in registros:
        if registro.barrio in barrios:
            barrios[registro.barrio] += registro.hombres + registro.mujeres
        else:
            barrios[registro.barrio] = registro.hombres + registro.mujeres
    barrio_mas_multicultural = max(barrios.items(), key = lambda x: x[1])
    return barrio_mas_multicultural[0]        

def barrio_con_mas_extranjeros(registros:list[RegistroExtranjeria], tipo:str=None)->str:
    barrios = dict()
    
    for registro in registros:
        if tipo == None:    
            if registro.barrio in barrios:
                barrios[registro.barrio] += registro.hombres + registro.mujeres
            else:
                barrios[registro.barrio] = registro.hombres + registro.mujeres
        elif tipo == "Hombres":
            if registro.barrio in barrios:
                barrios[registro.barrio] += registro.hombres
            else:
                barrios[registro.barrio] = registro.hombres
        else:
            if registro.barrio in barrios:
                barrios[registro.barrio] += registro.mujeres
            else:
                barrios[registro.barrio] = registro.mujeres 
        barrio_mas_multicultural = max(barrios.items(), key = lambda x: x[1])
        res = barrio_mas_multicultural[0]  
    return res 

def pais_mas_representado_por_distrito(registros:list[RegistroExtranjeria])->dict[str, str]:
    res = dict()
    dict_auxiliar = dict()
    for registro in registros:
        if        